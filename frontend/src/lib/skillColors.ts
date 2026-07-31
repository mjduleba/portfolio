import type { Skill, SkillCategory } from "@/lib/api/skills";
import type { TagColor } from "@/components/ui/Tag";

export const CATEGORY_COLORS: Record<SkillCategory, TagColor> = {
  "Languages & Querying": "blue",
  "Frameworks, Libraries & Tools": "purple",
  "Cloud & Infrastructure": "orange",
  "Technical Concepts": "red",
};

// Falls back to "purple" for tags with no matching entry in the Skill catalog (e.g. "pytest").
export function getSkillColor(skills: Skill[], name: string, fallback: TagColor = "purple"): TagColor {
  const skill = skills.find((s) => s.name === name);
  return skill ? CATEGORY_COLORS[skill.category] : fallback;
}
