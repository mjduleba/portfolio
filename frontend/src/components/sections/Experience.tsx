import type { Experience as ExperienceEntry } from "@/lib/api/experience";
import type { Skill } from "@/lib/api/skills";
import Card from "@/components/ui/Card";
import Tag from "@/components/ui/Tag";
import { getSkillColor } from "@/lib/skillColors";

interface ExperienceProps {
  experience: ExperienceEntry[];
  skills: Skill[];
}

function formatDate(dateStr: string) {
  return new Date(dateStr).toLocaleDateString("en-US", {
    month: "short",
    year: "numeric",
    timeZone: "UTC", // dates are date-only strings; force UTC to avoid local-tz day rollover
  });
}

function renderBulletText(text: string, tags: string[], skills: Skill[]) {
  if (tags.length === 0) return text;

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
  return nodes;
}

export default function Experience({ experience, skills }: ExperienceProps) {
  return (
    <section id="experience" className="px-8 py-16 sm:px-12">
      <div className="mx-auto max-w-6xl">
        <h2 className="font-title text-3xl font-semibold tracking-tight text-foreground">
          Experience
        </h2>
        <div className="mt-6 flex flex-col gap-6">
          {experience.map((job) => (
            <Card key={job.id} className="p-10 sm:p-12">
              <div className="flex flex-wrap items-baseline justify-between gap-3">
                <div>
                  <h3 className="font-title text-xl font-semibold text-foreground">{job.role}</h3>
                  <p className="font-mono text-base text-foreground/70">{job.company}</p>
                </div>
                <div className="flex flex-wrap gap-2">
                  <Tag
                    color="blue"
                    text={`${formatDate(job.start_date)} – ${job.end_date ? formatDate(job.end_date) : "Present"}`}
                  />
                  <Tag color="green" text={job.location} />
                </div>
              </div>

              <div className="my-6 border-t border-black/[.08] dark:border-white/[.145]" />

              <ul className="list-disc space-y-2 pl-5">
                {job.bullets.map((bullet, index) => (
                  <li key={index} className="font-mono text-base leading-7 text-foreground/90">
                    {renderBulletText(bullet.text, bullet.tags, skills)}
                  </li>
                ))}
              </ul>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}
