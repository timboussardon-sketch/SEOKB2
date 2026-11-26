#!/usr/bin/env python3
"""Envoi des alertes et du récap à l'élève : Gmail (mot de passe d'application) et/ou WhatsApp (CallMeBot).

Réglages lus dans le .env.local du coffre :
  CANAL=gmail | whatsapp | gmail,whatsapp
  GMAIL_ADRESSE, GMAIL_MOT_DE_PASSE_APPLICATION, ALERTES_DESTINATAIRE (par défaut GMAIL_ADRESSE)
  WHATSAPP_NUMERO (format international, +33…), CALLMEBOT_APIKEY
Rien n'est envoyé à une autre adresse ni à un autre numéro que ceux de l'élève.
"""
import html, smtplib, urllib.parse, urllib.request
from email.message import EmailMessage

WHATSAPP_MAX = 1500  # au-delà, CallMeBot coupe ou refuse le message


def canaux(cfg):
    return [c.strip() for c in (cfg.get('CANAL') or 'gmail').lower().split(',') if c.strip()]


def manquants(cfg):
    out = []
    for c in canaux(cfg):
        if c == 'gmail':
            out += [k for k in ('GMAIL_ADRESSE', 'GMAIL_MOT_DE_PASSE_APPLICATION') if not cfg.get(k)]
        elif c == 'whatsapp':
            out += [k for k in ('WHATSAPP_NUMERO', 'CALLMEBOT_APIKEY') if not cfg.get(k)]
        else:
            out.append(f'CANAL inconnu : {c} (gmail ou whatsapp)')
    return out


def page_html(titre, lignes):
    items = ''.join(f'<li style="margin:4px 0">{html.escape(l)}</li>' for l in lignes)
    return ('<!doctype html><html lang="fr"><head><meta charset="utf-8"></head>'
            '<body style="margin:0;background:#fff;color:#1d2230;font-family:Arial,sans-serif;font-size:15px;line-height:1.5">'
            f'<div style="max-width:640px;margin:0 auto;padding:24px 20px"><div style="font-size:18px;font-weight:bold;margin-bottom:12px">'
            f'{html.escape(titre)}</div><ul style="margin:0;padding-left:20px">{items}</ul></div></body></html>')


def texte_whatsapp(titre, lignes):
    corps, reste = f'*{titre}*', len(lignes)
    for l in lignes:
        ajout = '\n' + l
        if len(corps) + len(ajout) > WHATSAPP_MAX - 40:
            corps += f'\n… et {reste} ligne(s) de plus, voir le rapport du coffre'
            break
        corps += ajout
        reste -= 1
    return corps


def envoyer_gmail(cfg, titre, lignes):
    m = EmailMessage()
    m['From'] = cfg['GMAIL_ADRESSE']
    m['To'] = cfg.get('ALERTES_DESTINATAIRE') or cfg['GMAIL_ADRESSE']
    m['Subject'] = titre
    m.set_content('\n'.join(lignes))
    m.add_alternative(page_html(titre, lignes), subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=60) as s:
        s.login(cfg['GMAIL_ADRESSE'], cfg['GMAIL_MOT_DE_PASSE_APPLICATION'].replace(' ', ''))
        s.send_message(m)


def envoyer_whatsapp(cfg, titre, lignes):
    q = urllib.parse.urlencode({'phone': cfg['WHATSAPP_NUMERO'].replace(' ', ''),
                                'text': texte_whatsapp(titre, lignes), 'apikey': cfg['CALLMEBOT_APIKEY']})
    r = urllib.request.urlopen(urllib.request.Request('https://api.callmebot.com/whatsapp.php?' + q,
                                                      headers={'User-Agent': 'SEOKB2'}), timeout=60)
    corps = r.read().decode('utf-8', 'replace')
    if r.status != 200 or 'ERROR' in corps.upper():
        raise RuntimeError('CallMeBot : ' + ' '.join(corps.split())[:200])


def envoyer(cfg, titre, lignes):
    """Envoie sur chaque canal réglé. Renvoie {canal: 'ok' | message d'erreur}."""
    res = {}
    for c in canaux(cfg):
        try:
            (envoyer_gmail if c == 'gmail' else envoyer_whatsapp)(cfg, titre, lignes)
            res[c] = 'ok'
        except Exception as e:  # un canal en panne n'empêche pas l'autre
            res[c] = f'{type(e).__name__} : {e}'
    return res
