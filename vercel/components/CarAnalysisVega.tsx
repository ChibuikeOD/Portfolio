"use client";

import { useEffect, useMemo, useState } from "react";
import { VegaEmbed } from "react-vega";
import type { VisualizationSpec } from "vega-embed";
import Papa from "papaparse";

type CarRow = {
  Model: string;
  Price: number;
  Country: string;
  MPG: number;
  Weight: number;
  HP: number;
};

export function CarAnalysisVega() {
  const [rows, setRows] = useState<CarRow[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetch("/data/car_sample_data.csv")
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.text();
      })
      .then((text) => {
        const parsed = Papa.parse<Record<string, string>>(text, {
          header: true,
          skipEmptyLines: true,
        });
        if (parsed.errors.length) {
          throw new Error(parsed.errors[0]?.message ?? "CSV parse error");
        }
        const cleaned: CarRow[] = [];
        for (const r of parsed.data) {
          const price = Number(r.Price);
          const mpg = Number(r.MPG);
          const weight = Number(r.Weight);
          const hp = Number(r.HP);
          if (
            r.Model &&
            Number.isFinite(price) &&
            Number.isFinite(mpg) &&
            Number.isFinite(weight) &&
            Number.isFinite(hp)
          ) {
            cleaned.push({
              Model: r.Model,
              Price: price,
              Country: r.Country ?? "",
              MPG: mpg,
              Weight: weight,
              HP: hp,
            });
          }
        }
        if (!cancelled) setRows(cleaned);
      })
      .catch((e) => {
        if (!cancelled) setError(e instanceof Error ? e.message : "Load failed");
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const spec = useMemo((): VisualizationSpec => {
    return {
      $schema: "https://vega.github.io/schema/vega-lite/v5.json",
      description: "Linked brushing (Vega-Lite, mirrors Altair dashboard)",
      data: { values: rows },
      params: [
        {
          name: "brush",
          select: { type: "interval", encodings: ["x", "y"] },
        },
      ],
      hconcat: [
        {
          title: "Horsepower vs. Price",
          width: 400,
          height: 300,
          mark: { type: "circle", size: 60 },
          encoding: {
            x: { field: "HP", type: "quantitative" },
            y: { field: "Price", type: "quantitative" },
            color: {
              condition: {
                param: "brush",
                field: "Country",
                type: "nominal",
              },
              value: "lightgray",
            },
            tooltip: [
              { field: "Model", type: "nominal" },
              { field: "Price", type: "quantitative" },
              { field: "HP", type: "quantitative" },
              { field: "MPG", type: "quantitative" },
              { field: "Weight", type: "quantitative" },
              { field: "Country", type: "nominal" },
            ],
          },
        },
        {
          title: "Weight vs. MPG",
          width: 400,
          height: 300,
          mark: { type: "circle", size: 60 },
          encoding: {
            x: { field: "Weight", type: "quantitative" },
            y: { field: "MPG", type: "quantitative" },
            color: {
              condition: {
                param: "brush",
                field: "Country",
                type: "nominal",
              },
              value: "lightgray",
            },
            tooltip: [
              { field: "Model", type: "nominal" },
              { field: "Price", type: "quantitative" },
              { field: "HP", type: "quantitative" },
              { field: "MPG", type: "quantitative" },
              { field: "Weight", type: "quantitative" },
              { field: "Country", type: "nominal" },
            ],
          },
        },
      ],
    };
  }, [rows]);

  if (error) {
    return (
      <p className="text-sm text-red-600" role="alert">
        Could not load chart data: {error}
      </p>
    );
  }
  if (rows.length === 0) {
    return <p className="text-sm text-[#718096]">Loading data…</p>;
  }

  return (
    <div className="min-w-0 overflow-x-auto">
      <VegaEmbed spec={spec} options={{ actions: false }} />
    </div>
  );
}
