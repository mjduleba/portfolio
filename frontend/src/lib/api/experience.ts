import { apiFetch } from "@/lib/api/client";

export interface Experience {
  id: number;
  role: string;
  company: string;
  location: string;
  start_date: string;
  end_date: string | null;
  bullets: string[];
}

export async function getExperience(): Promise<Experience[]> {
  return apiFetch<Experience[]>("/api/experience/");
}
