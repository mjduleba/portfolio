import type { Project } from "@/lib/api/projects";
import type { Skill } from "@/lib/api/skills";
import Card from "@/components/ui/Card";
import Tag from "@/components/ui/Tag";
import TaggedText from "@/components/ui/TaggedText";
import ProjectMedia from "@/components/sections/ProjectMedia";
import { getSkillColor } from "@/lib/skillColors";

interface ProjectItemProps {
  project: Project;
  skills: Skill[];
  reverse: boolean;
}

export default function ProjectItem({ project, skills, reverse }: ProjectItemProps) {
  const hasMedia = Boolean(project.video_url || project.image_url);

  return (
    <div
      className={
        hasMedia
          ? "grid grid-cols-1 gap-8 sm:grid-cols-2 sm:h-[420px]"
          : "flex flex-col"
      }
    >
      {hasMedia && (
        <div className={`sm:h-full ${reverse ? "sm:order-2" : "sm:order-1"}`}>
          <ProjectMedia
            videoUrl={project.video_url}
            imageUrl={project.image_url}
            title={project.title}
          />
        </div>
      )}

      <Card
        className={`flex min-h-0 flex-col ${
          hasMedia ? `sm:h-full ${reverse ? "sm:order-1" : "sm:order-2"}` : "w-full"
        }`}
      >
        <div
          className={`overflow-y-auto p-10 sm:p-12 ${
            hasMedia ? "max-h-[420px] sm:h-full sm:max-h-full" : ""
          }`}
        >
          <div className="flex flex-wrap items-baseline gap-3">
            <h3 className="font-title text-2xl font-semibold text-foreground">{project.title}</h3>
            {project.github_url && (
              <a
                href={project.github_url}
                target="_blank"
                rel="noopener noreferrer"
                className="font-mono inline-flex items-center gap-1.5 text-sm font-medium text-foreground/60 transition-colors hover:text-foreground"
              >
                <img
                  src="/icons/github.png"
                  alt=""
                  width={16}
                  height={16}
                  className="h-4 w-4 rounded-full object-contain"
                />
                GitHub
              </a>
            )}
          </div>

          {project.demo_url && (
            <div className="mt-3 flex flex-wrap gap-2">
              <Tag color="green" text="Demo" href={project.demo_url} />
            </div>
          )}

          <div className="mt-3 flex flex-wrap gap-2">
            {project.tech_stack.map((tech) => (
              <Tag key={tech} color={getSkillColor(skills, tech)} text={tech} size="sm" />
            ))}
          </div>

          <p className="mt-4 font-mono text-base leading-7 text-foreground/90">
            {project.description}
          </p>

          {project.bullets.length > 0 && (
            <>
              <div className="my-6 border-t border-black/[.08] dark:border-white/[.145]" />
              <h4 className="font-mono text-sm font-semibold uppercase tracking-wide text-foreground/60">
                Logic Breakdown
              </h4>
              <ul className="mt-3 list-disc space-y-2 pl-5">
                {project.bullets.map((bullet, index) => (
                  <li key={index} className="font-mono text-base leading-7 text-foreground/90">
                    <TaggedText text={bullet.text} tags={bullet.tags} skills={skills} />
                  </li>
                ))}
              </ul>
            </>
          )}
        </div>
      </Card>
    </div>
  );
}
