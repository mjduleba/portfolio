import { apiFetch } from "@/lib/api/client";

// Mirrors backend/skills/models.py's TextChoices — must be kept in sync manually, no codegen.
export type SkillCategory =
  | "Languages & Querying"
  | "Frameworks, Libraries & Tools"
  | "Cloud & Infrastructure"
  | "Technical Concepts";

export interface Skill {
  id: number;
  name: string;
  category: SkillCategory;
  order: number;
  icon_key: string;
}

export async function getSkills(): Promise<Skill[]> {
  return apiFetch<Skill[]>("/api/skills/");
}
