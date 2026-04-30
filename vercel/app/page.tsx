"use client";

import dynamic from "next/dynamic";
import { useEffect, useState } from "react";
import { Modal } from "@/components/Modal";
import { ProfilePhoto } from "@/components/ProfilePhoto";
import { StaticInteractiveFrame } from "@/components/StaticInteractiveFrame";

const CarAnalysisVega = dynamic(
  () =>
    import("@/components/CarAnalysisVega").then((m) => ({
      default: m.CarAnalysisVega,
    })),
  { ssr: false, loading: () => <p className="text-sm text-[#718096]">Loading…</p> }
);

type BuiltProject = {
  title: string;
  subtitle: string;
  details: string;
  link: string | null;
};

const projects: BuiltProject[] = [
  {
    title: "Real Estate Pro Forma Investment Analyzer",
    subtitle:
      "Solo Full-Stack Developer • Mobile-first underwriting engine for commercial real estate.",
    details:
      "A dynamic, mobile-first underwriting engine that converts property walk-through inputs into a comprehensive 10-year IRR projection in seconds.",
    link: "https://forma-app.net",
  },
  {
    title: "Stock Market Forecasting",
    subtitle:
      "Python, Prophet, Azure, Power BI • End-to-end pipeline predicting OHLCV data with automated cloud storage.",
    details:
      "A comprehensive data engineering and predictive modeling pipeline designed for equity markets. The automated system reliably scrapes daily Open, High, Low, Close, and Volume (OHLCV) data, staging it in Azure Blob Storage. Meta's Prophet algorithm analyzes the time-series trends to forecast future price movements. Finally, this data flows into a dynamic Power BI report, providing stakeholders with intuitive visualizations of historical trends and short-term projections.",
    link:
      "https://app.powerbi.com/view?r=eyJrIjoiYTJjZmYxNDQtODRmNC00YmZjLWI0ZDQtZTYwMGVmNzMzZTFhIiwidCI6IjA1YjVmMDhmLTdkZWQtNDNjNS1iZTNmLWFmMDQyMDcwNzQxNCJ9",
  },
  {
    title: "Automated PDF Remediation",
    subtitle:
      "LayoutLMv3, FastAPI, pikepdf, React • AI-assisted PDF/UA accessibility at scale.",
    details:
      "An automation workflow that remediates untagged PDFs by inferring document structure, restoring reading order, remediating tables, and artifacting decorative content—then materializing fixes into the PDF structure tree for assistive technology.",
    link: null,
  },
  {
    title: "Voice-Automated AI Chatbot (VR)",
    subtitle:
      "Llama 2 (QLoRA), Unity, AWS • Low-latency voice tutor for clinical training in VR.",
    details:
      "A hands-free, voice-driven VR tutor that simulates clinical scenarios and provides responsive conversational guidance through a cloud-hosted LLM pipeline.",
    link: null,
  },
];

const research: BuiltProject[] = [
  {
    title: "Audio Deepfake Detection",
    subtitle:
      "PyTorch, Librosa, Spectral Analysis • Multimodal hybrid CNN-LSTM system addressing synthetic media threats (ROC-AUC 0.94).",
    details:
      "A multimodal deep learning framework for synthetic speech detection that fuses CNN-based spectral representations with LSTM temporal modeling, trained and evaluated under realistic channel degradations (compression and background noise).",
    link: null,
  },
  {
    title: "Edge-Deployed Neural Networks",
    subtitle:
      "hls4ml, Vivado HLS, Keras/TensorFlow • Hardware-aware quantization and FPGA inference.",
    details:
      "End-to-end path from a Keras deep learning model to a quantized, HLS-simulated FPGA inference engine—optimizing fixed-point arithmetic for throughput and resource use while tracking numerical fidelity against the floating-point baseline.",
    link: null,
  },
];

const workExperience = [
  { date: "Jun 2025", title: "Linux Server Admin", company: "UMass Dartmouth" },
  {
    date: "May 2024",
    title: "Data-Driven Software Engineer",
    company: "Jordan Brooke Estates",
  },
  { date: "May 2023", title: "Software Engineer", company: "Erie Insurance" },
  { date: "Aug 2020", title: "Research Assistant", company: "Penn State Erie" },
] as const;

