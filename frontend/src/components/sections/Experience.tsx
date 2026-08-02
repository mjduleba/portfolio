import type { Experience as ExperienceEntry } from "@/lib/api/experience";
import type { Skill } from "@/lib/api/skills";
import Card from "@/components/ui/Card";
import Tag from "@/components/ui/Tag";
import TaggedText from "@/components/ui/TaggedText";

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
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div className="flex flex-col items-start gap-2">
                  <h3 className="font-title text-2xl font-semibold text-foreground">{job.role}</h3>
                  <Tag
                    color="green"
                    text={`${formatDate(job.start_date)} – ${job.end_date ? formatDate(job.end_date) : "Present"}`}
                  />
                </div>
                <div className="flex flex-col items-end gap-2">
                  <div className="flex items-center gap-3">
                    <img
                      src={`/icons/${job.company_icon_key}.jpeg`}
                      alt=""
                      width={32}
                      height={32}
                      className="h-8 w-8 shrink-0 rounded-full object-contain"
                    />
                    <p className="font-mono text-lg text-foreground/70">{job.company}</p>
                  </div>
                  <Tag color="green" text={job.location} />
                </div>
              </div>

              <div className="my-6 border-t border-black/[.08] dark:border-white/[.145]" />

              <ul className="list-disc space-y-2 pl-5">
                {job.bullets.map((bullet, index) => (
                  <li key={index} className="font-mono text-base leading-7 text-foreground/90">
                    <TaggedText text={bullet.text} tags={bullet.tags} skills={skills} />
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
