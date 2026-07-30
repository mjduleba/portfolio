import type { UserProfile } from "@/lib/api/profile";
import Card from "@/components/ui/Card";
import Tag from "@/components/ui/Tag";

interface AboutProps {
  profile: UserProfile;
}

export default function About({ profile }: AboutProps) {
  // Split bio into paragraphs
  const bioParagraphs = profile.bio
    .split(/\r?\n\r?\n/)
    .map((paragraph) => paragraph.trim())
    .filter(Boolean);

  return (
    <section id="about" className="scroll-mt-24 px-8 py-24 sm:px-12">
      <div className="mx-auto max-w-3xl">
        <Card className="p-8 sm:p-10">
          <h2 className="font-title text-3xl font-semibold tracking-tight text-foreground">
            About
          </h2>

          <div className="mt-4 flex flex-wrap gap-2">
            <Tag color="blue" text={profile.title} />
            <Tag color="green" text={profile.location} />
          </div>

          <div className="my-6 border-t border-black/[.08] dark:border-white/[.145]" />

          <div className="space-y-4">
            {bioParagraphs.map((paragraph, index) => (
              <p key={index} className="font-mono text-base leading-7 text-foreground/90">
                {paragraph}
              </p>
            ))}
          </div>
        </Card>
      </div>
    </section>
  );
}