const FORMA_TITLE = "Real Estate Pro Forma Investment Analyzer";
const FORMA_PAGES = [
  {
    title: "Overview",
    content: (
      <div className="space-y-2">
        <p>
          <span className="font-semibold text-[#1A1A1A]">Role:</span> Solo
          Full-Stack Developer
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">Project:</span> Real
          Estate Pro Forma Investment Analyzer (Forma)
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">Core outcome:</span> A
          mobile-first underwriting engine that moves investors from a property
          walk-through to a full 10-year IRR projection in seconds.
        </p>
      </div>
    ),
  },
  {
    title: "Problem",
    content: (
      <div className="space-y-2">
        <p>
          Commercial real estate investors frequently rely on static,
          fragmented, and error-prone Excel spreadsheets for financial modeling.
          These files are difficult to maintain, easy to break, and hard to use
          in the field.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">Solution:</span> I
          architected and deployed a dynamic, mobile-first underwriting engine
          that transitions an investor from a property walk-through directly to
          a comprehensive 10-year IRR projection in seconds.
        </p>
      </div>
    ),
  },
  {
    title: "Architecture & Stack",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Frontend ecosystem:
          </span>{" "}
          React Native + Expo for a single JavaScript/TypeScript codebase with
          cross-platform consistency and native performance on iOS and Android.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            State & logic engine:
          </span>{" "}
          A{" "}
          <code className="rounded bg-[#E2E8F0]/60 px-1">
            useProformaCalculator
          </code>{" "}
          hook coordinating dozens of interdependent inputs (purchase price,
          renovation budgets, debt tranches, exit cap rates) and recomputing
          KPIs in real time.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Data visualization:
          </span>{" "}
          Integrated{" "}
          <code className="rounded bg-[#E2E8F0]/60 px-1">
            react-native-chart-kit
          </code>{" "}
          with interactive trendline mapping to track DSCR and NOI vs. cash flow
          over a 10-year hold period.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Backend & cloud sync:
          </span>{" "}
          Centralized, cloud-synced backend to provide a single source of truth
          across devices.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Performance optimization:
          </span>{" "}
          Tuned rendering and interaction for large month-by-month matrices
          using React Native’s{" "}
          <code className="rounded bg-[#E2E8F0]/60 px-1">ScrollView</code> and{" "}
          <code className="rounded bg-[#E2E8F0]/60 px-1">FlatList</code>.
        </li>
      </ul>
    ),
  },
  {
    title: "Business Logic",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Tiered analytical workflow:
          </span>{" "}
          A Year 1 waterfall cascade from Gross Potential Rent (GPR) → Effective
          Gross Income (EGI) → Net Operating Income (NOI) → final cash flow.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Advanced capital structuring:
          </span>{" "}
          Real-world financing support for multi-tier debt tranches, mezzanine
          debt, seller financing, and interest-only periods.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Institutional-grade return metrics:
          </span>{" "}
          Implemented XIRR and XNPV calculations to correctly handle irregular
          cash flow dates.
        </li>
      </ul>
    ),
  },
  {
    title: "Deployment & Monetization",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">CI/CD & OTA:</span>{" "}
          Used Expo Application Services (EAS) for streamlined releases and
          rapid over-the-air updates.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Subscription architecture:
          </span>{" "}
          Integrated RevenueCat to support a freemium model (free Year 1
          analytics; premium unlocks the 10-year projection matrix and advanced
          visual analytics suite).
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">ASO:</span> Executed a
          data-driven keyword strategy targeting high-intent long-tail terms
          (e.g., “DSCR calculator,” “multifamily proforma”).
        </li>
      </ul>
    ),
  },
] as const;

