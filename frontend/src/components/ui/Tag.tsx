export type TagColor = "blue" | "red" | "green" | "orange" | "purple";
export type TagSize = "sm" | "md";

// Text renders in the solid accent color; background is the same color at low
// opacity so it reads as a tinted bubble rather than a solid-filled one.
const TAG_STYLES: Record<TagColor, string> = {
  blue: "text-accent-blue bg-accent-blue/10",
  red: "text-accent-red bg-accent-red/10",
  green: "text-accent-green bg-accent-green/10",
  orange: "text-accent-orange bg-accent-orange/10",
  purple: "text-accent-purple bg-accent-purple/10",
};

const SIZE_STYLES: Record<TagSize, { tag: string; icon: string; iconPx: number }> = {
  sm: { tag: "gap-2.5 px-5 py-2.5 text-sm", icon: "h-7 w-7", iconPx: 28 },
  md: { tag: "gap-3 px-6 py-3 text-base", icon: "h-8 w-8", iconPx: 32 },
};

interface TagProps {
  color: TagColor;
  text: string;
  iconKey?: string;
  size?: TagSize;
}

export default function Tag({ color, text, iconKey, size = "sm" }: TagProps) {
  const sizeStyles = SIZE_STYLES[size];

  return (
    <span
      className={`font-mono inline-flex items-center rounded-full font-medium ${sizeStyles.tag} ${TAG_STYLES[color]}`}
    >
      {iconKey && (
        <img
          src={`/icons/${iconKey}.png`}
          alt=""
          width={sizeStyles.iconPx}
          height={sizeStyles.iconPx}
          className={`${sizeStyles.icon} rounded-full object-contain`}
        />
      )}
      {text}
    </span>
  );
}
