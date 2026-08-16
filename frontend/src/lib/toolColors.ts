import type { ToolCategory } from "@/lib/api/tools";
import type { TagColor } from "@/components/ui/Tag";

export const CATEGORY_COLORS: Record<ToolCategory, TagColor> = {
  Demo: "pink",
  Tool: "sky",
  Guide: "blue",
};

export function getToolColor(category: ToolCategory): TagColor {
  return CATEGORY_COLORS[category];
}