const STOCK_TITLE = "Stock Market Forecasting";
const STOCK_PAGES = [
  {
    title: "Overview",
    content: (
      <div className="space-y-2">
        <p>
          <span className="font-semibold text-[#1A1A1A]">Project:</span> Stock
          Market Forecasting
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">Focus:</span>{" "}
          End-to-end data engineering and time-series forecasting for equity
          markets—from automated ingestion through cloud storage to interactive
          reporting.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">Stack:</span> Python,
          Meta Prophet, Microsoft Azure (Blob Storage), Power BI.
        </p>
      </div>
    ),
  },
  {
    title: "Problem & Goals",
    content: (
      <div className="space-y-2">
        <p>
          Market analysis workflows often depend on manually refreshed
          spreadsheets and disconnected tools. That fragmentation increases
          operational risk, slows iteration, and makes it harder to communicate
          forecasts consistently.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">Objectives:</span>{" "}
          Automate reliable collection of daily OHLCV data, centralize historical
          series in the cloud, produce repeatable forecasts, and deliver a
          governed, shareable analytics surface in Power BI.
        </p>
      </div>
    ),
  },
  {
    title: "Data Pipeline & Azure",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">Ingestion:</span>{" "}
          Automated scraping of daily Open, High, Low, Close, and Volume
          (OHLCV) with validation and structured staging for downstream modeling.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Cloud storage:</span>{" "}
          Curated datasets persisted in Azure Blob Storage as a durable landing
          zone and historical archive.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Operations:</span>{" "}
          Idempotent writes, clear organization by symbol and date where
          applicable, and a schedule-friendly pipeline without manual file
          shuffling.
        </li>
      </ul>
    ),
  },
  {
    title: "Modeling & Analytics",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">Time-series engine:</span>{" "}
          Meta Prophet to model trend and seasonality and generate forward-looking
          projections from historical price series.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Robustness:</span>{" "}
          Addressed missing dates, regime shifts, and volatility spikes as part of
          fit and review—not as afterthoughts.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Interpretability:</span>{" "}
          Structured outputs so analysts can compare realized history to
          projected ranges instead of treating the model as a black box.
        </li>
      </ul>
    ),
  },
  {
    title: "Reporting & Delivery",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">Power BI:</span> A
          dynamic report connecting stakeholders to historical trends and
          short-term projections in one governed experience.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Publication:</span>{" "}
          Shared via Power BI’s web experience so reviewers are not tied to
          local spreadsheet workflows.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Outcome:</span> A
          repeatable path from raw daily inputs to cloud-backed storage, modeled
          forecasts, and executive-ready visuals.
        </li>
      </ul>
    ),
  },
] as const;

