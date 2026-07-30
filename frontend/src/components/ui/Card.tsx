interface CardProps {
  children: React.ReactNode;
  className?: string;
}

export default function Card({ children, className = "" }: CardProps) {
  return (
    <div
      className={`rounded-2xl border border-black/[.08] bg-foreground/5 dark:border-white/[.145] ${className}`}
    >
      {children}
    </div>
  );
}
