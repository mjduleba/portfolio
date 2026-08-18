import About from "@/components/sections/About";
import Tools from "@/components/sections/Tools";
import Skills from "@/components/sections/Skills";
import Experience from "@/components/sections/Experience";
import Projects from "@/components/sections/Projects";
import { getProfile } from "@/lib/api/profile";
import { getSkills } from "@/lib/api/skills";
import { getExperience } from "@/lib/api/experience";
import { getProjects } from "@/lib/api/projects";
import { getTools } from "@/lib/api/tools";

// The backend isn't reachable at build time (e.g. inside an isolated Docker
// build), so this route can't be statically prerendered. Rendering on first
// request instead; the underlying fetches still cache via `revalidate: 60`.
export const dynamic = "force-dynamic";

export default async function Home() {
  const [profile, skills, experience, projects, tools] = await Promise.all([
    getProfile(),
    getSkills(),
    getExperience(),
    getProjects(),
    getTools(),
  ]);

  return (
    <main className="flex flex-1 flex-col">
      <section id="intro" />
      <About profile={profile} />
      <div className="mx-auto w-full max-w-6xl px-8 sm:px-12">
        <div className="border-t border-black/[.08] dark:border-white/[.145]" />
      </div>
      <Tools tools={tools} />
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
