interface SectionHeadingProps {
  title: string;
}

export default function SectionHeading({ title }: SectionHeadingProps) {
  return (
    <div className="w-full border-t border-black/[.08] pt-3 dark:border-white/[.145]">
      <p className="font-mono text-lg font-semibold uppercase tracking-wide text-foreground/60">
        {title}
      </p>
    </div>
  );
}