const PDF_TITLE = "Automated PDF Remediation";
const PDF_PAGES = [
  {
    title: "Overview & Problem",
    content: (
      <div className="space-y-2">
        <p>
          Most PDFs on the web are effectively <strong>untagged</strong>: they
          render visually but lack the logical structure assistive technologies
          need. For the hundreds of millions of people who rely on screen
          readers, that gap makes documents incoherent or unusable.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">
            Manual remediation
          </span>{" "}
          is slow, expensive, and depends on specialized expertise—so
          inaccessible PDFs accumulate faster than teams can fix them.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">This project:</span> An
          automated pipeline that converts visual layout into accessible digital
          logic, writes structure into the PDF, and ties engineering decisions
          directly to WCAG-oriented outcomes.
        </p>
      </div>
    ),
  },
  {
    title: "Structure & Semantics",
    content: (
      <div className="space-y-2">
        <p>
          Screen readers do not infer meaning from bold type or large fonts;
          they consume the PDF <strong>structure tree</strong> (tags).
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">AI approach:</span> A
          LayoutLM-style document vision model acts as the “eyes” of the
          system—recognizing that a large, centered string is a{" "}
          <code className="rounded bg-[#E2E8F0]/60 px-1">&lt;H1&gt;</code>{" "}
          (Heading 1), not arbitrary body text.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">
            Accessibility impact:
          </span>{" "}
          Supports{" "}
          <span className="font-semibold">WCAG 1.3.1 (Info and Relationships)</span>{" "}
          by generating meaningful tags so users can navigate by headings—similar
          to how sighted readers skim titles.
        </p>
      </div>
    ),
  },
  {
    title: "Meaningful Sequence",
    content: (
      <div className="space-y-2">
        <p>
          PDF content is often ordered for print mechanics, not human reading
          order—footnotes, sidebars, and multi-column layouts can appear in code
          in a sequence that does not match visual flow.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">AI + geometry:</span>{" "}
          Because the model reasons over the page spatially,{" "}
          <code className="rounded bg-[#E2E8F0]/60 px-1">fix_reading_order()</code>{" "}
          re-sorts elements in a top-to-bottom, column-aware order aligned with
          how a human reads.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">
            Accessibility impact:
          </span>{" "}
          Addresses{" "}
          <span className="font-semibold">WCAG 1.3.2 (Meaningful Sequence)</span>,
          preventing the “jumble effect” where assistive technology reads a
          second column before the first or jumps unexpectedly between regions.
        </p>
      </div>
    ),
  },
  {
    title: "Table Remediation",
    content: (
      <div className="space-y-2">
        <p>
          Untagged tables frequently degrade into disconnected strings of numbers
          and labels—little usable context for non-visual navigation.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">AI approach:</span>{" "}
          Detect table boundaries and header rows (
          <code className="rounded bg-[#E2E8F0]/60 px-1">&lt;TH&gt;</code>), then
          programmatically assign{" "}
          <span className="font-semibold">scope</span> so headers bind to the
          correct rows or columns.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">
            Accessibility impact:
          </span>{" "}
          Users hear coherent table announcements (dimension + header + cell)
          instead of isolated values with no relationship.
        </p>
      </div>
    ),
  },
  {
    title: "Artifacts & Non-text",
    content: (
      <div className="space-y-2">
        <p>
          Decorative graphics, rules, and repeated “visual noise” are painful
          when assistive technology announces <strong>“Graphic”</strong> for
          every line or flourish.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">AI approach:</span>{" "}
          Classify content vs. decoration and automatically{" "}
          <span className="font-semibold">artifact</span> non-informative elements
          so they do not participate in the reading experience.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">
            Accessibility impact:
          </span>{" "}
          Aligns with{" "}
          <span className="font-semibold">WCAG 1.1.1 (Non-text Content)</span> by
          reducing cognitive load and keeping focus on meaningful information.
        </p>
      </div>
    ),
  },
  {
    title: "Technical Highlights",
    content: (
      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-[0.9rem]">
          <thead>
            <tr className="border-b border-[#E2E8F0] text-left">
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">Feature</th>
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Technology
              </th>
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Innovation
              </th>
            </tr>
          </thead>
          <tbody className="text-[#4A4A4A]">
            <tr className="border-b border-[#F1F5F9] align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Document vision
              </td>
              <td className="px-2 py-2">LayoutLMv3</td>
              <td className="px-2 py-2">
                Fine-tuned on library-specific and archival layouts to recognize
                complex academic structures.
              </td>
            </tr>
            <tr className="border-b border-[#F1F5F9] align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Structure injection
              </td>
              <td className="px-2 py-2">FastAPI + pikepdf</td>
              <td className="px-2 py-2">
                Bridges model predictions into the physical PDF{" "}
                <code className="rounded bg-[#E2E8F0]/60 px-1">/StructTreeRoot</code>{" "}
                and tag graph.
              </td>
            </tr>
            <tr className="align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Remediation UI
              </td>
              <td className="px-2 py-2">React</td>
              <td className="px-2 py-2">
                Before/after dashboard showing accessibility score improvements as
                automated fixes land.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    ),
  },
] as const;

