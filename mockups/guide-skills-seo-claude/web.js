(function(){
  var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var KEY='guide-skills-seo:v1',state={copied:{},fields:{},pos:0,sec:'',mode:'read'};
  try{var raw=localStorage.getItem(KEY);if(raw){var o=JSON.parse(raw);for(var k in o)state[k]=o[k]}}catch(e){}
  function save(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}
  var saved={pos:state.pos,sec:state.sec},hold=false;

  /* progression, section en cours, temps restant */
  var bar=$('.progress i'),cur=$('.where .cur'),startLabel=cur.textContent,timeB=$('.time b'),article=$('article');
  var links=$$('nav.toc a'),sheetLinks=$$('.sheet a'),heads=links.map(function(a){return document.getElementById(a.hash.slice(1))});
  var words=0;$$('article>p,article>ul,article>h2,article>h3,article>h4').forEach(function(n){words+=n.textContent.trim().split(/\s+/).length});
  var total=Math.max(1,Math.round(words/200)),tick=false,last=0;
  function onScroll(){
    tick=false;
    var h=document.documentElement,max=h.scrollHeight-h.clientHeight,r=max>0?Math.min(1,h.scrollTop/max):0;
    bar.style.transform='scaleX('+r+')';
    var a=article.getBoundingClientRect(),ar=Math.min(1,Math.max(0,(innerHeight*0.4-a.top)/a.height));
    timeB.textContent=Math.max(0,Math.round(total*(1-ar)));
    var idx=-1;heads.forEach(function(el,i){if(el.offsetParent!==null&&el.getBoundingClientRect().top<=140)idx=i});
    [links,sheetLinks].forEach(function(set){set.forEach(function(l,i){l.classList.toggle('on',i===idx);if(i===idx)l.setAttribute('aria-current','true');else l.removeAttribute('aria-current')})});
    cur.textContent=idx<0?startLabel:links[idx].textContent;
    var now=Date.now();if(!hold&&now-last>600){last=now;state.pos=r;state.sec=idx<0?'':links[idx].textContent;save()}
  }
  addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});
  onScroll();

  /* apparition au premier passage */
  var revs=$$('.reveal');
  if('IntersectionObserver' in window&&!reduce){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('seen');io.unobserve(en.target)}})},{rootMargin:'0px 0px -12% 0px'});
    revs.forEach(function(el){io.observe(el)});
  }else revs.forEach(function(el){el.classList.add('seen')});

  /* sommaire mobile */
  var sheet=$('.sheet');
  $('.where').addEventListener('click',function(){sheet.showModal()});
  $('.sx').addEventListener('click',function(){sheet.close()});
  sheet.addEventListener('click',function(ev){if(ev.target===sheet||ev.target.closest('a'))sheet.close()});

  function fallback(text){var a=document.createElement('textarea');a.value=text;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}a.remove()}
  function copyText(text,btn,done){
    var ok=function(){var l=$('.lbl',btn);btn.classList.add('ok');l.textContent=btn.dataset.copied;setTimeout(function(){btn.classList.remove('ok');l.textContent=btn.dataset.copy},1600);if(done)done()};
    if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(text).then(ok,function(){fallback(text);ok()});else{fallback(text);ok()}
  }
  function filled(row){var out='';$('.cons',row).childNodes.forEach(function(n){out+=n.nodeType===3?n.textContent:(n.value.trim()||n.dataset.ph)});return out}
  $$('.fill').forEach(function(inp){
    var fit=function(){inp.size=Math.max(4,(inp.value||inp.placeholder).length)};
    if(state.fields[inp.dataset.k])inp.value=state.fields[inp.dataset.k];fit();
    inp.addEventListener('input',function(){state.fields[inp.dataset.k]=inp.value;save();fit()});
  });
  $$('.crow').forEach(function(row){$('.copyc',row).addEventListener('click',function(){copyText(filled(row),this)})});

  /* mode lecture / skills */
  var modeBtns=$$('.seg2 button');
  function setMode(m,scroll){
    state.mode=m;save();document.body.classList.toggle('tools',m==='tools');
    modeBtns.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.mode===m)});
    if(scroll)$('.wrap').scrollIntoView({block:'start'});
    onScroll();
  }
  modeBtns.forEach(function(b){b.addEventListener('click',function(){setMode(b.dataset.mode,true)})});
  if(state.mode==='tools')setMode('tools',false);

  /* consignes */

  /* l'adresse email : aucun skill ne part sans elle. Même base, même cookie et même
     souvenir que organikk.co/skills : quelqu'un déjà connu là-bas n'est pas redemandé ici. */
  var G=window.GUIDE,MAIL_API='/api/skill-emails',MAIL_STATE='organikk-skills-mail',MAIL_COOKIE='organikk_skills_mail';
  function memo(v){try{return v===undefined?localStorage.getItem(MAIL_STATE):localStorage.setItem(MAIL_STATE,v)}catch(e){return null}}
  function cookieMail(){try{return document.cookie.split('; ').some(function(c){return c.indexOf(MAIL_COOKIE+'=')===0})}catch(e){return false}}
  function aMail(){if(memo()==='ok')return true;if(!cookieMail())return false;memo('ok');return true}
  var mbox=$('.mailbox'),mform=$('.mw-in',mbox),mfield=$('.mw-mail',mbox),mlab=$('.mw-lab',mbox),msuite=null,mslug='';
  function gate(slug,label,suite){
    if(aMail()){suite();return}
    mslug=slug;msuite=suite;mlab.textContent=label;mfield.value='';mbox.showModal();
    setTimeout(function(){mfield.focus()},60);
  }
  mform.addEventListener('submit',function(ev){
    ev.preventDefault();
    var email=mfield.value.trim();
    if(!/^[^\s@]+@[^\s@.]+\.[^\s@]+$/.test(email)){mbox.classList.add('bad');mfield.focus();setTimeout(function(){mbox.classList.remove('bad')},900);return}
    memo('ok');
    fetch(MAIL_API,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({email:email,slug:mslug,source:location.pathname,site:$('.mw-pot input',mbox).value})}).catch(function(){/* la base n'a pas répondu : le fichier part quand même */});
    mbox.close();
    if(msuite){var f=msuite;msuite=null;f()}   // la copie part dans le geste de l'envoi, sans attendre le réseau
  });
  $('.mw-back',mbox).addEventListener('click',function(){msuite=null;mbox.close()});
  mbox.addEventListener('click',function(ev){if(ev.target===mbox){msuite=null;mbox.close()}});
  /* skills */
  var skills=$$('.skillbox'),pill=$('.pill');
  function count(){$('b',pill).textContent=skills.filter(function(s){return state.copied[s.id]}).length+' / '+skills.length}
  function download(name,blob){var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(a.href)},2000)}
  skills.forEach(function(s){
    var more=$('.more',s),wrap=$('.swrap',s),pre=$('pre',wrap);
    function toggle(open){
      if(open===s.classList.contains('open'))return;
      var from=wrap.offsetHeight;
      if(open){s.classList.add('open');var to=wrap.scrollHeight;wrap.style.height=from+'px';wrap.offsetHeight;wrap.style.height=to+'px'}
      else{wrap.style.height=from+'px';wrap.offsetHeight;wrap.style.height='190px'}
      var end=function(){wrap.removeEventListener('transitionend',end);if(!open)s.classList.remove('open');wrap.style.height=''};
      if(reduce)end();else wrap.addEventListener('transitionend',end);
      more.setAttribute('aria-expanded',open);more.textContent=open?more.dataset.hide:more.dataset.show;
      if(!open)s.scrollIntoView({block:'nearest'});
    }
    more.addEventListener('click',function(){toggle(!s.classList.contains('open'))});
    $('.copy',s).addEventListener('click',function(){var b=this;gate(s.dataset.name,G.mw.copy,function(){copyText(pre.textContent,b,function(){state.copied[s.id]=1;save();count()})})});
    $('.dl',s).addEventListener('click',function(){gate(s.dataset.name,G.mw.dl,function(){download(s.dataset.name+'.md',new Blob([pre.textContent+'\n'],{type:'text/markdown'}))})});
    $$('.chipb',s).forEach(function(c){c.addEventListener('click',function(){var t=document.getElementById(c.dataset.t);t.scrollIntoView({block:'start'});t.classList.add('flash');setTimeout(function(){t.classList.remove('flash')},1200)})});
  });
  function md(s){return esc(s).replace(/`([^`]+)`/g,'<code>$1</code>')}
  function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;')}
  pill.addEventListener('click',function(){var t=skills.filter(function(s){return !state.copied[s.id]})[0]||skills[0];if(!document.body.classList.contains('tools')&&t.offsetParent===null)setMode('tools');t.scrollIntoView({block:'start'})});
  count();

  /* zip sans dépendance (méthode « stored ») */
  var crcT=(function(){var t=[],c,n,k;for(n=0;n<256;n++){c=n;for(k=0;k<8;k++)c=c&1?0xEDB88320^(c>>>1):c>>>1;t[n]=c>>>0}return t})();
  function crc(b){var c=-1;for(var i=0;i<b.length;i++)c=crcT[(c^b[i])&255]^(c>>>8);return (c^-1)>>>0}
  function zip(files){
    var enc=new TextEncoder(),parts=[],central=[],off=0;
    files.forEach(function(f){
      var name=enc.encode(f.name),data=enc.encode(f.text),c=crc(data),h=new DataView(new ArrayBuffer(30));
      h.setUint32(0,0x04034b50,true);h.setUint16(4,20,true);h.setUint16(6,0x0800,true);h.setUint32(14,c,true);h.setUint32(18,data.length,true);h.setUint32(22,data.length,true);h.setUint16(26,name.length,true);
      parts.push(h,name,data);
      var d=new DataView(new ArrayBuffer(46));
      d.setUint32(0,0x02014b50,true);d.setUint16(4,20,true);d.setUint16(6,20,true);d.setUint16(8,0x0800,true);d.setUint32(16,c,true);d.setUint32(20,data.length,true);d.setUint32(24,data.length,true);d.setUint16(28,name.length,true);d.setUint32(42,off,true);
      central.push(d,name);off+=30+name.length+data.length;
    });
    var size=central.reduce(function(s,p){return s+p.byteLength},0),e=new DataView(new ArrayBuffer(22));
    e.setUint32(0,0x06054b50,true);e.setUint16(8,files.length,true);e.setUint16(10,files.length,true);e.setUint32(12,size,true);e.setUint32(16,off,true);
    return new Blob(parts.concat(central,[e]),{type:'application/zip'});
  }
  $('.dlall').addEventListener('click',function(){gate('',G.mw.dl,function(){download(window.GUIDE.zip,zip(skills.map(function(s){return {name:s.dataset.name+'/SKILL.md',text:$('.swrap pre',s).textContent+'\n'}})))})});

  /* reprise de lecture */
  var res=$('.resume');
  if(saved.pos>0.08&&saved.pos<0.97&&scrollY<200){
    $('.rs',res).textContent=saved.sec||Math.round(saved.pos*100)+' %';res.hidden=false;hold=true;
    $('.go',res).addEventListener('click',function(){var h=document.documentElement;scrollTo({top:saved.pos*(h.scrollHeight-h.clientHeight)});res.hidden=true;hold=false});
    $('.rx',res).addEventListener('click',function(){res.hidden=true;hold=false});
    addEventListener('scroll',function hide(){if(scrollY>innerHeight){res.hidden=true;hold=false;removeEventListener('scroll',hide)}},{passive:true});
  }
})();
