import { apiFetch } from "@/lib/api/client";

export interface ProjectBullet {
  text: string;
  tags: string[];
}

export interface Project {
  id: number;
  title: string;
  description: string;
  tech_stack: string[];
  github_url: string;
  demo_url: string | null;
  video_url: string;
  image_url: string;
  featured: boolean;
  order: number;
  created_at: string;
  bullets: ProjectBullet[];
}

export async function getProjects(): Promise<Project[]> {
  return apiFetch<Project[]>("/api/projects/");
}
