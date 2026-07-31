export type TagColor = "blue" | "red" | "green" | "orange" | "purple";

// Text renders in the solid accent color; background is the same color at low
// opacity so it reads as a tinted bubble rather than a solid-filled one.
const TAG_STYLES: Record<TagColor, string> = {
  blue: "text-accent-blue bg-accent-blue/10",
  red: "text-accent-red bg-accent-red/10",
  green: "text-accent-green bg-accent-green/10",
  orange: "text-accent-orange bg-accent-orange/10",
  purple: "text-accent-purple bg-accent-purple/10",
};

interface TagProps {
  color: TagColor;
  text: string;
  iconKey?: string;
}

export default function Tag({ color, text, iconKey }: TagProps) {
  return (
    <span
      className={`font-mono inline-flex items-center gap-2.5 rounded-full px-5 py-2.5 text-sm font-medium ${TAG_STYLES[color]}`}
    >
      {iconKey && (
        <img
          src={`/icons/${iconKey}.png`}
          alt=""
          width={28}
          height={28}
          className="h-7 w-7 rounded-full object-contain"
        />
      )}
      {text}
    </span>
  );
}
