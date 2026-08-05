import type { Tool } from "@/lib/api/tools";
import ToolCard from "@/components/ui/ToolCard";

interface ToolsProps {
  tools: Tool[];
}

export default function Tools({ tools }: ToolsProps) {
  return (
    <section id="tools" className="px-8 py-16 sm:px-12">
      <div className="mx-auto max-w-6xl">
        <h2 className="font-title text-3xl font-semibold tracking-tight text-foreground">
          Tools
        </h2>
        <div className="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {tools.map((tool) => (
            <ToolCard key={tool.id} tool={tool} />
          ))}
        </div>
      </div>
    </section>
  );
}
