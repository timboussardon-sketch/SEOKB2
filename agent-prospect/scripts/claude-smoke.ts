// Vérifie l'intégration Claude avec trois appels réels (facturés) : accès au modèle, une question de mesure, une extraction structurée.
import Anthropic from "@anthropic-ai/sdk";
import { assessRun } from "../src/core/verdict";
import { loadPriceTable, priceOf } from "../src/engine/pricing";
import { claudeProviders } from "../src/providers/claude";

const prices = loadPriceTable(process.env.PRICING_JSON);
const p = claudeProviders(process.env);
const model = await new Anthropic().models.retrieve(p.visibility.model);
console.log("modèle accessible :", model.id);

const a = await p.visibility.ask("Quels cabinets d'avocats accompagnent les entreprises en droit du travail à Lyon ?", "Lyon");
console.log("mesure :", a.text.length, "caractères ;", a.citations.length, "citations ; recherche web utilisée :", a.webSearchUsed, "; validité :", assessRun({ text: a.text, webSearchUsed: a.webSearchUsed, requireWebSearch: true }).validity);
console.log("usage :", a.usage.model, a.usage.input_tokens, "in", a.usage.output_tokens, "out", a.usage.web_search_calls, "recherches →", priceOf(prices, a.usage).toFixed(4), "$ (majorant réservé :", priceOf(prices, p.visibility.estimate()).toFixed(4), "$)");
console.log(a.text.slice(0, 400).replace(/\n+/g, " "));

const k = await p.analyst.proposeKeywords({ services: [{ evidenceId: "s1", label: "Contentieux prud'homal employeur", url: "https://exemple-fictif.test/prudhommes" }], city: "Lyon", clientTypes: ["entreprise"], count: 6, round: 1, alreadyKept: [] });
console.log("mots-clés :", k.candidates.length, "candidats →", priceOf(prices, k.usage).toFixed(4), "$ ;", k.candidates.slice(0, 3).map((c) => c.keyword).join(" | "));
