"use client";

import React, { useState } from "react";
import EngineStarter from "./ui/EngineStarter";
import Link from "next/link";
import {
  Zap,
  Bot,
  Ruler,
  Users2,
  Stethoscope,
  Terminal,
  ShieldCheck,
  Sliders,
  Copy,
  Check,
  Sparkles,
  ExternalLink,
  ChevronRight,
  Database,
  Layers,
  FileCode2,
  Activity,
  ArrowRight,
  HelpCircle,
  X,
} from "lucide-react";

type EngineMode = "SDLC" | "ADLC" | "SDD" | "SWARM" | "HEALING";

interface ModeConfig {
  id: EngineMode;
  name: string;
  tag: string;
  icon: typeof Zap;
  color: string;
  borderColor: string;
  bgGlow: string;
  title: string;
  desc: string;
  steps: { num: string; title: string; desc: string; samplePrompt: string }[];
}

const ENGINE_MODES: Record<EngineMode, ModeConfig> = {
  SDLC: {
    id: "SDLC",
    name: "1. SDLC Vibe",
    tag: "Human-in-the-Lead",
    icon: Zap,
    color: "#38bdf8",
    borderColor: "rgba(56, 189, 248, 0.4)",
    bgGlow: "rgba(56, 189, 248, 0.15)",
    title: "Vibe Code SDLC Workflow",
    desc: "Spec-Driven Development with AI Copilot — มนุษย์นำยุทธศาสตร์ AI เป็นคู่คิด ปรับแต่งรวดเร็ว",
    steps: [
      {
        num: "01",
        title: "Intent & Inception",
        desc: "ป้อนไอเดียและวิสัยทัศน์เริ่มต้นให้ AI",
        samplePrompt: "เป้าหมาย: ฉันต้องการสร้างระบบ [ระบุชื่อระบบ] ที่แก้ปัญหา [ระบุปัญหา] ช่วยถามเจาะลึก 4 ด้านแบบ Grill-me ก่อนเริ่มเขียนโค้ด",
      },
      {
        num: "02",
        title: "Blueprint Co-Design",
        desc: "ร่างสถาปัตยกรรมและ Schema ร่วมกัน",
        samplePrompt: "กรุณาสังเคราะห์สถาปัตยกรรมตาม structure/ และออก SYSTEM_BLUEPRINT.md พร้อมผัง Mermaid แสดง Data Flow",
      },
      {
        num: "03",
        title: "Vertical Build",
        desc: "พัฒนาทีละโมดูลแบบมีมนุษย์คุม Gate",
        samplePrompt: "เขียนโค้ดโมดูลแรกตามหลัก 1 Test : 1 Implementation ห้ามใช้ any และทดสอบ Vitest ให้ผ่านก่อนทำโมดูลถัดไป",
      },
      {
        num: "04",
        title: "Vibe & Polish",
        desc: "ขัดเกลา UI และพรีวิวสดใน Tactical Studio",
        samplePrompt: "เปิดหน้า Tactical UI Studio ปรับแต่ง Tokens ให้เป็น Tactical Neo-Brutalism แล้วส่งออกโค้ด Tailwind v4",
      },
    ],
  },
  ADLC: {
    id: "ADLC",
    name: "2. ADLC Engine",
    tag: "Agent Autonomous",
    icon: Bot,
    color: "#a855f7",
    borderColor: "rgba(168, 85, 247, 0.4)",
    bgGlow: "rgba(168, 85, 247, 0.15)",
    title: "Autonomous Agent Development Lifecycle",
    desc: "ให้ AI ดำเนินการเอง 100% ตั้งแต่ล็อกแผนงาน ➔ แตก Task ➔ เขียน TDD ➔ รันเทสต์อัตโนมัติ",
    steps: [
      {
        num: "01",
        title: "Knowledge Hydration",
        desc: "ดึงบริบทจาก 4 คลังความรู้แม่บท",
        samplePrompt: "อ่าน BRAIN.md และ SOVEREIGN.md เตรียมพร้อมรัน ADLC Engine ภายใต้ Token Budget Tier M",
      },
      {
        num: "02",
        title: "Single Task Lock",
        desc: "ล็อกงานลงใน STATE.md ทีละข้อ",
        samplePrompt: "แตกงานเป็น Atomic Vertical Slices และบันทึกลง STATE.md พร้อมเปิดใช้งาน Single Active Task Lock",
      },
      {
        num: "03",
        title: "TDD Vertical Slice",
        desc: "ลูปเขียนเทสต์คู่โค้ดผ่าน Vitest",
        samplePrompt: "รันวงจร red_green พัฒนาฟังก์ชันพร้อมทดสอบ Exit Code 0 เมื่อครบ 50% ให้หยุด Compact โค้ด",
      },
      {
        num: "04",
        title: "Audit & Deploy",
        desc: "ตรวจรับอัตโนมัติด้วย npm run audit",
        samplePrompt: "รันสคริปต์ npm run audit และ npx tsc --noEmit เพื่อพิสูจน์ผล 100% ก่อนส่งมอบงาน",
      },
    ],
  },
  SDD: {
    id: "SDD",
    name: "3. Spec-Driven",
    tag: "Schema is King",
    icon: Ruler,
    color: "#10b981",
    borderColor: "rgba(16, 185, 129, 0.4)",
    bgGlow: "rgba(16, 185, 129, 0.15)",
    title: "Spec-Driven Development (SDD)",
    desc: "สเปกคือพระเจ้า — ตัดปัญหา AI มโนโค้ด ด้วยการล็อก Zod Schemas และ DB Contracts ก่อนแตะต้อง Logic",
    steps: [
      {
        num: "01",
        title: "Schema First",
        desc: "นิยาม Zod Types และ Drizzle Model",
        samplePrompt: "นิยาม Zod Schemas และ Drizzle Table พร้อม Optimistic Lock (version) ใน src/db/schema.ts ห้ามใช้ any",
      },
      {
        num: "02",
        title: "API Envelope",
        desc: "ล็อกกล่องรับส่งข้อมูล Universal Format",
        samplePrompt: "ออกแบบ Route Handler ตามมาตรฐาน Fast/REST API Envelope { success, data, error, meta }",
      },
      {
        num: "03",
        title: "Compile to Code",
        desc: "คอมไพล์สเปกสู่ฟังก์ชันแบบ 1:1",
        samplePrompt: "นำ Zod Schema มาสร้าง Service Layer ตรวจสอบ Input Validation 100% ก่อนบันทึกลงฐานข้อมูล",
      },
      {
        num: "04",
        title: "Contract Verification",
        desc: "ทดสอบการรับส่งข้อมูลตามสัญญา",
        samplePrompt: "รัน Integration Test ยิง Request ด้วยข้อมูล Malformed เพื่อพิสูจน์ว่า Zod Interceptor ดักจับได้สมบูรณ์",
      },
    ],
  },
  SWARM: {
    id: "SWARM",
    name: "4. Agent Swarm",
    tag: "Maker vs Checker",
    icon: Users2,
    color: "#f59e0b",
    borderColor: "rgba(245, 158, 11, 0.4)",
    bgGlow: "rgba(245, 158, 11, 0.15)",
    title: "Multi-Agent Swarm & Maker-Checker",
    desc: "แยก 2 ขั้วคานอำนาจ: คนเขียนโค้ด (Maker) ⇄ คนตรวจจับผิด (Checker QA) ป้องกัน AI หลอกตัวเอง",
    steps: [
      {
        num: "01",
        title: "Architect Brief",
        desc: "Root Architect ออกสัญญากลาง",
        samplePrompt: "สวมหมวก Root Architect Mode ตรวจสอบ Invariant Shield และอนุมัติ Scope Lock ก่อนเริ่มงาน",
      },
      {
        num: "02",
        title: "Maker Execution",
        desc: "Cheat Code Dev พัฒนาด้วยสปีด 10x",
        samplePrompt: "สวมหมวก Cheat Code Mode ลงมือเขียน Minimal Surgical Diff เฉพาะบรรทัดที่จำเป็นตาม YAGNI",
      },
      {
        num: "03",
        title: "Checker Audit",
        desc: "Tech Lead QA ตรวจจับผิด 4 ระดับ",
        samplePrompt: "สวมหมวก Tech Lead Mode ตรวจสอบโค้ดตามเช็กลิสต์ 4-Tier Code Review และตรวจสอบหา Regression",
      },
      {
        num: "04",
        title: "Circuit Breaker",
        desc: "คุมลูปวนซ่อมไม่เกิน 3 ครั้ง",
        samplePrompt: "หาก Maker แก้ไม่ผ่านรอบที่ 3 ให้ตัดวงจร Circuit Breaker ทันที และรายงาน Root Cause เพื่อ Escalate",
      },
    ],
  },
  HEALING: {
    id: "HEALING",
    name: "5. Self-Healing",
    tag: "5-Whys Diagnostics",
    icon: Stethoscope,
    color: "#ef4444",
    borderColor: "rgba(239, 68, 68, 0.4)",
    bgGlow: "rgba(239, 68, 68, 0.15)",
    title: "Self-Healing & Forensic Telemetry",
    desc: "แพทย์ผ่าตัดซ่อมสด — วินิจฉัยรากเหง้าด้วย 5-Whys RCA และออกแพตช์ถาวร ป้องกันเกิดซ้ำ 100%",
    steps: [
      {
        num: "01",
        title: "Error Intake",
        desc: "ดึง Stderr และ Stack Trace รันไทม์จริง",
        samplePrompt: "นำ Error Log นี้ไปวิเคราะห์: [วาง Log] ห้ามเดาเอง ให้ตรวจสอบไฟล์โค้ดจริงที่เกี่ยวข้อง",
      },
      {
        num: "02",
        title: "5-Whys RCA",
        desc: "ขุดลึกหารากเหง้าโครงสร้าง 5 ชั้น",
        samplePrompt: "ทำตรรกะ 5-Whys Diagnostic Drill-Down แยกแยะระหว่างอาการภายนอกกับต้นตอแท้จริง",
      },
      {
        num: "03",
        title: "Surgical Patch",
        desc: "ลงมือผ่าตัดเฉพาะจุดที่พัง",
        samplePrompt: "เขียนโค้ดผ่าตัดแก้ไขถาวร ห้ามใช้วิธีแปะพลาสเตอร์ชั่วคราว และสร้าง Unit Test ป้องกันบั๊กนี้กลับมา",
      },
      {
        num: "04",
        title: "Proof & Green",
        desc: "รันคำสอบยืนยัน Exit Code 0",
        samplePrompt: "รันชุดทดสอบที่เคยพังซ้ำอีกครั้ง แสดงผลลัพธ์ Exit Code 0 และบันทึกลง LATEST_CHECKPOINT.md",
      },
    ],
  },
};

