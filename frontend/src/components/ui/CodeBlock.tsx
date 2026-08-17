interface CodeBlockProps {
  code: string;
  language?: string;
}

export default function CodeBlock({ code, language }: CodeBlockProps) {
  return (
    <div className="overflow-x-auto rounded-2xl border border-black/[.08] bg-foreground/5 dark:border-white/[.145]">
      {language && (
        <div className="border-b border-black/[.08] px-4 py-2 font-mono text-xs uppercase tracking-wide text-foreground/50 dark:border-white/[.145]">
          {language}
        </div>
      )}
      <pre className="p-4 text-sm leading-6">
        <code className="font-mono text-foreground/90">{code}</code>
      </pre>
    </div>
  );
}
