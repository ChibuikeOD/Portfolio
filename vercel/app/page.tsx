"use client";

import dynamic from "next/dynamic";
import { useState } from "react";
import { Modal } from "@/components/Modal";
import { StaticInteractiveFrame } from "@/components/StaticInteractiveFrame";

const CarAnalysisVega = dynamic(
  () =>
    import("@/components/CarAnalysisVega").then((m) => ({
      default: m.CarAnalysisVega,
    })),
  { ssr: false, loading: () => <p className="text-sm text-[#718096]">Loading…</p> }
);

const timelineItems = [
  { date: "Jun 2025", title: "Linux Server Admin", company: "UMass Dartmouth" },
  {
    date: "May 2024",
    title: "Data-Driven Software Engineer",
    company: "Jordan Brooke Estates",
  },
  { date: "May 2023", title: "Software Engineer", company: "Erie Insurance" },
  { date: "Aug 2020", title: "Research Assistant", company: "Penn State Erie" },
];

type BuiltProject = {
  title: string;
  subtitle: string;
  details: string;
  link: string | null;
};

const builtProjects: BuiltProject[] = [
  {
    title: "Audio Deepfake Detection",
    subtitle:
      "PyTorch, Librosa, Spectral Analysis • Multimodal hybrid CNN-LSTM system addressing synthetic media threats (ROC-AUC 0.94).",
    details:
      "This project addressed the growing threat of synthetic media by developing a robust detection framework for audio deepfakes. It combined Convolutional Neural Networks (CNNs) to extract fine-grained spatial features from mel-spectrograms, and Long Short-Term Memory (LSTMs) networks to model temporal dependencies. Trained on extensive datasets of authentic and generated audio, the hybrid architecture achieved a 0.94 ROC-AUC score, demonstrating resilience against compression algorithms and background noise.",
    link: null,
  },
  {
    title: "Edge-Deployed Neural Networks",
    subtitle:
      "C++, Xilinx Vivado HLS, PYNQ • Porting quantized ML models onto FPGA logic for 20x speedup and 60% power reduction.",
    details:
      "Focused on optimizing deep learning models for resource-constrained edge devices. The workflow involved quantizing neural networks and translating their C++ implementations into hardware description via Xilinx Vivado HLS. Designed custom hardware accelerators targeting the Zynq-7000 SoC architecture, utilizing the PYNQ framework for high-level hardware-software abstraction.Validated designs via Vivado simulation, demonstrating a theoretical 20x speedup in inference latency and an estimated 60% reduction in power consumption compared to baseline ARM-based software execution",
    link: null,
  },
  {
    title: "Voice-Automated AI Chatbot (VR)",
    subtitle:
      "Llama 2 (QLoRA), Unity, AWS • Immersive voice-activated tutor for medical students in virtual reality.",
    details:
      "An immersive educational tool built in Unity that simulates realistic clinical scenarios for medical practitioners. The core intelligence is powered by a parameter-efficient fine-tuned Llama 2 model (using QLoRA). The architecture is distributed, relying on AWS infrastructure to host the LLM and bridge real-time Speech-to-Text and Text-to-Speech services. This created a low-latency, hands-free conversational experience within VR.",
    link: null,
  },
  {
    title: "Stock Market Forecasting",
    subtitle:
      "Python, Prophet, Azure, Power BI • End-to-end pipeline predicting OHLCV data with automated cloud storage.",
    details:
      "A comprehensive data engineering and predictive modeling pipeline designed for equity markets. The automated system reliably scrapes daily Open, High, Low, Close, and Volume (OHLCV) data, staging it in Azure Blob Storage. Meta's Prophet algorithm analyzes the time-series trends to forecast future price movements. Finally, this data flows into a dynamic Power BI report, providing stakeholders with intuitive visualizations of historical trends and short-term projections.",
    link:
      "https://app.powerbi.com/links/DS54-3Zmjn?ctid=328d6c0d-0f2f-4b76-9310-9762ba1c3e2d&pbi_source=linkShare&bookmarkGuid=b7a06065-d696-442f-8e4f-52b489fc6a0d",
  },
];

type InteractiveKind = "car" | "iframe";

type InteractiveItem = {
  id: string;
  title: string;
  description: string;
  cta: string;
  kind: InteractiveKind;
  /** Same-origin path under /public for D3 bundles */
  iframeSrc?: string;
};

