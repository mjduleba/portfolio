import About from "@/components/sections/About";
import Skills from "@/components/sections/Skills";
import Experience from "@/components/sections/Experience";
import Projects from "@/components/sections/Projects";
import { getProfile } from "@/lib/api/profile";
import { getSkills } from "@/lib/api/skills";
import { getExperience } from "@/lib/api/experience";
import { getProjects } from "@/lib/api/projects";

export default async function Home() {
  const [profile, skills, experience, projects] = await Promise.all([
    getProfile(),
    getSkills(),
    getExperience(),
    getProjects(),
  ]);

  return (
    <main className="flex flex-1 flex-col">
      <section id="intro" />
      <About profile={profile} />
      <div className="mx-auto w-full max-w-6xl px-8 sm:px-12">
        <div className="border-t border-black/[.08] dark:border-white/[.145]" />
      </div>
      <Skills skills={skills} />
      <div className="mx-auto w-full max-w-6xl px-8 sm:px-12">
        <div className="border-t border-black/[.08] dark:border-white/[.145]" />
      </div>
      <Experience experience={experience} skills={skills} />
      <div className="mx-auto w-full max-w-6xl px-8 sm:px-12">
        <div className="border-t border-black/[.08] dark:border-white/[.145]" />
      </div>
      <Projects projects={projects} skills={skills} />
    </main>
  );
}
