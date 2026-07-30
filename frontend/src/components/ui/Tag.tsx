export type TagColor = "blue" | "red" | "green" | "orange" | "purple";

// Text renders in the solid accent color; background is the same color at low
// opacity so it reads as a tinted bubble rather than a solid-filled one.
const TAG_STYLES: Record<TagColor, string> = {
  blue: "text-accent-blue bg-accent-blue/15",
  red: "text-accent-red bg-accent-red/15",
  green: "text-accent-green bg-accent-green/15",
  orange: "text-accent-orange bg-accent-orange/15",
  purple: "text-accent-purple bg-accent-purple/15",
};

interface TagProps {
  color: TagColor;
  text: string;
}

export default function Tag({ color, text }: TagProps) {
  return (
    <span
      className={`font-mono inline-flex items-center rounded-full px-3 py-1 text-sm font-medium ${TAG_STYLES[color]}`}
    >
      {text}
    </span>
  );
}