const interactiveItems: InteractiveItem[] = [
  {
    id: "car_analysis",
    title: "Car Data Analysis ⊇ Vega-Lite interactive dashboard",
    description:
      "Linked brushing across horsepower/price and weight/MPG (same logic as the Streamlit Altair version).",
    cta: "Open Dashboard",
    kind: "car",
  },
  {
    id: "network_analysis",
    title: "Co-Authorship Network ⊇ D3.js force-directed graph",
    description:
      "Interactive network visualization with force-directed layout, parameter controls, and author tooltips.",
    cta: "Open interactive",
    kind: "iframe",
    iframeSrc: "/interactives/network/index.html",
  },
  {
    id: "contour_analysis",
    title: "Contour Analysis ⊇ Medical imaging density contours",
    description:
      "CT scan contour visualization with slice selection and threshold controls.",
    cta: "Open interactive",
    kind: "iframe",
    iframeSrc: "/interactives/contour/activity.html",
  },
  {
    id: "nigeria_timeline",
    title: "Nigeria Economic Timeline ⊇ Historical data visualization",
    description:
      "D3-based timeline of Nigerian economic indicators from bundled CSV datasets.",
    cta: "Open interactive",
    kind: "iframe",
    iframeSrc: "/interactives/nigeria/index.html",
  },
];

type InteractiveModalState =
  | null
  | { kind: "car"; title: string }
  | { kind: "iframe"; title: string; src: string };

