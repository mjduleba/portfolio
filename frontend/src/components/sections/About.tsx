import type { UserProfile } from "@/lib/api/profile";
import Card from "@/components/ui/Card";
import ContactCard from "@/components/sections/ContactCard";
import Tag from "@/components/ui/Tag";
import SectionHeading from "@/components/ui/SectionHeading";
import IconRow from "@/components/ui/IconRow";

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
    <section id="about" className="scroll-mt-24 px-8 py-16 sm:px-12">
      <div className="mx-auto flex max-w-6xl flex-col gap-6 sm:flex-row sm:items-stretch">
        <ContactCard profile={profile} />

        <Card className="p-10 sm:flex-1 sm:p-12">
          <h2 className="font-title text-3xl font-semibold tracking-tight text-foreground">
            About
          </h2>

          <div className="my-6 border-t border-black/[.08] dark:border-white/[.145]" />

          <div className="space-y-4">
            {bioParagraphs.map((paragraph, index) => (
              <p key={index} className="font-mono text-base leading-7 text-foreground/90">
                {paragraph}
              </p>
            ))}
          </div>

          {profile.education.length > 0 && (
            <div className="mt-6 w-full">
              <SectionHeading title="Education" />
              <div className="mt-3 flex w-full flex-col gap-2">
                {profile.education.map((edu, index) => (
                  <div key={index} className="flex flex-col gap-2">
                    <IconRow iconKey={edu.institution_icon_key} label={edu.institution} />
                    <IconRow iconKey={edu.degree_icon_key} label={edu.degree} />
                  </div>
                ))}
              </div>
            </div>
          )}
        </Card>
      </div>
    </section>
  );
}
