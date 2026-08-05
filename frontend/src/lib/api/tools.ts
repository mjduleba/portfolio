import { apiFetch } from "@/lib/api/client";

// Mirrors backend/tools/models.py's TextChoices — must be kept in sync manually, no codegen.
export type ToolCategory = "Demo" | "Tool";

// Content specific to the Skills & Agents Showcase tool. Other future tools may
// need entirely different content shapes and their own dedicated models — see
// the portfolio roadmap notes on why the shared Tool model stays metadata-only.
export type SkillAgentKind = "Skill" | "Agent";

export interface SkillAgentEntry {
  name: string;
  kind: SkillAgentKind;
  description: string;
  tags: string[];
  video_url: string;
  image_url: string;
}

export interface Tool {
  id: number;
  title: string;
  slug: string;
  category: ToolCategory;
  description: string;
  url: string;
  order: number;
  created_at: string;
  skill_agent_entries: SkillAgentEntry[];
}

export async function getTools(): Promise<Tool[]> {
  return apiFetch<Tool[]>("/api/tools/");
}

export async function getToolBySlug(slug: string): Promise<Tool> {
  return apiFetch<Tool>(`/api/tools/${slug}/`);
}
