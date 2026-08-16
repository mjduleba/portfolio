"use client";

import { useState } from "react";
import type { GuidePattern } from "@/lib/api/tools";
import Card from "@/components/ui/Card";
import Modal from "@/components/ui/Modal";
import SectionHeading from "@/components/ui/SectionHeading";
import CodeBlock from "@/components/ui/CodeBlock";

interface GuideContentProps {
  patterns: GuidePattern[];
}

export default function GuideContent({ patterns }: GuideContentProps) {
  const [selected, setSelected] = useState<GuidePattern | null>(null);

  return (
    <div>
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {patterns.map((pattern) => (
          <Card
            key={pattern.name}
            className="flex cursor-pointer flex-col p-6 transition-colors duration-200 hover:bg-foreground/10"
            onClick={() => setSelected(pattern)}
          >
            <h3 className="font-title text-lg font-semibold text-foreground">{pattern.name}</h3>
            <p className="mt-2 line-clamp-3 font-mono text-sm leading-6 text-foreground/80">
              {pattern.how_it_works}
            </p>
          </Card>
        ))}
      </div>

      <Modal open={selected !== null} onClose={() => setSelected(null)}>
        {selected && (
          <>
            <h2 className="font-title pr-10 text-xl font-semibold text-foreground">
              {selected.name}
            </h2>
            <p className="mt-2 whitespace-pre-line font-mono text-base leading-7 text-foreground/90">
              {selected.how_it_works}
            </p>

            {selected.diagram_svg && (
              <div
                className="mt-6 flex justify-center rounded-2xl border border-black/[.08] bg-foreground/5 p-4 dark:border-white/[.145] [&_svg]:h-auto [&_svg]:max-w-full"
                dangerouslySetInnerHTML={{ __html: selected.diagram_svg }}
              />
            )}

            <div className="mt-6">
              <SectionHeading title="How to Recognize It" />
              <ul className="mt-3 list-disc space-y-1 pl-5 font-mono text-sm leading-6 text-foreground/80">
                {selected.recognition_signals.map((signal, i) => (
                  <li key={i}>{signal}</li>
                ))}
              </ul>
            </div>

            <div className="mt-6">
              <SectionHeading title="Code" />
              <div className="mt-3">
                <CodeBlock code={selected.code_solution} language={selected.code_language} />
              </div>
            </div>

            <div className="mt-6">
              <SectionHeading title="Example Problems" />
              <ul className="mt-3 list-disc space-y-1 pl-5 font-mono text-sm leading-6 text-foreground/80">
                {selected.example_problems.map((ex) => (
                  <li key={ex.title}>
                    {ex.url ? (
                      <a
                        href={ex.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-foreground underline decoration-foreground/30 underline-offset-2 hover:decoration-foreground"
                      >
                        {ex.title}
                      </a>
                    ) : (
                      <span className="text-foreground">{ex.title}</span>
                    )}{" "}
                    — {ex.description}
                  </li>
                ))}
              </ul>
            </div>
          </>
        )}
      </Modal>
    </div>
  );
}
