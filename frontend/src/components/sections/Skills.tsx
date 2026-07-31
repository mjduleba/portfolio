import type { Skill, SkillCategory } from "@/lib/api/skills";
import type { TagColor } from "@/components/ui/Tag";
import Card from "@/components/ui/Card";
import Tag from "@/components/ui/Tag";

interface SkillsProps {
  skills: Skill[];
}

const CATEGORY_ORDER: SkillCategory[] = [
  "Languages & Querying",
  "Frameworks, Libraries & Tools",
  "Cloud & Infrastructure",
  "Technical Concepts",
];

const CATEGORY_COLORS: Record<SkillCategory, TagColor> = {
  "Languages & Querying": "blue",
  "Frameworks, Libraries & Tools": "purple",
  "Cloud & Infrastructure": "orange",
  "Technical Concepts": "red",
};

export default function Skills({ skills }: SkillsProps) {
  const categories = CATEGORY_ORDER.map((category) => ({
    category,
    skills: skills
      .filter((skill) => skill.category === category)
      .sort((a, b) => a.order - b.order),
  })).filter((group) => group.skills.length > 0);

  return (
    <section id="skills" className="scroll-mt-24 px-8 py-24 sm:px-12">
      <Card className="mx-auto max-w-4xl p-8 sm:p-10">
        <h2 className="font-title text-3xl font-semibold tracking-tight text-foreground">Skills</h2>
        <div className="mt-6 space-y-6">
          {categories.map((group, index) => (
            <div
              key={group.category}
              className={
                index === 0
                  ? undefined
                  : "border-t border-black/[.08] pt-6 dark:border-white/[.145]"
              }
            >
              <h3 className="font-mono text-sm font-medium uppercase tracking-wide text-foreground/60">
                {group.category}
              </h3>
              <div className="mt-3 flex flex-wrap gap-2">
                {group.skills.map((skill) => (
                  <Tag
                    key={skill.id}
                    color={CATEGORY_COLORS[group.category]}
                    text={skill.name}
                    iconKey={skill.icon_key || undefined}
                  />
                ))}
              </div>
            </div>
          ))}
        </div>
      </Card>
    </section>
  );
}
