import { notFound } from "next/navigation";
import { getToolBySlug } from "@/lib/api/tools";
import Tag from "@/components/ui/Tag";
import { getToolColor } from "@/lib/toolColors";
import ProjectMedia from "@/components/sections/ProjectMedia";

interface ToolDetailPageProps {
  params: Promise<{ slug: string }>;
}

export default async function ToolDetailPage({ params }: ToolDetailPageProps) {
  const { slug } = await params;
  const tool = await getToolBySlug(slug).catch(() => null);

  if (!tool) {
    notFound();
  }

  return (
    <main className="flex flex-1 flex-col px-8 py-16 sm:px-12">
      <div className="mx-auto w-full max-w-3xl">
        <div className="flex flex-wrap items-baseline gap-3">
          <Tag color={getToolColor(tool.category)} text={tool.category} size="sm" />
          <h1 className="font-title text-3xl font-semibold tracking-tight text-foreground">
            {tool.title}
          </h1>
        </div>
        <p className="mt-4 whitespace-pre-line font-mono text-base leading-7 text-foreground/90">
          {tool.description}
        </p>

        <div className="my-8 border-t border-black/[.08] dark:border-white/[.145]" />

        {tool.skill_agent_entries.length > 0 ? (
          <div className="space-y-10">
            {tool.skill_agent_entries.map((entry, index) => {
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
        ) : (
          <p className="font-mono text-sm text-foreground/60">Entries coming soon.</p>
        )}
      </div>
    </main>
  );
}
