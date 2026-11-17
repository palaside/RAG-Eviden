"use client";

import React, { useState, useEffect, useRef, useTransition } from "react";
import Link from "next/link";
import {
  Sliders,
  Code2,
  Eye,
  Copy,
  Check,
  Terminal,
  Shield,
  Sparkles,
  RotateCcw,
  Monitor,
  Tablet,
  Smartphone,
  Layers,
  ArrowLeft,
  Activity,
  AlertTriangle,
} from "lucide-react";
import {
  DEFAULT_UNIFIED_STATE,
  UnifiedState,
  RadiusToken,
} from "@/types/ui-studio";

export default function StudioPage() {
  const [state, setState] = useState<UnifiedState>(DEFAULT_UNIFIED_STATE);
  const [copied, setCopied] = useState(false);
  const [activeTab, setActiveTab] = useState<"tailwind" | "css" | "react">("tailwind");
  const [compiledCode, setCompiledCode] = useState<string>("");
  const [isPending, startTransition] = useTransition();
  const [renderLatencyMs, setRenderLatencyMs] = useState<number>(12);

  // Reference to the isolated sandbox viewport
  const sandboxRef = useRef<HTMLDivElement>(null);

  // Track 1: Immediate Direct DOM Injection (< 60ms)
  const injectStyleDirectly = (key: string, value: string) => {
    const start = performance.now();
    if (sandboxRef.current) {
      sandboxRef.current.style.setProperty(`--studio-${key}`, value);
    }
    const duration = Math.max(1, Math.round(performance.now() - start));
    setRenderLatencyMs(duration);
  };

  // Update State & Direct DOM Injection
  const handleRadiusChange = (radius: RadiusToken) => {
    setState((prev) => ({
      ...prev,
      designTokens: { ...prev.designTokens, radiusPx: radius },
    }));
    injectStyleDirectly("radius", `${radius}px`);
  };

  const handleBlurChange = (blur: number) => {
    setState((prev) => ({
      ...prev,
      designTokens: {
        ...prev.designTokens,
        effects: { ...prev.designTokens.effects, backdropBlurPx: blur },
      },
    }));
    injectStyleDirectly("blur", `${blur}px`);
  };

  const handleBorderWidthChange = (width: number) => {
    setState((prev) => ({
      ...prev,
      designTokens: {
        ...prev.designTokens,
        effects: { ...prev.designTokens.effects, hairlineBorderWidthPx: width },
      },
    }));
    injectStyleDirectly("border-width", `${width}px`);
  };

  const handleColorChange = (key: keyof UnifiedState["designTokens"]["palette"], color: string) => {
    setState((prev) => ({
      ...prev,
      designTokens: {
        ...prev.designTokens,
        palette: { ...prev.designTokens.palette, [key]: color },
      },
    }));
    injectStyleDirectly(key, color);
  };

  const handlePresetSelect = (preset: "TACTICAL" | "EXECUTIVE" | "DEEP_SPACE") => {
    if (preset === "TACTICAL") {
      setState((prev) => ({
        ...prev,
        contextPreset: { ...prev.contextPreset, toneAesthetic: "TACTICAL_NEO_BRUTALISM" },
        designTokens: {
          ...prev.designTokens,
          radiusPx: 0,
          palette: {
            ...prev.designTokens.palette,
            bgPrimary: "#121214",
            bgSurface: "#0b0c10",
            accentPrimary: "#ffb000",
            accentAlert: "#8b0000",
          },
          effects: { ...prev.designTokens.effects, backdropBlurPx: 16 },
        },
      }));
      injectStyleDirectly("radius", "0px");
      injectStyleDirectly("bgPrimary", "#121214");
      injectStyleDirectly("accentPrimary", "#ffb000");
    } else if (preset === "EXECUTIVE") {
      setState((prev) => ({
        ...prev,
        contextPreset: { ...prev.contextPreset, toneAesthetic: "EXECUTIVE_LUXURY" },
        designTokens: {
          ...prev.designTokens,
          radiusPx: 2,
          palette: {
            ...prev.designTokens.palette,
            bgPrimary: "#0d0e12",
            bgSurface: "#1a1d24",
            accentPrimary: "#d4af37",
            accentAlert: "#e63946",
          },
          effects: { ...prev.designTokens.effects, backdropBlurPx: 24 },
        },
      }));
      injectStyleDirectly("radius", "2px");
      injectStyleDirectly("bgPrimary", "#0d0e12");
      injectStyleDirectly("accentPrimary", "#d4af37");
    } else {
      setState((prev) => ({
        ...prev,
        contextPreset: { ...prev.contextPreset, toneAesthetic: "DEEP_SPACE_MINIMAL" },
        designTokens: {
          ...prev.designTokens,
          radiusPx: 4,
          palette: {
            ...prev.designTokens.palette,
            bgPrimary: "#050507",
            bgSurface: "#0d0e15",
            accentPrimary: "#00e5ff",
            accentAlert: "#ff0055",
          },
          effects: { ...prev.designTokens.effects, backdropBlurPx: 32 },
        },
      }));
      injectStyleDirectly("radius", "4px");
      injectStyleDirectly("bgPrimary", "#050507");
      injectStyleDirectly("accentPrimary", "#00e5ff");
    }
  };

  // Track 2: Throttled / Debounced AST Compiler Engine (150ms)
  useEffect(() => {
    const timer = setTimeout(() => {
      startTransition(() => {
        const radiusClass =
          state.designTokens.radiusPx === 0
            ? "rounded-none"
            : state.designTokens.radiusPx === 2
            ? "rounded-xs"
            : "rounded-sm";

        if (activeTab === "tailwind") {
          setCompiledCode(`<!-- Tactical 360° Component - Tailwind CSS v4 -->
<div className="relative p-6 ${radiusClass} border border-white/10 
  bg-[${state.designTokens.palette.bgSurface}]/80 
  backdrop-blur-[${state.designTokens.effects.backdropBlurPx}px] 
  shadow-2xl transition-all duration-150">
  <div className="flex items-center justify-between mb-4">
    <span className="text-[${state.designTokens.palette.accentPrimary}] font-mono text-xs uppercase tracking-wider">
      SYS.VERIFIED // 001
    </span>
    <span className="h-2 w-2 rounded-full bg-[${state.designTokens.palette.accentPrimary}] animate-pulse" />
  </div>
  <h3 className="text-lg font-bold text-white mb-2">Tactical Forensic Engine</h3>
  <p className="text-sm text-gray-400 font-sans">
    Evidence-backed execution pipeline with zero-lag dual track rendering.
  </p>
</div>`);
        } else if (activeTab === "css") {
          setCompiledCode(`/* Tactical 360° Design Tokens CSS */
:root {
  --studio-radius: ${state.designTokens.radiusPx}px;
  --studio-blur: ${state.designTokens.effects.backdropBlurPx}px;
  --studio-border: ${state.designTokens.effects.hairlineBorderWidthPx}px solid rgba(255, 255, 255, 0.1);
  --studio-bg: ${state.designTokens.palette.bgSurface};
  --studio-accent: ${state.designTokens.palette.accentPrimary};
}

.tactical-card {
  border-radius: var(--studio-radius);
  backdrop-filter: blur(var(--studio-blur));
  border: var(--studio-border);
  background-color: var(--studio-bg);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.6);
}`);
        } else {
          setCompiledCode(`// React 19 Production Component
import React from "react";

export function TacticalCard() {
  return (
    <div
      style={{
        borderRadius: "${state.designTokens.radiusPx}px",
        backdropFilter: "blur(${state.designTokens.effects.backdropBlurPx}px)",
        borderColor: "rgba(255, 255, 255, 0.1)",
        backgroundColor: "${state.designTokens.palette.bgSurface}",
      }}
      className="p-6 border shadow-2xl transition-all duration-150"
    >
      <div className="flex items-center justify-between mb-4">
        <span className="font-mono text-xs text-[${state.designTokens.palette.accentPrimary}]">
          STATION // ACTIVE
        </span>
      </div>
      <h3 className="font-bold text-white">Forensic Evidence Container</h3>
    </div>
  );
}`);
        }
      });
    }, 150);

    return () => clearTimeout(timer);
  }, [state, activeTab]);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(compiledCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="flex flex-col h-screen w-screen bg-[#0b0c10] text-[#f0f2f5] font-sans overflow-hidden select-none">
      {/* Top Navigation Bar */}
      <header className="h-12 border-b border-white/10 bg-[#121214]/90 backdrop-blur-md px-4 flex items-center justify-between flex-shrink-0 z-20">
        <div className="flex items-center gap-3">
          <Link
            href="/"
            className="flex items-center gap-2 text-xs font-mono text-gray-400 hover:text-white transition-colors"
          >
            <ArrowLeft className="w-3.5 h-3.5" /> Back
          </Link>
          <div className="h-4 w-px bg-white/10" />
          <div className="flex items-center gap-2">
            <Shield className="w-4 h-4 text-[#ffb000]" />
            <h1 className="text-sm font-bold tracking-tight text-white flex items-center gap-2">
              Tactical UI Studio 360°
              <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-white/5 border border-white/10 text-gray-400">
                Next.js 16
              </span>
            </h1>
          </div>
        </div>

        {/* Viewport Breakpoint Switcher */}
        <div className="flex items-center bg-black/40 rounded border border-white/10 p-0.5 gap-1">
          <button
            onClick={() => setState((prev) => ({ ...prev, metaSession: { ...prev.metaSession, activeBreakpoint: "DESKTOP" } }))}
            className={`p-1.5 rounded transition-colors ${state.metaSession.activeBreakpoint === "DESKTOP" ? "bg-white/10 text-[#00e5ff]" : "text-gray-400 hover:text-white"}`}
            title="Desktop 100%"
          >
            <Monitor className="w-3.5 h-3.5" />
          </button>
          <button
            onClick={() => setState((prev) => ({ ...prev, metaSession: { ...prev.metaSession, activeBreakpoint: "TABLET" } }))}
            className={`p-1.5 rounded transition-colors ${state.metaSession.activeBreakpoint === "TABLET" ? "bg-white/10 text-[#00e5ff]" : "text-gray-400 hover:text-white"}`}
            title="Tablet 768px"
          >
            <Tablet className="w-3.5 h-3.5" />
          </button>
          <button
            onClick={() => setState((prev) => ({ ...prev, metaSession: { ...prev.metaSession, activeBreakpoint: "MOBILE" } }))}
            className={`p-1.5 rounded transition-colors ${state.metaSession.activeBreakpoint === "MOBILE" ? "bg-white/10 text-[#00e5ff]" : "text-gray-400 hover:text-white"}`}
            title="Mobile 375px"
          >
            <Smartphone className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* Telemetry Indicator */}
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-1.5 font-mono text-[11px] text-emerald-400 bg-emerald-950/40 border border-emerald-500/20 px-2 py-0.5 rounded">
            <Activity className="w-3 h-3 animate-pulse" />
            <span>Track 1: {renderLatencyMs}ms (60 FPS)</span>
          </div>
          <button
            onClick={() => handlePresetSelect("TACTICAL")}
            className="text-xs font-mono text-gray-400 hover:text-white transition-colors flex items-center gap-1"
          >
            <RotateCcw className="w-3 h-3" /> Reset
          </button>
        </div>
      </header>

      {/* Main 3-Column Studio Workspace */}
      <div className="flex-1 grid grid-cols-[350px_1fr_420px] overflow-hidden">
        {/* ========================================================================= */}
        {/* Left Panel: Controller (350px) */}
        {/* ========================================================================= */}
        <aside className="border-r border-white/10 bg-[#121214]/60 backdrop-blur-sm overflow-y-auto p-4 flex flex-col gap-6 text-xs">
          {/* Aesthetic Presets */}
          <div className="flex flex-col gap-2">
            <label className="font-mono text-gray-400 uppercase tracking-wider text-[10px] flex items-center gap-1.5">
              <Sparkles className="w-3 h-3 text-[#ffb000]" /> Tone & Aesthetic Presets
            </label>
            <div className="grid grid-cols-3 gap-1.5">
              <button
                onClick={() => handlePresetSelect("TACTICAL")}
                className={`py-2 px-1 text-center font-bold rounded text-[11px] border transition-all ${
                  state.contextPreset.toneAesthetic === "TACTICAL_NEO_BRUTALISM"
                    ? "bg-[#ffb000]/10 border-[#ffb000] text-[#ffb000]"
                    : "bg-white/5 border-white/10 text-gray-400 hover:text-white"
                }`}
              >
                Tactical
              </button>
              <button
                onClick={() => handlePresetSelect("EXECUTIVE")}
                className={`py-2 px-1 text-center font-bold rounded text-[11px] border transition-all ${
                  state.contextPreset.toneAesthetic === "EXECUTIVE_LUXURY"
                    ? "bg-[#d4af37]/10 border-[#d4af37] text-[#d4af37]"
                    : "bg-white/5 border-white/10 text-gray-400 hover:text-white"
                }`}
              >
                Luxury
              </button>
              <button
                onClick={() => handlePresetSelect("DEEP_SPACE")}
                className={`py-2 px-1 text-center font-bold rounded text-[11px] border transition-all ${
                  state.contextPreset.toneAesthetic === "DEEP_SPACE_MINIMAL"
                    ? "bg-[#00e5ff]/10 border-[#00e5ff] text-[#00e5ff]"
                    : "bg-white/5 border-white/10 text-gray-400 hover:text-white"
                }`}
              >
                Deep Space
              </button>
            </div>
          </div>

          {/* Strict Radius Limit (0px, 2px, 4px) */}
          <div className="flex flex-col gap-2">
            <div className="flex justify-between items-center font-mono text-[10px] text-gray-400 uppercase tracking-wider">
              <span>Strict Radius Limit (Max 4px)</span>
              <span className="text-[#00e5ff] font-mono">{state.designTokens.radiusPx}px</span>
            </div>
            <div className="grid grid-cols-3 gap-2">
              {[0, 2, 4].map((rad) => (
                <button
                  key={rad}
                  onClick={() => handleRadiusChange(rad as RadiusToken)}
                  className={`py-2 text-center font-mono text-xs rounded border transition-all ${
                    state.designTokens.radiusPx === rad
                      ? "bg-white/15 border-white text-white font-bold"
                      : "bg-white/5 border-white/10 text-gray-400 hover:text-white"
                  }`}
                >
                  {rad}px {rad === 0 ? "(None)" : rad === 2 ? "(Critical)" : "(Max)"}
                </button>
              ))}
            </div>
          </div>

          {/* Backdrop Blur Slider */}
          <div className="flex flex-col gap-2">
            <div className="flex justify-between items-center font-mono text-[10px] text-gray-400 uppercase tracking-wider">
              <span>Backdrop Blur</span>
              <span className="text-[#00e5ff] font-mono">{state.designTokens.effects.backdropBlurPx}px</span>
            </div>
            <input
              type="range"
              min="0"
              max="48"
              step="4"
              value={state.designTokens.effects.backdropBlurPx}
              onChange={(e) => handleBlurChange(parseInt(e.target.value, 10))}
              className="w-full accent-[#ffb000] cursor-pointer"
            />
          </div>

          {/* Hairline Border Width */}
          <div className="flex flex-col gap-2">
            <div className="flex justify-between items-center font-mono text-[10px] text-gray-400 uppercase tracking-wider">
              <span>Hairline Border Width</span>
              <span className="text-[#00e5ff] font-mono">{state.designTokens.effects.hairlineBorderWidthPx}px</span>
            </div>
            <div className="grid grid-cols-3 gap-2">
              {[0.5, 1, 2].map((w) => (
                <button
                  key={w}
                  onClick={() => handleBorderWidthChange(w)}
                  className={`py-1.5 text-center font-mono text-xs rounded border transition-all ${
                    state.designTokens.effects.hairlineBorderWidthPx === w
                      ? "bg-white/15 border-white text-white font-bold"
                      : "bg-white/5 border-white/10 text-gray-400 hover:text-white"
                  }`}
                >
                  {w}px
                </button>
              ))}
            </div>
          </div>

          {/* Color Palette Controls */}
          <div className="flex flex-col gap-3 border-t border-white/10 pt-4">
            <label className="font-mono text-gray-400 uppercase tracking-wider text-[10px]">
              Color Palette Tokens
            </label>
            <div className="grid grid-cols-2 gap-3">
              <div className="flex items-center gap-2">
                <input
                  type="color"
                  value={state.designTokens.palette.bgSurface}
                  onChange={(e) => handleColorChange("bgSurface", e.target.value)}
                  className="w-7 h-7 rounded border border-white/20 bg-transparent cursor-pointer"
                />
                <span className="font-mono text-[11px] text-gray-300">Surface</span>
              </div>
              <div className="flex items-center gap-2">
                <input
                  type="color"
                  value={state.designTokens.palette.accentPrimary}
                  onChange={(e) => handleColorChange("accentPrimary", e.target.value)}
                  className="w-7 h-7 rounded border border-white/20 bg-transparent cursor-pointer"
                />
                <span className="font-mono text-[11px] text-gray-300">Accent</span>
              </div>
            </div>
          </div>
        </aside>

        {/* ========================================================================= */}
        {/* Center Panel: Live Isolated Sandbox (1fr) */}
        {/* ========================================================================= */}
        <main className="bg-[#08090c] relative flex items-center justify-center p-8 overflow-hidden">
          {/* Tactical Background Grid Pattern */}
          <div
            className="absolute inset-0 opacity-15 pointer-events-none"
            style={{
              backgroundImage:
                "linear-gradient(to right, rgba(255,255,255,0.08) 1px, transparent 1px), linear-gradient(to bottom, rgba(255,255,255,0.08) 1px, transparent 1px)",
              backgroundSize: "24px 24px",
            }}
          />

          {/* Dynamic Sandbox Viewport Container */}
          <div
            ref={sandboxRef}
            style={{
              width:
                state.metaSession.activeBreakpoint === "DESKTOP"
                  ? "600px"
                  : state.metaSession.activeBreakpoint === "TABLET"
                  ? "480px"
                  : "340px",
              borderRadius: `${state.designTokens.radiusPx}px`,
              backdropFilter: `blur(${state.designTokens.effects.backdropBlurPx}px)`,
              borderWidth: `${state.designTokens.effects.hairlineBorderWidthPx}px`,
              borderColor: "rgba(255, 255, 255, 0.12)",
              backgroundColor: `${state.designTokens.palette.bgSurface}`,
            }}
            className="relative p-6 border shadow-2xl transition-all duration-150 flex flex-col gap-4 text-white z-10"
          >
            {/* Header Badge */}
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span
                  style={{ color: state.designTokens.palette.accentPrimary }}
                  className="font-mono text-xs uppercase tracking-wider font-bold"
                >
                  SYSTEM.EVIDENCE // VERIFIED
                </span>
              </div>
              <span
                style={{ backgroundColor: state.designTokens.palette.accentPrimary }}
                className="w-2.5 h-2.5 rounded-full animate-ping"
              />
            </div>

            <div>
              <h2 className="text-lg font-bold tracking-tight text-white mb-1">
                Forensic Evidence Container
              </h2>
              <p className="text-xs text-gray-400 font-sans leading-relaxed">
                Direct DOM injection active. All numerical telemetry follows strict anti-displacement monospace discipline.
              </p>
            </div>

            {/* Mock Telemetry Stats */}
            <div className="grid grid-cols-2 gap-3 pt-2">
              <div className="p-3 bg-black/40 rounded border border-white/5 flex flex-col gap-1">
                <span className="text-[10px] font-mono text-gray-400 uppercase">Latency (Track 1)</span>
                <span className="text-base font-mono font-bold text-emerald-400">{renderLatencyMs} ms</span>
              </div>
              <div className="p-3 bg-black/40 rounded border border-white/5 flex flex-col gap-1">
                <span className="text-[10px] font-mono text-gray-400 uppercase">CLS Rating</span>
                <span className="text-base font-mono font-bold text-[#00e5ff]">0.000 (Target)</span>
              </div>
            </div>

            {/* Action Button */}
            <button
              style={{
                borderRadius: `${state.designTokens.radiusPx}px`,
                backgroundColor: state.designTokens.palette.accentPrimary,
              }}
              className="w-full py-2.5 text-black font-bold text-xs uppercase tracking-wider hover:opacity-90 transition-opacity mt-2"
            >
              Confirm Transaction
            </button>
          </div>
        </main>

        {/* ========================================================================= */}
        {/* Right Panel: Live Terminal Code Stream (420px) */}
        {/* ========================================================================= */}
        <aside className="border-l border-white/10 bg-[#0c0d11] flex flex-col overflow-hidden">
          {/* Header Tabs */}
          <div className="h-10 border-b border-white/10 bg-black/40 px-3 flex items-center justify-between flex-shrink-0">
            <div className="flex items-center gap-1">
              <Terminal className="w-3.5 h-3.5 text-gray-400" />
              <span className="font-mono text-xs text-gray-300">Live AST Stream</span>
            </div>
            <div className="flex items-center gap-1 bg-white/5 p-0.5 rounded border border-white/10 text-[10px] font-mono">
              <button
                onClick={() => setActiveTab("tailwind")}
                className={`px-2 py-0.5 rounded ${activeTab === "tailwind" ? "bg-white/10 text-[#ffb000] font-bold" : "text-gray-400 hover:text-white"}`}
              >
                Tailwind v4
              </button>
              <button
                onClick={() => setActiveTab("css")}
                className={`px-2 py-0.5 rounded ${activeTab === "css" ? "bg-white/10 text-[#ffb000] font-bold" : "text-gray-400 hover:text-white"}`}
              >
                CSS
              </button>
              <button
                onClick={() => setActiveTab("react")}
                className={`px-2 py-0.5 rounded ${activeTab === "react" ? "bg-white/10 text-[#ffb000] font-bold" : "text-gray-400 hover:text-white"}`}
              >
                React TSX
              </button>
            </div>
          </div>

          {/* Terminal Code Viewer */}
          <div className="flex-1 p-4 overflow-auto font-mono text-xs leading-relaxed text-emerald-400 bg-[#050608]">
            <pre className="whitespace-pre-wrap word-break">{compiledCode}</pre>
          </div>

          {/* Copy Button Footer */}
          <div className="p-3 border-t border-white/10 bg-[#0f1015] flex items-center justify-between">
            <span className="text-[10px] font-mono text-gray-400">
              Debounce: 150ms // Zero CPU Freeze
            </span>
            <button
              onClick={copyToClipboard}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded bg-white/10 hover:bg-white/15 text-white font-mono text-xs transition-colors border border-white/10"
            >
              {copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
              <span>{copied ? "Copied!" : "Copy Code"}</span>
            </button>
          </div>
        </aside>
      </div>
    </div>
  );
}

