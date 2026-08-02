"use client";

import { useEffect, useRef } from "react";
import { useInView } from "@/lib/hooks/useInView";
import RestartIcon from "@/components/ui/RestartIcon";

interface ProjectMediaProps {
  videoUrl: string;
  imageUrl: string;
  title: string;
}

export default function ProjectMedia({ videoUrl, imageUrl, title }: ProjectMediaProps) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const { ref: containerRef, isInView } = useInView<HTMLDivElement>(0.5);

  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;
    if (isInView) {
      video.currentTime = 0;
      void video.play().catch(() => {
        // Autoplay can still be rejected by some browser/OS combinations even
        // when muted; the restart button remains available as a fallback.
      });
    } else {
      video.pause();
      video.currentTime = 0; // reset so the next scroll-into-view replays from the start
    }
  }, [isInView]);

  function handleRestart() {
    const video = videoRef.current;
    if (!video) return;
    video.currentTime = 0;
    void video.play().catch(() => {});
  }

  if (!videoUrl && !imageUrl) return null;

  return (
    <div
      ref={containerRef}
      className="relative aspect-video w-full overflow-hidden rounded-2xl border border-black/[.08] sm:aspect-auto sm:h-full dark:border-white/[.145]"
    >
      {videoUrl ? (
        <>
          <video
            ref={videoRef}
            src={videoUrl}
            muted
            playsInline
            preload="metadata"
            aria-label={`${title} demo video`}
            className="h-full w-full object-cover"
          />
          <button
            type="button"
            onClick={handleRestart}
            aria-label="Restart video"
            className="absolute bottom-3 right-3 flex h-9 w-9 items-center justify-center rounded-full bg-background/80 text-foreground/70 transition-all duration-200 hover:bg-foreground/10 hover:text-foreground"
          >
            <RestartIcon className="h-5 w-5" />
          </button>
        </>
      ) : (
        <img src={imageUrl} alt="" className="h-full w-full object-cover" />
      )}
    </div>
  );
}
