"use client";

import { useRef, useState } from "react";

/** Prefer extensions you actually ship first (fewer 404s). Order matches Streamlit resolver. */
const CANDIDATES = [
  "/ProfilePic.jpeg",
  "/ProfilePic.jpg",
  "/ProfilePic.png",
  "/ProfilePic.webp",
] as const;

export function ProfilePhoto() {
  const [index, setIndex] = useState(0);
  /** Avoid advancing twice when `onError` fires more than once for the same src (e.g. Strict Mode). */
  const lastHandledErrorIndex = useRef<number | null>(null);

  if (index >= CANDIDATES.length) {
    return null;
  }

  const src = CANDIDATES[index];

  return (
    // eslint-disable-next-line @next/next/no-img-element -- multi-extension fallback without static imports
    <img
      key={src}
      src={src}
      alt="Chibuike Odibeli"
      width={112}
      height={112}
      className="h-28 w-28 shrink-0 rounded-full border border-[#E2E8F0] object-cover"
      onError={() => {
        if (lastHandledErrorIndex.current === index) {
          return;
        }
        lastHandledErrorIndex.current = index;
        setIndex((i) => i + 1);
      }}
    />
  );
}
