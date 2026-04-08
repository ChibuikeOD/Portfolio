"use client";

type Props = {
  src: string;
  title: string;
  className?: string;
};

export function StaticInteractiveFrame({ src, title, className = "" }: Props) {
  return (
    <iframe
      title={title}
      src={src}
      className={`h-[min(80vh,850px)] w-full min-w-0 border-0 bg-white ${className}`}
      sandbox="allow-scripts allow-same-origin"
      loading="lazy"
      referrerPolicy="strict-origin-when-cross-origin"
    />
  );
}
