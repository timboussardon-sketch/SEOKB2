export function Tag({ pair }: { pair?: [string, string] }) {
  if (!pair) return null;
  return <span className={`tag ${pair[1]}`}>{pair[0]}</span>;
}

export function SimBanner({ simulation }: { simulation: boolean }) {
  if (!simulation) return null;
  return <div className="banner">Simulation : cabinets, sites et réponses IA fictifs. Aucun appel externe, aucune donnée réelle.</div>;
}

export const usd = (n: number) => `${n.toFixed(n < 1 && n > 0 ? 4 : 2)} $`;
