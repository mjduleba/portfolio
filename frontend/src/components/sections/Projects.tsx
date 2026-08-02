import type { Project } from "@/lib/api/projects";
import type { Skill } from "@/lib/api/skills";
import ProjectItem from "@/components/sections/ProjectItem";

interface ProjectsProps {
  projects: Project[];
  skills: Skill[];
}

export default function Projects({ projects, skills }: ProjectsProps) {
  return (
    <section id="projects" className="px-8 py-16 sm:px-12">
      <div className="mx-auto max-w-6xl">
        <h2 className="font-title text-3xl font-semibold tracking-tight text-foreground">
          Projects
        </h2>
        <div className="mt-6 flex flex-col gap-12">
          {projects.map((project, index) => (
            <ProjectItem
              key={project.id}
              project={project}
              skills={skills}
              reverse={index % 2 === 1}
            />
          ))}
        </div>
      </div>
    </section>
  );
}
