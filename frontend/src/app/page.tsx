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
      <Skills skills={skills} />
    </main>
  );
}
