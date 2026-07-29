import About from "@/components/sections/About";
import { getProfile } from "@/lib/api/profile";

export default async function Home() {
  const profile = await getProfile();

  return (
    <main className="flex flex-1 flex-col">
      <section id="intro" />
      <About profile={profile} />
    </main>
  );
}
