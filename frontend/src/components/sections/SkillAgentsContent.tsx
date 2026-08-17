import type { SkillAgentEntry } from "@/lib/api/tools";
import Tag from "@/components/ui/Tag";
import ProjectMedia from "@/components/sections/ProjectMedia";

interface SkillAgentsContentProps {
  entries: SkillAgentEntry[];
}

export default function SkillAgentsContent({ entries }: SkillAgentsContentProps) {
  return (
    <div className="space-y-10">
      {entries.map((entry, index) => {
        const hasMedia = Boolean(entry.video_url || entry.image_url);
        return (
          <div
            key={index}
            className={hasMedia ? "grid grid-cols-1 gap-6 sm:grid-cols-2 sm:items-start" : ""}
          >
            {hasMedia && (
              <div className="sm:h-56">
                <ProjectMedia
                  videoUrl={entry.video_url}
                  imageUrl={entry.image_url}
                  title={entry.name}
                />
              </div>
            )}
            <div>
              <div className="flex flex-wrap items-baseline gap-3">
                <h2 className="font-title text-xl font-semibold text-foreground">
                  {entry.name}
                </h2>
                <Tag color={entry.kind === "Agent" ? "orange" : "purple"} text={entry.kind} size="sm" />
              </div>
              <p className="mt-2 whitespace-pre-line font-mono text-base leading-7 text-foreground/90">
                {entry.description}
              </p>
              {entry.tags.length > 0 && (
                <div className="mt-3 flex flex-wrap gap-2">
                  {entry.tags.map((tag) => (
                    <Tag key={tag} color="green" text={tag} size="sm" />
                  ))}
                </div>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
}
