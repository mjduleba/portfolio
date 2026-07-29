import Link from "next/link";

// Navigation links for the header buttons
const NAV_LINKS = [
  { label: "About", href: "/about" },
  { label: "Skills", href: "/skills" },
  { label: "Experience", href: "/experience" },
  { label: "Projects", href: "/projects" },
  { label: "Tools", href: "/tools" },
];

export default function Header() {
    return (
      <header className="border-b border-black/[.08] dark:border-white/[.145]">
        <div className="flex w-full items-center justify-between px-8 py-6 sm:px-12">
          <Link href="/" className="font-title text-2xl font-semibold tracking-tight text-foreground">
            Michael Duleba
          </Link>
          <nav className="flex items-center gap-2">
            {NAV_LINKS.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                className="font-mono rounded-full px-4 py-2 text-base font-medium text-foreground/70 transition-all duration-200 hover:bg-foreground/10 hover:text-foreground"
              >
                {link.label}
              </Link>
            ))}
          </nav>
        </div>
      </header>
    );
}

