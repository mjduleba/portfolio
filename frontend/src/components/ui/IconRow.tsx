interface IconRowProps {
  iconKey: string;
  label: string;
}

export default function IconRow({ iconKey, label }: IconRowProps) {
  return (
    <div className="font-mono flex w-full items-center gap-3 text-base font-medium text-foreground/80">
      <img
        src={`/icons/${iconKey}.png`}
        alt=""
        width={24}
        height={24}
        className="h-6 w-6 shrink-0 rounded-full object-contain"
      />
      <span className="min-w-0 flex-1 truncate text-left">{label}</span>
    </div>
  );
}