const AUDIO_TITLE = "Audio Deepfake Detection";
const AUDIO_PAGES = [
  {
    title: "Overview & Motivation",
    content: (
      <div className="space-y-2">
        <p>
          <span className="font-semibold text-[#1A1A1A]">Project:</span> Audio
          Deepfake Detection
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">Motivation:</span>{" "}
          Generative audio models make it increasingly easy to fabricate
          convincing speech. The goal was a detector that generalizes beyond a
          single generator or dataset and remains useful under real-world
          recording conditions.
        </p>
        
      </div>
    ),
  },
  {
    title: "Problem Framing",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Subtle manipulations:
          </span>{" "}
          Synthetic speech can preserve prosody and bandwidth cues that fool
          naive spectral heuristics.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Distribution shift:</span>{" "}
          Models trained on one synthesis family often fail when generators,
          codecs, or microphones change.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Operational realism:
          </span>{" "}
          Deployed detectors must tolerate lossy compression, variable SNR, and
          background interference—conditions often missing from “clean lab”
          datasets.
        </li>
      </ul>
    ),
  },
  {
    title: "Data & Representation",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">Frontend DSP:</span>{" "}
          <strong>Librosa</strong> for framing, windowing, and mel-scale feature
          extraction to stabilize inputs across sample rates and devices.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Mel-spectrograms:</span>{" "}
          Time–frequency tiles as structured inputs so convolutional filters can
          capture fine-grained harmonic and noise-floor signatures.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Augmentation & hygiene:
          </span>{" "}
          Noise, codec-like degradation, and gain variation during training to
          reduce overfitting to a single acoustic environment.
        </li>
      </ul>
    ),
  },
  {
    title: "Model Architecture",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">CNN branch:</span>{" "}
          Convolutional layers extract local spatial patterns from
          mel-spectrogram patches (short-term spectral texture).
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">LSTM branch:</span>{" "}
          Recurrent modeling captures long-range temporal dependencies across
          frames (prosody, coarticulation, and generator-specific temporal
          artifacts).
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Hybrid fusion:</span>{" "}
          Combined pathways into a unified classifier in{" "}
          <strong>PyTorch</strong> so the model jointly reasons about spectral
          appearance and temporal evolution.
        </li>
      </ul>
    ),
  },
  {
    title: "Training & Evaluation",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">Objective:</span> Binary
          discrimination (authentic vs. synthetic) with threshold-independent
          reporting via ROC-AUC.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Generalization:</span>{" "}
          Stress-tested across sources to avoid memorizing a single generator
          fingerprint.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Robustness:</span>{" "}
          Evaluated under compression and background noise to approximate real
          playback and capture pipelines.
        </li>
      </ul>
    ),
  },
  {
    title: "Technical Highlights",
    content: (
      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-[0.9rem]">
          <thead>
            <tr className="border-b border-[#E2E8F0] text-left">
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Capability
              </th>
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Technology
              </th>
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Innovation
              </th>
            </tr>
          </thead>
          <tbody className="text-[#4A4A4A]">
            <tr className="border-b border-[#F1F5F9] align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Spectral modeling
              </td>
              <td className="px-2 py-2">CNN on mel-spectrograms</td>
              <td className="px-2 py-2">
                Localized time–frequency cues that separate subtle synthesis
                artifacts from natural speech texture.
              </td>
            </tr>
            <tr className="border-b border-[#F1F5F9] align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Temporal modeling
              </td>
              <td className="px-2 py-2">LSTM / sequence head</td>
              <td className="px-2 py-2">
                Frame-to-frame dynamics that CNNs alone can miss across longer
                utterances.
              </td>
            </tr>
            <tr className="align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Training stack
              </td>
              <td className="px-2 py-2">PyTorch + Librosa</td>
              <td className="px-2 py-2">
                End-to-end pipeline from raw waveform to calibrated probabilities
                with degradation-aware augmentation.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    ),
  },
] as const;

