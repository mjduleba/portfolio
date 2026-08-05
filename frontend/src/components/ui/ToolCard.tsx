import Link from "next/link";
import Card from "@/components/ui/Card";
import Tag from "@/components/ui/Tag";
import type { Tool } from "@/lib/api/tools";
import { getToolColor } from "@/lib/toolColors";

interface ToolCardProps {
  tool: Tool;
}

export default function ToolCard({ tool }: ToolCardProps) {
  const content = (
    <Card className="flex aspect-square flex-col p-8 transition-colors duration-200 hover:bg-foreground/10">
      <div className="flex flex-wrap items-baseline gap-3">
        <Tag color={getToolColor(tool.category)} text={tool.category} size="sm" />
        <h3 className="font-title text-xl font-semibold text-foreground">{tool.title}</h3>
      </div>
      <div className="my-5 border-t border-black/[.08] dark:border-white/[.145]" />
      <p className="line-clamp-8 whitespace-pre-line font-mono text-sm leading-6 text-foreground/80">
        {tool.description}
      </p>
    </Card>
  );

  if (tool.url) {
    return (
      <a href={tool.url} target="_blank" rel="noopener noreferrer">
        {content}
      </a>
    );
  }

  return <Link href={`/tools/${tool.slug}`}>{content}</Link>;
}
