import { apiFetch } from "@/lib/api/client";

export interface Project {
  id: number;
  title: string;
  description: string;
  tech_stack: string[];
  github_url: string;
  demo_url: string | null;
  featured: boolean;
  order: number;
  created_at: string;
}

export async function getProjects(): Promise<Project[]> {
  return apiFetch<Project[]>("/api/projects/");
}
