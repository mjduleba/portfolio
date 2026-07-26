import Link from "next/link";

export default function Header() {
  return (
    <header className="border-b border-black/[.08] dark:border-white/[.145]">
      <div className="mx-auto flex max-w-3xl items-center justify-between px-16 py-6">
        <Link href="/" className="text-lg font-semibold text-foreground">
          Michael Duleba
        </Link>
        <nav>
          <Link href="/" className="text-sm font-medium text-foreground">
            Home
          </Link>
        </nav>
      </div>
    </header>
  );
}
