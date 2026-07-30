import type { UserProfile } from "@/lib/api/profile";
import Card from "@/components/ui/Card";
import Tag from "@/components/ui/Tag";

interface ContactCardProps {
  profile: UserProfile;
}

interface ProfileLink {
  label: string;
  href: string;
  iconKey: string;
  external?: boolean;
  download?: boolean;
}

function getProfileLinks(profile: UserProfile): ProfileLink[] {
  return [
    { label: "LinkedIn", href: profile.linkedin_url, iconKey: "linkedin", external: true },
    { label: "GitHub", href: profile.github_url, iconKey: "github", external: true },
    { label: "LeetCode", href: profile.leetcode_url, iconKey: "leetcode", external: true },
    { label: "Gmail", href: `mailto:${profile.email}`, iconKey: "gmail" },
    { label: "Resume", href: "/resume.pdf", iconKey: "resume", download: true },
  ];
}

export default function ContactCard({ profile }: ContactCardProps) {
  const links = getProfileLinks(profile);

  return (
    <Card className="flex flex-col items-center gap-4 p-8 text-center sm:w-72">
      <img
        src="/profile.png"
        alt={profile.name}
        width={128}
        height={128}
        className="h-32 w-32 rounded-full border-2 border-black/[.08] object-cover dark:border-white/[.145]"
      />

      <div>
        <h3 className="font-title text-xl font-semibold text-foreground">{profile.name}</h3>
        <div className="mt-2 flex justify-center">
          <Tag color="green" text={profile.location} />
        </div>
      </div>

      <div className="mt-2 flex w-full flex-col gap-2">
        {links.map((link) => (
          <a
            key={link.iconKey}
            href={link.href}
            {...(link.external ? { target: "_blank", rel: "noopener noreferrer" } : {})}
            {...(link.download ? { download: true } : {})}
            className="font-mono flex items-center justify-start gap-3 rounded-full border border-black/[.08] px-5 py-2.5 text-base font-medium text-foreground/80 transition-colors hover:bg-foreground/10 dark:border-white/[.145]"
          >
            <img src={`/icons/${link.iconKey}.png`} alt="" width={24} height={24} className="h-6 w-6" />
            {link.label}
          </a>
        ))}
      </div>
    </Card>
  );
}
