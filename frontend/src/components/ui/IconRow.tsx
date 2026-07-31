interface IconRowProps {
  iconKey: string;
  label: string;
}

export default function IconRow({ iconKey, label }: IconRowProps) {
  return (
    <div className="font-mono flex w-full items-center gap-3 text-lg font-medium text-foreground/80">
      <img
        src={`/icons/${iconKey}.png`}
        alt=""
        width={32}
        height={32}
        className="h-8 w-8 shrink-0 rounded-full object-contain"
      />
      <span className="min-w-0 flex-1 truncate text-left">{label}</span>
    </div>
  );
}
