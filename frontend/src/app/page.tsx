import About from "@/components/sections/About";
import Skills from "@/components/sections/Skills";
import { getProfile } from "@/lib/api/profile";
import { getSkills } from "@/lib/api/skills";

export default async function Home() {
  const [profile, skills] = await Promise.all([getProfile(), getSkills()]);

  return (
    <main className="flex flex-1 flex-col">
      <section id="intro" />
      <About profile={profile} />
      <div className="mx-auto w-full max-w-6xl px-8 sm:px-12">
        <div className="border-t border-black/[.08] dark:border-white/[.145]" />
      </div>
      <Skills skills={skills} />
    </main>
  );
}
