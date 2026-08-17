import { notFound } from "next/navigation";
import { getToolBySlug } from "@/lib/api/tools";
import Tag from "@/components/ui/Tag";
import { getToolColor } from "@/lib/toolColors";
import SkillAgentsContent from "@/components/sections/SkillAgentsContent";
import GuideContent from "@/components/sections/GuideContent";

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
      </div>

      {tool.guide_patterns.length > 0 ? (
        <div className="mx-auto w-full max-w-6xl">
          <GuideContent patterns={tool.guide_patterns} />
        </div>
      ) : tool.skill_agent_entries.length > 0 ? (
        <div className="mx-auto w-full max-w-3xl">
          <SkillAgentsContent entries={tool.skill_agent_entries} />
        </div>
      ) : (
        <div className="mx-auto w-full max-w-3xl">
          <p className="font-mono text-sm text-foreground/60">Entries coming soon.</p>
        </div>
      )}
    </main>
  );
}
