"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";

/** Rafraîchit les données de la page tant qu'un traitement est en cours. */
export function AutoRefresh({ active, seconds = 3 }: { active: boolean; seconds?: number }) {
  const router = useRouter();
  useEffect(() => {
    if (!active) return;
    const id = setInterval(() => router.refresh(), seconds * 1000);
    return () => clearInterval(id);
  }, [active, seconds, router]);
  return null;
}