export default function Home() {
  const [projectModal, setProjectModal] = useState<BuiltProject | null>(null);
  const [interactiveModal, setInteractiveModal] =
    useState<InteractiveModalState>(null);

  return (
    <>
      <div className="portfolio-blob portfolio-blob-1" aria-hidden />
      <div className="portfolio-blob portfolio-blob-2" aria-hidden />

      <main className="relative z-0 mx-auto max-w-[650px] px-4 pb-20 pt-16 text-[#1A1A1A]">
        <h1 className="portfolio-title-gradient mb-0 text-[2.5rem] font-semibold leading-tight tracking-tight">
          Chibuike &apos;Chib&apos; Odibeli
        </h1>
        <p className="mt-0 text-base text-[#718096]">
          Data Science Master&apos;s Student &amp; Software Engineer
        </p>
        <div className="mb-8 mt-2.5 flex gap-[15px] text-[0.9rem]">
          <a
            href="https://www.linkedin.com/in/chibuike-odibeli-862319220/"
            target="_blank"
            rel="noopener noreferrer"
            className="text-[#718096] no-underline hover:text-[#1A1A1A]"
          >
            LinkedIn
          </a>
          <a
            href="mailto:chibuikeodibeli@gmail.com"
            className="text-[#718096] no-underline hover:text-[#1A1A1A]"
          >
            Email
          </a>
        </div>

        <h2 className="mb-2 mt-10 text-[1.4rem] font-semibold text-[#6A1B9A]">
          About Myself
        </h2>
        <div className="space-y-4 text-[0.95rem] leading-relaxed text-[#4A4A4A]">
          <p>
            I am a Data Science Master&apos;s student at UMass Dartmouth and a
            Data-Driven Software Engineer. I am passionate about turning complex
            data into compelling stories, actionable insights, and robust
            software solutions.
          </p>
          <p>
            With a background in Software Engineering from Penn State, my work
            bridges the gap between machine learning research and full-stack
            application development. I&apos;ve designed immersive VR AI
            chatbots, deployed quantized neural networks to edge devices, and
            modernized large-scale web applications.
          </p>
        </div>

        <h2 className="mb-2 mt-10 text-[1.4rem] font-semibold text-[#6A1B9A]">
          What I&apos;ve Been Up To
        </h2>
        <ul className="list-none space-y-5 p-0">
          {timelineItems.map((item) => (
            <li key={`${item.date}-${item.title}`} className="mb-5">
              <span className="inline-block min-w-[80px] text-[0.85rem] text-[#A0AEC0]">
                {item.date}
              </span>
              <span className="mx-2 text-[1.1rem] font-bold text-[#FF007F]">
                ⊇
              </span>
              <span className="text-[0.95rem] font-semibold text-[#1A1A1A]">
                {item.title}
              </span>{" "}
              <span className="text-[#A0AEC0]">@ {item.company}</span>
            </li>
          ))}
        </ul>

        <h2 className="mb-2 mt-10 text-[1.4rem] font-semibold text-[#6A1B9A]">
          What I&apos;ve Built
        </h2>
        <ul className="list-none space-y-5 p-0">
          {builtProjects.map((proj) => (
            <li key={proj.title} className="mb-5">
              <div className="mb-1 text-[0.95rem] font-semibold text-[#1A1A1A]">
                {proj.title}
              </div>
              <div className="mt-0.5 text-[0.85rem] text-[#718096]">
                {proj.subtitle}
              </div>
              <button
                type="button"
                onClick={() => setProjectModal(proj)}
                className="mt-2 cursor-pointer border-0 bg-transparent p-0 text-[0.95rem] text-[#1A1A1A] underline decoration-[#E2E8F0] underline-offset-4 hover:decoration-[#1A1A1A]"
              >
                View Project
              </button>
            </li>
          ))}
        </ul>

        <div className="mt-10" />

        <div className="mb-3 text-[0.95rem] font-semibold text-[#1A1A1A]">
          Interactive Visualizations
        </div>
        <div className="space-y-4">
          {interactiveItems.map((item) => (
            <details
              key={item.id}
              className="rounded-md border border-[#E2E8F0]/80 bg-[#FDF9F6]/80 px-3 py-2"
            >
              <summary className="cursor-pointer text-[0.9rem] font-medium text-[#4A4A4A]">
                {item.title}
              </summary>
              <p className="mt-2 text-[0.95rem] leading-relaxed text-[#4A4A4A]">
                {item.description}
              </p>
              <button
                type="button"
                onClick={() => {
                  if (item.kind === "car") {
                    setInteractiveModal({ kind: "car", title: item.title });
                  } else if (item.iframeSrc) {
                    setInteractiveModal({
                      kind: "iframe",
                      title: item.title,
                      src: item.iframeSrc,
                    });
                  }
                }}
                className="mt-3 cursor-pointer rounded border border-[#E2E8F0] bg-white px-3 py-1.5 text-sm font-medium text-[#1A1A1A] hover:bg-[#f7f2ee]"
              >
                {item.cta}
              </button>
            </details>
          ))}
        </div>

        <h2 className="mb-2 mt-10 text-[1.4rem] font-semibold text-[#6A1B9A]">
          Interests / Readings
        </h2>
        <ul className="interests-list mt-4 space-y-1 text-[0.95rem] leading-relaxed text-[#4A4A4A]">
          <li>Machine Learning Architecture</li>
          <li>Distributed Systems</li>
          <li>Science Fiction</li>
          <li>Community Technology Education</li>
        </ul>
      </main>

      <Modal
        title="Project Details"
        open={projectModal !== null}
        onClose={() => setProjectModal(null)}
      >
        {projectModal && (
          <div className="space-y-4 px-4 py-4 text-[0.95rem] leading-relaxed text-[#4A4A4A]">
            <h3 className="text-lg font-semibold text-[#1A1A1A]">
              {projectModal.title}
            </h3>
            <p>{projectModal.details}</p>
            {projectModal.link && (
              <a
                href={projectModal.link}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block rounded-md bg-[#1A1A1A] px-4 py-2 text-sm font-medium text-white no-underline hover:opacity-90"
              >
                View Live Project
              </a>
            )}
          </div>
        )}
      </Modal>

      <Modal
        title={interactiveModal?.title ?? "Interactive"}
        open={interactiveModal !== null}
        onClose={() => setInteractiveModal(null)}
      >
        {interactiveModal?.kind === "car" && (
          <div className="flex flex-col gap-3 px-2 py-2 sm:px-4 sm:py-4">
            <p className="text-sm text-[#718096]">
              Click and drag on either chart to brush; selection links both views.
            </p>
            <CarAnalysisVega />
          </div>
        )}
        {interactiveModal?.kind === "iframe" && (
          <div className="px-1 pb-2 sm:px-2">
            <StaticInteractiveFrame
              src={interactiveModal.src}
              title={interactiveModal.title}
            />
          </div>
        )}
      </Modal>
    </>
  );
}
