import { apiFetch } from "@/lib/api/client";

// Mirrors backend/tools/models.py's TextChoices — must be kept in sync manually, no codegen.
export type ToolCategory = "Demo" | "Tool";

export interface Tool {
  id: number;
  title: string;
  slug: string;
  category: ToolCategory;
  description: string;
  url: string;
  order: number;
  created_at: string;
}

export async function getTools(): Promise<Tool[]> {
  return apiFetch<Tool[]>("/api/tools/");
}
