import type { DraftSentence, Fact, SentenceCheck } from "../core/claims";
import type { KeywordCandidate, ServiceRef } from "../core/keywords";
import type { Citation } from "../core/verdict";

export interface Usage {
  model: string;
  input_tokens: number;
  output_tokens: number;
  web_search_calls: number;
  /** Usage tel que rapporté par le fournisseur, conservé tel quel. */
  reported: unknown;
}

/** Majorant de consommation d'un appel, utilisé pour réserver le budget avant de l'émettre. */
export interface CallEstimate {
  model: string;
  input_tokens: number;
  output_tokens: number;
  web_search_calls: number;
}

export interface SearchCandidate {
  name: string | null;
  website: string;
  source_url: string;
  snippet: string;
}

export interface SearchProvider {
  name: string;
  model: string;
  estimate(): CallEstimate;
  search(query: string, limit: number, excludeDomains: string[]): Promise<{ candidates: SearchCandidate[]; usage: Usage }>;
}

export interface VisibilityAnswer {
  text: string;
  citations: Citation[];
  webSearchUsed: boolean;
  responseId: string | null;
  usage: Usage;
}

export interface VisibilityProvider {
  name: "CLAUDE_API_WEB_SEARCH" | "OPENAI_API_WEB_SEARCH" | "OPENAI_CODEX_WEB_SEARCH" | "SIMULATION";
  model: string;
  params: Record<string, unknown>;
  requireWebSearch: boolean;
  estimate(): CallEstimate;
  /** Chaque appel est une conversation neuve, sans historique ni cache applicatif. */
  ask(prompt: string, city: string): Promise<VisibilityAnswer>;
}

export interface PageDigest {
  url: string;
  title: string | null;
  h1s: string[];
  text: string;
}

export interface Quote {
  value: string;
  source_url: string;
  excerpt: string;
}

export interface SiteProfile {
  firm_name: Quote | null;
  lawyers: { first_name: string; last_name: string; source_url: string; excerpt: string }[];
  cities: Quote[];
  practice_areas: (Quote & { matches_target: boolean })[];
  client_types: (Quote & { value: "entreprise" | "particulier" })[];
  services: Quote[];
  certification_claims: Quote[];
}

export interface ProfileRequest {
  pages: PageDigest[];
  practice: string;
  subspecialties: string[];
  city: string;
}

export interface KeywordRequest {
  services: ServiceRef[];
  city: string;
  clientTypes: ("entreprise" | "particulier")[];
  count: number;
  round: number;
  alreadyKept: string[];
}

export interface DraftRequest {
  practice: string;
  city: string;
  lawyerLastName: string | null;
  firmName: string | null;
  facts: Fact[];
  visibility: { allowed: boolean; validRuns: number; date: string; modeFragment: string; exampleQuery: string; sentence: string | null };
  /** Défauts d'ensemble du brouillon précédent (longueur, objet, information absente), pour une nouvelle rédaction. */
  feedback?: string[];
  keywords: string[];
  /** Résultat relevé par requête : true cité, false non cité ; absent = non vérifié. */
  keywordChecks: Record<string, boolean>;
  keywordCheckWho: string;
  keywordCount: number;
  auditUrl: string | null;
  auditPages: number | null;
  auditFactId: string | null;
  contactSourceUrl: string | null;
}

export interface Analyst {
  name: string;
  model: string;
  promptVersion: string;
  estimate(kind: "profile" | "keywords" | "draft" | "rewrite"): CallEstimate;
  extractProfile(req: ProfileRequest): Promise<{ profile: SiteProfile; usage: Usage }>;
  proposeKeywords(req: KeywordRequest): Promise<{ candidates: KeywordCandidate[]; usage: Usage }>;
  draftEmail(req: DraftRequest): Promise<{ subject: string; sentences: DraftSentence[]; usage: Usage }>;
  /** Réécrit uniquement les phrases refusées. `null` supprime la phrase. */
  rewriteSentences(req: DraftRequest, failed: { sentence: DraftSentence; check: SentenceCheck }[]): Promise<{ rewrites: { id: string; text: string | null; evidence_ids: string[] }[]; usage: Usage }>;
}

export interface Providers {
  search: SearchProvider;
  visibility: VisibilityProvider;
  analyst: Analyst;
}