const EDGE_TITLE = "Edge-Deployed Neural Networks";
const EDGE_PAGES = [
  {
    title: "Overview",
    content: (
      <div className="space-y-2">
        <p>
          <span className="font-semibold text-[#1A1A1A]">Focus:</span>{" "}
          Hardware-aware quantization for FPGA inference.
        </p>
        <p>
          I built an end-to-end workflow to deploy a{" "}
          <strong>Keras</strong>-trained model to an <strong>FPGA</strong>. The
          central challenge was translating floating-point mathematics into{" "}
          <strong>hardware-efficient fixed-point</strong> arithmetic without
          unacceptable accuracy loss.
        </p>
        <p>
          Using <strong>hls4ml</strong>, I targeted a high-throughput inference
          implementation for <strong>resource-constrained</strong> edge
          environments, with validation through HLS simulation.
        </p>
      </div>
    ),
  },
  {
    title: "Quantization Strategy",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">Model compression:</span>{" "}
          Moved from 32-bit floating-point toward{" "}
          <strong>custom fixed-point</strong> representations sized for FPGA
          datapaths.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Per-layer precision:</span>{" "}
          Manually tuned bit-widths (for example,{" "}
          <code className="rounded bg-[#E2E8F0]/60 px-1">ap_fixed&lt;16,6&gt;</code>
          ) layer by layer to balance numerical fidelity against{" "}
          <strong>LUT and DSP</strong> budget.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Co-design:</span> Each
          bit-width choice directly affects area and power; quantization was
          treated as part of the architecture—not only a training afterthought.
        </li>
      </ul>
    ),
  },
  {
    title: "Profiling & Bounds",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Static and dynamic analysis:
          </span>{" "}
          Profiled activation ranges and weight distributions to choose minimum
          integer and fractional bits per layer.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Overflow prevention:
          </span>{" "}
          Bounded tensors so fixed-point operators remained stable across
          representative inputs.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Traceability:</span>{" "}
          Decisions tied to measured signal statistics rather than generic
          defaults.
        </li>
      </ul>
    ),
  },
  {
    title: "HLS & Validation",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">Vivado HLS:</span>{" "}
          Simulated hardware-oriented C++ to verify structure and behavior before
          full RTL closure.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Equivalence checking:
          </span>{" "}
          Compared quantized fixed-point behavior against the floating-point
          baseline on held-out data.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Outcome:</span> A
          validated path from trained network → fixed-point specification →
          HLS-friendly FPGA implementation.
        </li>
      </ul>
    ),
  },
  {
    title: "Results & Stack",
    content: (
      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-[0.9rem]">
          <thead>
            <tr className="border-b border-[#E2E8F0] text-left">
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Dimension
              </th>
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">Detail</th>
            </tr>
          </thead>
          <tbody className="text-[#4A4A4A]">
            <tr className="border-b border-[#F1F5F9] align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Optimization tooling
              </td>
              <td className="px-2 py-2">hls4ml, Xilinx Vivado (HLS toolchain)</td>
            </tr>
            <tr className="border-b border-[#F1F5F9] align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Frameworks
              </td>
              <td className="px-2 py-2">Keras / TensorFlow, Python</td>
            </tr>
            <tr className="border-b border-[#F1F5F9] align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Hardware concepts
              </td>
              <td className="px-2 py-2">
                High-level synthesis (HLS), fixed-point arithmetic, RTL-oriented
                simulation
              </td>
            </tr>
            <tr className="align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">Impact</td>
              <td className="px-2 py-2">
                Substantially reduced memory footprint and logic utilization
                through disciplined per-layer quantization—consistent with prior
                estimates of large inference speedup and power reduction vs.
                baseline ARM execution on comparable workloads.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    ),
  },
] as const;

