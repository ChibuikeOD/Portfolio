"use client";

import { useState } from "react";

const CANDIDATES = [
  "/ProfilePic.png",
  "/ProfilePic.jpg",
  "/ProfilePic.jpeg",
  "/ProfilePic.webp",
] as const;

export function ProfilePhoto() {
  const [index, setIndex] = useState(0);

  if (index >= CANDIDATES.length) {
    return null;
  }

  return (
    // eslint-disable-next-line @next/next/no-img-element -- multi-extension fallback without static imports
    <img
      src={CANDIDATES[index]}
      alt="Chibuike Odibeli"
      width={112}
      height={112}
      className="h-28 w-28 shrink-0 rounded-full border border-[#E2E8F0] object-cover"
      onError={() => setIndex((i) => i + 1)}
    />
  );
}
