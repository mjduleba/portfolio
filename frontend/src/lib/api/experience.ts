import { apiFetch } from "@/lib/api/client";

export interface ExperienceBullet {
  text: string;
  tags: string[];
}

export interface Experience {
  id: number;
  role: string;
  company: string;
  company_icon_key: string;
  location: string;
  start_date: string;
  end_date: string | null;
  bullets: ExperienceBullet[];
}

export async function getExperience(): Promise<Experience[]> {
  return apiFetch<Experience[]>("/api/experience/");
}