const VR_TITLE = "Voice-Automated AI Chatbot (VR)";
const VR_PAGES = [
  {
    title: "Overview",
    content: (
      <div className="space-y-2">
        <p>
          <span className="font-semibold text-[#1A1A1A]">Project:</span> Voice-
          Automated AI Chatbot (VR)
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">Goal:</span> Deliver a
          hands-free, low-latency conversational tutor inside VR to support
          realistic clinical training workflows.
        </p>
        <p>
          <span className="font-semibold text-[#1A1A1A]">Outcome:</span> A
          distributed pipeline bridging Speech-to-Text (STT), an LLM reasoning
          layer, and Text-to-Speech (TTS) back into Unity for natural, voice-
          first interaction.
        </p>
      </div>
    ),
  },
  {
    title: "Use Case & UX",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Hands-free interaction:
          </span>{" "}
          Designed for sessions where typing or menu navigation breaks immersion.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Clinical realism:</span>{" "}
          Dialogue flow aligned with simulated patient encounters and guided
          decision-making.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Low friction:</span>{" "}
          Voice-first design reduces cognitive load and keeps attention on the
          scenario, not UI mechanics.
        </li>
      </ul>
    ),
  },
  {
    title: "Architecture & Stack",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">VR runtime:</span> Unity
          for immersive scenario simulation and interaction.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">LLM core:</span> Llama 2
          fine-tuned with QLoRA for domain relevance with practical training
          efficiency.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Cloud infrastructure:
          </span>{" "}
          AWS-hosted services coordinating inference and speech routing.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Speech loop:</span> Real-
          time STT → LLM → TTS for continuous conversational turns.
        </li>
      </ul>
    ),
  },
  {
    title: "Latency & Reliability",
    content: (
      <ul className="list-disc space-y-2 pl-5">
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Pipeline orchestration:
          </span>{" "}
          Separated STT, LLM, and TTS so each stage can be optimized
          independently.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">
            Conversational latency:
          </span>{" "}
          Minimized end-to-end response time to avoid “turn-based” feel in VR.
        </li>
        <li>
          <span className="font-semibold text-[#1A1A1A]">Resilience:</span>{" "}
          Guardrails for partial speech-service failures to preserve session
          usability.
        </li>
      </ul>
    ),
  },
  {
    title: "Technical Highlights",
    content: (
      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-[0.9rem]">
          <thead>
            <tr className="border-b border-[#E2E8F0] text-left">
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Capability
              </th>
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Technology
              </th>
              <th className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Implementation detail
              </th>
            </tr>
          </thead>
          <tbody className="text-[#4A4A4A]">
            <tr className="border-b border-[#F1F5F9] align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                VR experience
              </td>
              <td className="px-2 py-2">Unity</td>
              <td className="px-2 py-2">
                Immersive scenario simulation with a voice-driven interaction
                loop.
              </td>
            </tr>
            <tr className="border-b border-[#F1F5F9] align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                LLM adaptation
              </td>
              <td className="px-2 py-2">Llama 2 + QLoRA</td>
              <td className="px-2 py-2">
                Parameter-efficient fine-tuning aligned to clinical tutoring
                needs.
              </td>
            </tr>
            <tr className="align-top">
              <td className="px-2 py-2 font-semibold text-[#1A1A1A]">
                Cloud orchestration
              </td>
              <td className="px-2 py-2">AWS + STT/TTS</td>
              <td className="px-2 py-2">
                Distributed speech + inference pipeline optimized for low-latency
                turn-taking.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    ),
  },
] as const;

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
  const [projectPageIdx, setProjectPageIdx] = useState(0);
  const [interactiveModal, setInteractiveModal] =
    useState<InteractiveModalState>(null);

  useEffect(() => {
    setProjectPageIdx(0);
  }, [projectModal?.title]);

  const projectDetailPages =
    projectModal?.title === FORMA_TITLE
      ? FORMA_PAGES
      : projectModal?.title === STOCK_TITLE
        ? STOCK_PAGES
        : projectModal?.title === PDF_TITLE
          ? PDF_PAGES
          : projectModal?.title === AUDIO_TITLE
            ? AUDIO_PAGES
            : projectModal?.title === EDGE_TITLE
              ? EDGE_PAGES
              : projectModal?.title === VR_TITLE
                ? VR_PAGES
                : null;

  return (
    <>
      <div className="portfolio-blob portfolio-blob-1" aria-hidden />
      <div className="portfolio-blob portfolio-blob-2" aria-hidden />

      <main className="relative z-0 mx-auto max-w-[650px] px-4 pb-20 pt-16 text-[#1A1A1A]">
        <div className="flex flex-row items-start gap-5">
          <ProfilePhoto />
          <div className="min-w-0 flex-1">
            <h1 className="portfolio-title-gradient mb-0 text-[2.5rem] font-semibold leading-tight tracking-tight">
              Chibuike &apos;Chib&apos; Odibeli
            </h1>
            <p className="mt-0 text-base text-[#718096]">
              Data Science Master&apos;s Student &amp; Software Engineer
            </p>
            <p className="mt-0 text-base text-[#718096]">
              Solo Developer of Forma. Check it out below!
            </p>
            <div className="mt-2.5 flex gap-[15px] text-[0.9rem]">
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
            <div className="mt-3 mb-8 flex flex-wrap items-center gap-2.5">
              <a
                href="https://forma-app.net"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block rounded-md bg-[#0a2342] px-5 py-2.5 text-[0.95rem] font-semibold text-[#9ecfff] no-underline hover:opacity-92 hover:text-[#c5e5ff]"
              >
                Forma
              </a>
              <a
                href="https://app.powerbi.com/view?r=eyJrIjoiYTJjZmYxNDQtODRmNC00YmZjLWI0ZDQtZTYwMGVmNzMzZTFhIiwidCI6IjA1YjVmMDhmLTdkZWQtNDNjNS1iZTNmLWFmMDQyMDcwNzQxNCJ9"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block rounded-md bg-[#0a2342] px-5 py-2.5 text-[0.95rem] font-semibold text-[#9ecfff] no-underline hover:opacity-92 hover:text-[#c5e5ff]"
              >
                Daily Stock Price Prediction
              </a>
            </div>
          </div>
        </div>

        <h2 className="mb-2 mt-10 text-[1.55rem] font-semibold text-[#6A1B9A]">
          About Myself
        </h2>
        <div className="space-y-4 text-[0.95rem] leading-relaxed text-[#4A4A4A]">
          <p>
            I am a Software Engineer with a strong background in Data Science and Machine Learning. 
            I combine meticulous research methods with the speed of industry to create architecturally robust products
            that satisfy user needs.
          </p>
          <p>
           I have professional experience in building end-to-end machine learning pipelines and full-stack applications
           in production environments. My research is surrounded around making large language models more
           ubiquitous in software engineering and other use cases. This includes making them more accessible i.e. 
           ensuring they are lightweight enough to run on as many devices as possible, and also making them more secure by 
           implementing safeguards to mitigate some of the inherent risks associated with this powerful technology
          </p>
        </div>

        <h2 className="mb-2 mt-10 text-[1.55rem] font-semibold text-[#6A1B9A]">
          Work Experience
        </h2>
        <ul className="list-none space-y-5 p-0">
          {workExperience.map((item) => (
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

        <h2 className="mb-2 mt-10 text-[1.55rem] font-semibold text-[#6A1B9A]">
          Projects
        </h2>
        <ul className="list-none space-y-5 p-0">
          {projects.map((proj) => (
            <li key={`proj-${proj.title}`} className="mb-5">
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

        <h2 className="mb-2 mt-10 text-[1.55rem] font-semibold text-[#6A1B9A]">
          Research
        </h2>
        <ul className="list-none space-y-5 p-0">
          {research.map((proj) => (
            <li key={`research-${proj.title}`} className="mb-5">
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

        <h2 className="mb-2 mt-10 text-[1.55rem] font-semibold text-[#6A1B9A]">
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
            {projectDetailPages ? (
              <>
                <div className="flex flex-wrap gap-2">
                  {projectDetailPages.map((p, idx) => (
                    <button
                      key={p.title}
                      type="button"
                      onClick={() => setProjectPageIdx(idx)}
                      className={
                        idx === projectPageIdx
                          ? "rounded-md bg-[#0a2342] px-3 py-1.5 text-sm font-semibold text-[#9ecfff]"
                          : "rounded-md border border-[#E2E8F0] bg-white px-3 py-1.5 text-sm font-medium text-[#4A4A4A] hover:bg-[#f7f2ee]"
                      }
                    >
                      {p.title}
                    </button>
                  ))}
                </div>

                <div className="rounded-md border border-[#E2E8F0]/80 bg-white/70 p-4">
                  {projectDetailPages[projectPageIdx]?.content}
                </div>

                <div className="flex items-center justify-between gap-3">
                  <button
                    type="button"
                    onClick={() => setProjectPageIdx((i) => Math.max(0, i - 1))}
                    disabled={projectPageIdx === 0}
                    className="rounded-md border border-[#E2E8F0] bg-white px-3 py-1.5 text-sm font-medium text-[#1A1A1A] disabled:opacity-40"
                  >
                    Previous
                  </button>
                  <div className="text-sm text-[#718096]">
                    {projectPageIdx + 1} / {projectDetailPages.length}
                  </div>
                  <button
                    type="button"
                    onClick={() =>
                      setProjectPageIdx((i) =>
                        Math.min(projectDetailPages.length - 1, i + 1)
                      )
                    }
                    disabled={projectPageIdx >= projectDetailPages.length - 1}
                    className="rounded-md border border-[#E2E8F0] bg-white px-3 py-1.5 text-sm font-medium text-[#1A1A1A] disabled:opacity-40"
                  >
                    Next
                  </button>
                </div>
              </>
            ) : (
              <p>{projectModal.details}</p>
            )}
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
