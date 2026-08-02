import type { Skill } from "@/lib/api/skills";
import Tag from "@/components/ui/Tag";
import { getSkillColor } from "@/lib/skillColors";

interface TaggedTextProps {
  text: string;
  tags: string[];
  skills: Skill[];
}

export default function TaggedText({ text, tags, skills }: TaggedTextProps) {
  if (tags.length === 0) return <>{text}</>;

  const matches = tags
    .map((tag) => ({ tag, index: text.indexOf(tag) }))
    .filter((m) => m.index !== -1)
    .sort((a, b) => a.index - b.index);

  const nodes: React.ReactNode[] = [];
  let cursor = 0;
  for (const { tag, index } of matches) {
    if (index < cursor) continue; // already consumed by an earlier, overlapping match
    if (index > cursor) nodes.push(text.slice(cursor, index));
    nodes.push(<Tag key={tag} color={getSkillColor(skills, tag)} text={tag} size="sm" />);
    cursor = index + tag.length;
  }
  if (cursor < text.length) nodes.push(text.slice(cursor));
  return <>{nodes}</>;
}