export default function HomePage() {
  const [currentMode, setCurrentMode] = useState<EngineMode>("SDLC");
  const [activeStepIndex, setActiveStepIndex] = useState<number>(0);
  const [userIdea, setUserIdea] = useState<string>("");
  const [generatedPrompt, setGeneratedPrompt] = useState<string>("");
  const [copied, setCopied] = useState<boolean>(false);
  const [isGuideOpen, setIsGuideOpen] = useState<boolean>(false);
  const [adlcRunning, setAdlcRunning] = useState<boolean>(false);
  const [adlcStep, setAdlcStep] = useState<number>(0);

  const activeMode = ENGINE_MODES[currentMode];
  const activeStep = activeMode.steps[activeStepIndex] || activeMode.steps[0];

  const runAdlcSimulation = () => {
    setAdlcRunning(true);
    setAdlcStep(1);
    const intervals = [800, 1600, 2400, 3200, 4000, 4800];
    intervals.forEach((delay, idx) => {
      setTimeout(() => {
        setAdlcStep(idx + 1);
        if (idx === intervals.length - 1) {
          setTimeout(() => setAdlcRunning(false), 1000);
        }
      }, delay);
    });
  };

  const handleGeneratePrompt = () => {
    const ideaText = userIdea.trim() || "ระบบวิเคราะห์และตรวจสอบพยานหลักฐานดิจิทัลคดีอาญา";
    const prompt = `[คำสั่งเริ่มโหมด ${activeMode.name}]
เป้าหมายของฉัน: ${ideaText}

กรุณาเริ่มปฏิบัติการตามสายพานใน BRAIN.md ทันที:
1. สวมบทบาทเป็น Lead Architect ซักถามฉัน 4 ด้าน (Core, Data Flow, Tech Stack, Edge Cases) ตามหลัก Grill-Me
2. เมื่อฉันตอบครบ ให้ออก SYSTEM_BLUEPRINT.md โดยอ้างอิงมาตรฐานจาก structure/ และ SPECIFICATION TEMPLATE/
3. แตกเป็น Atomic Tasks ล็อกลงใน STATE.md และพาทำทีละโมดูลแบบ 1 Test : 1 Implementation
4. คุมคุณภาพด้วย ENGINEERING EXECUTION POLICY และตัดวงจรลูปไม่เกิน 3 ครั้ง

พร้อมแล้ว เริ่มคำถามชุดแรกได้เลย!`;
    setGeneratedPrompt(prompt);
  };

  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="min-h-screen w-full bg-[#0a0e17] text-[#f8fafc] font-sans flex flex-col relative overflow-x-hidden selection:bg-[#38bdf8]/30 selection:text-white">
      {/* Ambient Radial Glowing Background Layer */}
      <div className="fixed inset-0 pointer-events-none z-0">
        <div
          className="absolute top-[-10%] left-[-5%] w-[600px] h-[600px] rounded-full blur-[140px] opacity-25 transition-all duration-700"
          style={{ backgroundColor: activeMode.color }}
        />
        <div className="absolute bottom-[-10%] right-[-5%] w-[550px] h-[550px] rounded-full blur-[140px] opacity-20 bg-purple-600" />
        <div className="absolute top-[40%] left-[30%] w-[450px] h-[450px] rounded-full blur-[160px] opacity-15 bg-emerald-600" />
      </div>

      {/* Top Hub Navigation Bar */}
      <nav className="h-12 border-b border-white/10 bg-[#0f172a]/80 backdrop-blur-md px-6 flex items-center justify-between z-20 text-xs">
        <div className="flex items-center gap-3">
          <span className="font-mono font-bold tracking-widest text-[#38bdf8] flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-[#38bdf8] animate-pulse" />
            iAMor FAMILY // SOVEREIGN HUB
          </span>
          <div className="h-3 w-px bg-white/15" />
          <span className="font-mono text-gray-400 text-[11px] hidden sm:inline">
            SDLC 5-in-1 Master Architecture Active
          </span>
        </div>

        <div className="flex items-center gap-3">
          <Link
            href="/chawakom"
            className="flex items-center gap-1.5 px-3 py-1 rounded bg-sky-500/10 hover:bg-sky-500/20 text-sky-400 border border-sky-500/30 font-mono font-bold text-xs transition-all hover:scale-105"
          >
            <Layers className="w-3.5 h-3.5" />
            <span>ชวกม.7 Platform</span>
          </Link>
          <Link
            href="/studio"
            className="flex items-center gap-1.5 px-3 py-1 rounded bg-[#ffb000]/10 hover:bg-[#ffb000]/20 text-[#ffb000] border border-[#ffb000]/30 font-mono font-bold text-xs transition-all hover:scale-105"
          >
            <Sliders className="w-3.5 h-3.5" />
            <span>Launch UI Studio 360°</span>
          </Link>
          <button
            onClick={() => setIsGuideOpen(true)}
            className="flex items-center gap-1 text-gray-400 hover:text-white transition-colors"
          >
            <HelpCircle className="w-4 h-4" />
            <span className="hidden sm:inline">คู่มือ 5 โหมด</span>
          </button>
        </div>
      </nav>

      {/* Main Header & 5-Mode Switcher */}
      <header className="border-b border-white/10 bg-[#121826]/85 backdrop-blur-xl px-6 py-4 z-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div className="flex items-center gap-3.5">
          <div
            className="w-11 h-11 rounded-xl flex items-center justify-center border transition-all duration-300 shadow-lg"
            style={{
              backgroundColor: activeMode.bgGlow,
              borderColor: activeMode.borderColor,
              color: activeMode.color,
            }}
          >
            <activeMode.icon className="w-6 h-6" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-xl font-extrabold tracking-tight text-white">
                {activeMode.title}
              </h1>
              <span
                className="text-[10px] font-mono px-2 py-0.5 rounded-full border uppercase tracking-wider font-bold"
                style={{
                  backgroundColor: activeMode.bgGlow,
                  borderColor: activeMode.borderColor,
                  color: activeMode.color,
                }}
              >
                {activeMode.tag}
              </span>
            </div>
            <p className="text-xs text-gray-400 mt-0.5">{activeMode.desc}</p>
          </div>
        </div>

        {/* 5 Distinct Mode Switcher Pills */}
        <div className="flex items-center bg-black/40 p-1 rounded-xl border border-white/10 gap-1 overflow-x-auto max-w-full">
          {(Object.keys(ENGINE_MODES) as EngineMode[]).map((modeKey) => {
            const m = ENGINE_MODES[modeKey];
            const isActive = currentMode === modeKey;
            const IconComponent = m.icon;
            return (
              <button
                key={modeKey}
                onClick={() => {
                  setCurrentMode(modeKey);
                  setActiveStepIndex(0);
                }}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all whitespace-nowrap ${
                  isActive
                    ? "shadow-md scale-102"
                    : "text-gray-400 hover:text-white hover:bg-white/5"
                }`}
                style={
                  isActive
                    ? {
                        backgroundColor: m.bgGlow,
                        borderColor: m.borderColor,
                        color: m.color,
                        borderWidth: "1px",
                      }
                    : {}
                }
              >
                <IconComponent className="w-3.5 h-3.5" />
                <span>{m.name}</span>
              </button>
            );
          })}
        </div>
      </header>

      {/* Main Content Viewport */}
      <main className="flex-1 px-6 py-6 z-10 flex flex-col gap-6 max-w-7xl w-full mx-auto">
        {/* Stepper Progress Flow */}
        <div className="bg-[#121826]/75 backdrop-blur-xl border border-white/10 rounded-2xl p-3 flex gap-2 overflow-x-auto shadow-xl">
          {activeMode.steps.map((st: { num: string; title: string; desc: string; samplePrompt: string }, idx: number) => {
            const isCurrent = idx === activeStepIndex;
            return (
              <button
                key={st.num}
                onClick={() => setActiveStepIndex(idx)}
                className={`flex-1 min-w-[170px] p-3 rounded-xl border text-left transition-all flex flex-col gap-1 ${
                  isCurrent
                    ? "bg-white/10 shadow-lg scale-[1.01]"
                    : "bg-white/[0.02] border-transparent hover:bg-white/5 opacity-70 hover:opacity-100"
                }`}
                style={
                  isCurrent
                    ? {
                        borderColor: activeMode.color,
                        boxShadow: `0 0 20px ${activeMode.bgGlow}`,
                      }
                    : {}
                }
              >
                <span
                  className="font-mono text-[10px] uppercase font-bold"
                  style={{ color: isCurrent ? activeMode.color : "#94a3b8" }}
                >
                  Step {st.num}
                </span>
                <span className="text-xs font-bold text-white">{st.title}</span>
                <span className="text-[11px] text-gray-400 line-clamp-1">{st.desc}</span>
              </button>
            );
          })}
        </div>

        {/* The Sovereign Interactive Command Center */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          {/* Left Column: Interactive Reverse-Prompt Engine (7 Cols) */}
          <section className="lg:col-span-7 bg-[#121826]/80 backdrop-blur-2xl border border-white/10 rounded-2xl p-6 shadow-2xl flex flex-col gap-5">
            <div className="flex items-center justify-between border-b border-white/10 pb-4">
              <div className="flex items-center gap-2">
                <Sparkles className="w-5 h-5 text-[#ffb000]" />
                <h2 className="text-base font-bold text-white">
                  Reverse Prompt Generator (Grill-Me System)
                </h2>
              </div>
              <span className="font-mono text-[11px] text-gray-400">
                BRAIN.md Powered // 7-Step Circuit
              </span>
            </div>

            {/* Input Box for User's Raw Idea */}
            <div className="flex flex-col gap-2">
              <label className="text-xs font-bold text-gray-300">
                💡 ระบุเป้าหมาย หรือระบบที่คุณต้องการสร้าง (เพียง 1 ประโยค):
              </label>
              <textarea
                value={userIdea}
                onChange={(e) => setUserIdea(e.target.value)}
                placeholder="เช่น: ต้องการทำระบบตรวจสอบสลิปโอนเงินคดีอาญา ที่มี OCR ถอดชื่อ ยอดเงิน วันที่ และจัดหน้าสลิปลง A4 ส่งศาล..."
                className="w-full h-24 bg-black/50 border border-white/15 rounded-xl p-3 text-sm text-white placeholder-gray-500 focus:outline-none focus:border-[#38bdf8] focus:ring-1 focus:ring-[#38bdf8] transition-all resize-none font-sans"
              />
            </div>

            {/* Trigger Button */}
            <div className="flex items-center gap-3">
              <button
                onClick={handleGeneratePrompt}
                className="flex-1 py-3 px-4 rounded-xl font-bold text-xs uppercase tracking-wider text-black flex items-center justify-center gap-2 shadow-lg transition-transform hover:scale-[1.02] active:scale-[0.98]"
                style={{ backgroundColor: activeMode.color }}
              >
                <Zap className="w-4 h-4 fill-black" />
                <span>สังเคราะห์ Prompt เริ่มโหมด {activeMode.name}</span>
              </button>
              {currentMode === "ADLC" && (
                <button
                  onClick={runAdlcSimulation}
                  disabled={adlcRunning}
                  className="py-3 px-4 rounded-xl font-bold text-xs uppercase tracking-wider bg-purple-600/30 border border-purple-500/50 hover:bg-purple-600/50 text-white flex items-center gap-2 shadow-lg transition-all"
                >
                  <Bot className={`w-4 h-4 ${adlcRunning ? "animate-spin" : ""}`} />
                  <span>{adlcRunning ? `Running Gate ${adlcStep}/6...` : "⚡ Simulate ADLC 6 Gates"}</span>
                </button>
              )}
            </div>

            {/* Live ADLC Pipeline Progress Bar (when ADLC is active or running) */}
            {currentMode === "ADLC" && (
              <div className="bg-[#050810] border border-purple-500/30 rounded-xl p-3 flex flex-col gap-2">
                <div className="flex justify-between items-center text-[11px] font-mono">
                  <span className="text-purple-400 font-bold flex items-center gap-1.5">
                    <Bot className="w-3.5 h-3.5" />
                    <span>ADLC Autonomous Pipeline Verification:</span>
                  </span>
                  <span className="text-gray-400">
                    {adlcStep === 6 ? "🏆 ALL 6 GATES VERIFIED 100%" : `Gate ${adlcStep || 6} / 6`}
                  </span>
                </div>
                <div className="grid grid-cols-6 gap-1.5">
                  {[
                    "1. Discovery",
                    "2. Spec Lock",
                    "3. Topology",
                    "4. TDD Clean",
                    "5. Auto-QA",
                    "6. SRE Build",
                  ].map((gateName, gIdx) => {
                    const isDone = (adlcStep === 0 && !adlcRunning) || adlcStep > gIdx;
                    const isCurrent = adlcRunning && adlcStep === gIdx + 1;
                    return (
                      <div
                        key={gateName}
                        className={`p-1.5 rounded text-center font-mono text-[9px] border transition-all ${
                          isDone
                            ? "bg-purple-950/60 border-purple-500/50 text-purple-300 font-bold"
                            : isCurrent
                            ? "bg-purple-500/30 border-purple-400 text-white animate-pulse"
                            : "bg-white/5 border-white/5 text-gray-500"
                        }`}
                      >
                        {gateName} {isDone ? "✓" : ""}
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* Generated Prompt Output Terminal */}
            <div className="flex flex-col gap-2 bg-[#050810] border border-white/10 rounded-xl p-4">
              <div className="flex items-center justify-between border-b border-white/10 pb-2">
                <div className="flex items-center gap-1.5 text-xs font-mono text-gray-400">
                  <Terminal className="w-3.5 h-3.5 text-[#38bdf8]" />
                  <span>Executable Antigravity Prompt</span>
                </div>
                <button
                  onClick={() =>
                    copyToClipboard(
                      generatedPrompt ||
                        activeStep.samplePrompt.replace(
                          "[ระบุชื่อระบบ]",
                          userIdea.trim() || "ระบบงานใหม่"
                        )
                    )
                  }
                  className="flex items-center gap-1 px-2.5 py-1 rounded bg-white/10 hover:bg-white/20 text-white font-mono text-[11px] transition-colors"
                >
                  {copied ? (
                    <Check className="w-3 h-3 text-emerald-400" />
                  ) : (
                    <Copy className="w-3 h-3" />
                  )}
                  <span>{copied ? "Copied!" : "Copy Prompt"}</span>
                </button>
              </div>

              <pre className="font-mono text-xs text-[#38bdf8] leading-relaxed whitespace-pre-wrap max-h-52 overflow-y-auto mt-2">
                {generatedPrompt ||
                  activeStep.samplePrompt.replace(
                    "[ระบุชื่อระบบ]",
                    userIdea.trim() || "ระบบงานที่ต้องการ"
                  )}
              </pre>
            </div>
          </section>

          {/* Right Column: 4 Foundation Knowledge Vaults & Telemetry (5 Cols) */}
          <aside className="lg:col-span-5 flex flex-col gap-5">
            {/* The 4 Knowledge Vaults Status Card */}
            <div className="bg-[#121826]/80 backdrop-blur-2xl border border-white/10 rounded-2xl p-5 shadow-2xl flex flex-col gap-3">
              <div className="flex items-center justify-between border-b border-white/10 pb-3">
                <div className="flex items-center gap-2">
                  <Layers className="w-4 h-4 text-[#a855f7]" />
                  <h3 className="text-xs font-bold text-white uppercase tracking-wider">
                    The 4 Knowledge Vaults Status
                  </h3>
                </div>
                <span className="text-[10px] font-mono text-emerald-400 bg-emerald-950/40 border border-emerald-500/20 px-2 py-0.5 rounded">
                  SYNCHRONIZED
                </span>
              </div>

              <div className="grid grid-cols-1 gap-2.5 text-xs">
                {/* Vault 1 */}
                <div className="p-3 bg-white/[0.02] border border-white/5 rounded-xl hover:border-white/15 transition-all flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <ShieldCheck className="w-4 h-4 text-[#ef4444]" />
                    <div>
                      <div className="font-bold text-white">ENGINEERING POLICY</div>
                      <div className="text-[10px] text-gray-400 font-mono">
                        Scope Lock · 4-Tier Evidence · Zero Guess
                      </div>
                    </div>
                  </div>
                  <span className="font-mono text-[10px] text-emerald-400">ACTIVE</span>
                </div>

                {/* Vault 2 */}
                <div className="p-3 bg-white/[0.02] border border-white/5 rounded-xl hover:border-white/15 transition-all flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <Bot className="w-4 h-4 text-[#a855f7]" />
                    <div>
                      <div className="font-bold text-white">FRAMEWORK ARCHITECTURE</div>
                      <div className="text-[10px] text-gray-400 font-mono">
                        5 Pillars: Prompt · Context · Loop · Harness · Graph
                      </div>
                    </div>
                  </div>
                  <span className="font-mono text-[10px] text-emerald-400">ACTIVE</span>
                </div>

                {/* Vault 3 */}
                <div className="p-3 bg-white/[0.02] border border-white/5 rounded-xl hover:border-white/15 transition-all flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <Sliders className="w-4 h-4 text-[#ffb000]" />
                    <div>
                      <div className="font-bold text-white">SPECIFICATION TEMPLATE</div>
                      <div className="text-[10px] text-gray-400 font-mono">
                        360° Studio · Dual-Track &lt;60ms · Radius &le;4px
                      </div>
                    </div>
                  </div>
                  <Link
                    href="/studio"
                    className="font-mono text-[10px] text-[#ffb000] hover:underline flex items-center gap-0.5"
                  >
                    <span>OPEN</span>
                    <ArrowRight className="w-3 h-3" />
                  </Link>
                </div>

                {/* Vault 4 */}
                <div className="p-3 bg-white/[0.02] border border-white/5 rounded-xl hover:border-white/15 transition-all flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <Database className="w-4 h-4 text-[#38bdf8]" />
                    <div>
                      <div className="font-bold text-white">STRUCTURE VAULT</div>
                      <div className="text-[10px] text-gray-400 font-mono">
                        SDLC 5-in-1 Master · Modular Monolith · Neon DB
                      </div>
                    </div>
                  </div>
                  <span className="font-mono text-[10px] text-emerald-400">ACTIVE</span>
                </div>
              </div>
            </div>

            {/* Live System Telemetry Card */}
            <div className="bg-[#121826]/80 backdrop-blur-2xl border border-white/10 rounded-2xl p-5 shadow-2xl flex flex-col gap-3">
              <div className="flex items-center justify-between border-b border-white/10 pb-3">
                <div className="flex items-center gap-2">
                  <Activity className="w-4 h-4 text-emerald-400 animate-pulse" />
                  <h3 className="text-xs font-bold text-white uppercase tracking-wider">
                    Sovereign Telemetry
                  </h3>
                </div>
                <span className="text-[10px] font-mono text-gray-400">
                  Node 20 / Next 16
                </span>
              </div>

              <div className="grid grid-cols-2 gap-2.5 text-xs font-mono">
                <div className="p-3 bg-black/40 border border-white/5 rounded-xl flex flex-col gap-0.5">
                  <span className="text-[10px] text-gray-400">Circuit Breaker</span>
                  <span className="text-emerald-400 font-bold">&le; 3 Loops Limit</span>
                </div>
                <div className="p-3 bg-black/40 border border-white/5 rounded-xl flex flex-col gap-0.5">
                  <span className="text-[10px] text-gray-400">Type Integrity</span>
                  <span className="text-[#00e5ff] font-bold">Strict Zero-Any</span>
                </div>
                <div className="p-3 bg-black/40 border border-white/5 rounded-xl flex flex-col gap-0.5">
                  <span className="text-[10px] text-gray-400">Policy Auditor</span>
                  <span className="text-emerald-400 font-bold">Passed (Exit 0)</span>
                </div>
                <div className="p-3 bg-black/40 border border-white/5 rounded-xl flex flex-col gap-0.5">
                  <span className="text-[10px] text-gray-400">Rendering Target</span>
                  <span className="text-[#ffb000] font-bold">&lt; 60ms 60 FPS</span>
                </div>
              </div>
            </div>
          </aside>
        </div>
      </main>

      {/* Guide Modal: 5-Mode Operation Manual */}
      {isGuideOpen && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
          <div className="bg-[#0f172a] border border-white/15 rounded-2xl max-w-3xl w-full max-h-[85vh] flex flex-col overflow-hidden shadow-2xl">
            <div className="px-6 py-4 border-b border-white/10 flex items-center justify-between">
              <h3 className="font-extrabold text-base text-white flex items-center gap-2">
                <HelpCircle className="w-5 h-5 text-[#38bdf8]" />
                คู่มือปฏิบัติการลูปวงจรทั้ง 5 โหมด (SDLC 5-in-1 Master Guide)
              </h3>
              <button
                onClick={() => setIsGuideOpen(false)}
                className="p-1.5 rounded-lg hover:bg-white/10 text-gray-400 hover:text-white transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="p-6 overflow-y-auto flex flex-col gap-4 text-xs leading-relaxed text-gray-300">
              {(Object.keys(ENGINE_MODES) as EngineMode[]).map((k) => {
                const m = ENGINE_MODES[k];
                return (
                  <div
                    key={k}
                    className="p-4 rounded-xl border flex flex-col gap-1.5"
                    style={{
                      backgroundColor: m.bgGlow,
                      borderColor: m.borderColor,
                    }}
                  >
                    <div className="font-bold text-sm" style={{ color: m.color }}>
                      {m.name} — {m.title}
                    </div>
                    <p className="text-gray-300">{m.desc}</p>
                    <div className="text-[11px] font-mono text-gray-400 mt-1">
                      <strong>ขั้นตอนหลัก:</strong> {m.steps.map((s) => s.title).join(" ➔ ")}
                    </div>
                  </div>
                );
              })}
            </div>

            <div className="px-6 py-3 border-t border-white/10 flex justify-end">
              <button
                onClick={() => setIsGuideOpen(false)}
                className="px-4 py-2 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs transition-colors"
              >
                รับทราบและปิดคู่มือ
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
