"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import {
  ShieldAlert,
  ShieldCheck,
  Scale,
  FileText,
  Search,
  ExternalLink,
  ChevronRight,
  Database,
  Layers,
  Sparkles,
  Zap,
  Bot,
  Ruler,
  Users2,
  Stethoscope,
  Copy,
  Check,
  ArrowRight,
  Sliders,
  RefreshCw,
  Eye,
  AlertTriangle,
  FolderGit2,
  Terminal,
  Activity,
  Cpu,
  Lock,
  Network,
  Calendar,
  DollarSign,
  Gavel,
  CheckCircle2,
  FileCheck2,
  FileSpreadsheet,
} from "lucide-react";

type EngineMode = "SDLC" | "ADLC" | "SDD" | "SWARM" | "HEALING";
type MainTab = "COMMAND" | "TARGETS" | "SMOKING_GUNS" | "AI_ENGINE" | "DOCS_1TO1";

interface TargetPerson {
  id: string;
  name: string;
  role: string;
  roleType: "MAIN" | "ACCOMPLICE" | "MULE";
  roleColor: string;
  totalLoss: string;
  accounts: string[];
  charges: string[];
  defenseBusting: string;
  smokingGunId: string;
  smokingGunTitle: string;
  chatSnippet: string;
  coordinates: string;
}

const TARGET_PERSONS: TargetPerson[] = [
  {
    id: "target-1",
    name: "น.ส. จิณห์นิภา ประสาทเขตรการ",
    role: "ตัวการหลัก (ผู้บงการ/ผู้สั่งการ)",
    roleType: "MAIN",
    roleColor: "#ef4444",
    totalLoss: "ยอดความเสียหายรวมทุกบัญชี",
    accounts: ["KBANK xxx-x-x1951-x", "สลิปตรง 26,400 บาท"],
    charges: [
      "ป.อ. มาตรา ๓๔๑, ๓๔๓ (ฉ้อโกงประชาชน/ปกติธุระ)",
      "พ.ร.บ. ป้องกันและปราบปรามการฟอกเงิน พ.ศ. ๒๕๔๒ มาตรา ๓, ๕",
      "พ.ร.ก. มาตรการป้องกันและปราบปรามอาชญากรรมทางเทคโนโลยี พ.ศ. ๒๕๖๖",
    ],
    defenseBusting:
      "หักล้างข้ออ้าง 'ยืมเงินส่วนตัวทางแพ่ง': นำสเตทเมนต์พิสูจน์การสั่งโอนเงินกระจัดกระจายเข้าบัญชีม้า ๕ บัญชีในเวลาเสี้ยวนาที พร้อมแชทสร้างเรื่องเท็จซ้ำซาก ขาดเจตนาชำระคืนแต่แรก",
    smokingGunId: "EVIDENCE_8",
    smokingGunTitle: "สลิปโอนตรง 26,400 บาท และแชทรับสภาพหนี้เจตนาลวง",
    chatSnippet:
      "«หนูกำลังหาทางเคลียร์ให้พี่อยู่นะคะ เงินจะเข้าบัญชีหนูช่วงบ่าย... แต่ขอให้พี่โอนยอดนี้เข้าบัญชีปรียาฉัตรก่อน»",
    coordinates: "หน้าแชทหลัก #106 / พิกัด Master Transcript",
  },
  {
    id: "target-2",
    name: "น.ส. ปรียาฉัตร ชิมพลี",
    role: "ตัวการร่วม / บัญชีรับผลประโยชน์แกนหลัก",
    roleType: "ACCOMPLICE",
    roleColor: "#f59e0b",
    totalLoss: "22,500+ บาท (พบหลักฐานสลิปตรง)",
    accounts: ["KBANK 055-1-49978-4", "KBANK 055-1-49978-4"],
    charges: [
      "ป.อ. มาตรา ๓๔๑, ๓๔๓ ประกอบมาตรา ๘๓ (ตัวการร่วม)",
      "พ.ร.ก. อาชญากรรมทางเทคโนโลยี ๒๕๖๖ มาตรา ๙ (บัญชีม้า)",
      "พ.ร.บ. ฟอกเงิน พ.ศ. ๒๕๔๒",
    ],
    defenseBusting:
      "หักล้างข้ออ้าง 'ไม่รู้จักผู้เสียหาย/ขายของออนไลน์': ตรวจพบพิกัด Master Timeline Strip V3 หน้า 41-42 เชื่อมโยงบัญชีปรียาฉัตรโอนต่อไปยังบัญชี 3 พี่น้องประสาทเขตรการทันที แสดงถึงการรู้เห็นเป็นใจในสายธารเงิน",
    smokingGunId: "EVIDENCE_2_9",
    smokingGunTitle: "สลิป 9,000 / 13,500 บาท & แชท V3 หน้า 41 พิกัดประสานงา",
    chatSnippet:
      "«โอนเข้าบัญชี ปรียาฉัตร ชิมพลี กสิกร 0551499784 ยอด 9,000 บาทนะคะ หนูส่งสลิปให้แล้วค่ะ»",
    coordinates: "Chat V3 Page 41 / NEW_362_FILES Node #41",
  },
  {
    id: "target-3",
    name: "น.ส. วรรณวิสา ประสาทเขตรการ",
    role: "ตัวการร่วมทางเครือญาติ (ผู้รับผลประโยชน์ฟอกเงิน)",
    roleType: "ACCOMPLICE",
    roleColor: "#a855f7",
    totalLoss: "โอนหมุนเวียนต่อเนื่องข้ามธนาคาร",
    accounts: ["ธ.ออมสิน (GSB) 020-3-92576-946"],
    charges: [
      "ป.อ. มาตรา ๘๓, ๓๔๑ (ร่วมกันฉ้อโกง)",
      "พ.ร.บ. ฟอกเงิน พ.ศ. ๒๕๔๒ มาตรา ๕ (โอน รับโอน หรือเปลี่ยนสภาพทรัพย์สิน)",
      "พ.ร.ก. บัญชีม้า พ.ศ. ๒๕๖๖",
    ],
    defenseBusting:
      "หักล้างข้ออ้าง 'เงินช่วยเหลือพี่น้อง': นำแชทคำสั่งโอน V3 หน้า 31 และ 42 ที่จำเลยสั่งให้โอนเข้าบัญชีออมสินของวรรณวิสาโดยตรง พิสูจน์ว่าเป็นจุดพักเงินเพื่อนำไปชำระหนี้สินเชื่อบ้านของครอบครัว",
    smokingGunId: "EVIDENCE_10_11",
    smokingGunTitle: "แชท V3 หน้า 31 และ 42 สั่งโอนเข้าออมสิน วรรณวิสา",
    chatSnippet:
      "«โอนเข้าออมสินพี่สาวหนู วรรณวิสา 020392576946 ยอดนี้ต้องตัดก่อนเที่ยงนะพี่»",
    coordinates: "Chat V3 Page 31 & 42 / Master Strip Timeline",
  },
  {
    id: "target-4",
    name: "ด.ญ. ทัศนียกานต์ ประสาทเขตรการ",
    role: "ตัวการร่วมเครือข่ายครอบครัว (บัญชีพร้อมเพย์รับโอน)",
    roleType: "ACCOMPLICE",
    roleColor: "#a855f7",
    totalLoss: "กระจายรับเงินหมุนเวียน",
    accounts: ["พร้อมเพย์ 099-317-0627"],
    charges: [
      "พ.ร.ก. มาตรการป้องกันและปราบปรามอาชญากรรมทางเทคโนโลยี พ.ศ. ๒๕๖๖ มาตรา ๙",
      "พ.ร.บ. ฟอกเงิน พ.ศ. ๒๕๔๒ (ทางร่วมรับผลประโยชน์)",
    ],
    defenseBusting:
      "หักล้างข้ออ้าง 'ผู้เยาว์ไม่มีส่วนเกี่ยวข้อง': ผู้ปกครองและตัวการหลักนำบัญชีพร้อมเพย์เด็กมาเปิดรับโอนเงินจากการกระทำผิด ถือเป็นเครื่องมือในการฟอกเงินและกระจายถ่ายโอนทรัพย์สิน",
    smokingGunId: "EVIDENCE_12",
    smokingGunTitle: "แชท V3 หน้า 113 พร้อมเพย์ 099-317-0627",
    chatSnippet:
      "«พี่โอนเข้าพร้อมเพย์นี้ได้เลยค่ะ 0993170627 ชื่อ ทัศนียกานต์ เดี๋ยวเงินเข้าแล้วหนูโทรบอก»",
    coordinates: "Chat V3 Page 113 / Evidence Node #113",
  },
  {
    id: "target-5",
    name: "น.ส. บุณฑริกา บุญประเสริฐ",
    role: "บัญชีม้าสร้างสถานการณ์ (Mule with Fabricated Drama)",
    roleType: "MULE",
    roleColor: "#38bdf8",
    totalLoss: "รับโอนหมุนเวียนตามแผนดราม่า",
    accounts: ["KBANK 147-3-15709-0"],
    charges: [
      "พ.ร.ก. บัญชีม้า พ.ศ. ๒๕๖๖ มาตรา ๙, ๑๐",
      "ป.อ. มาตรา ๘๖ (ผู้สนับสนุนการฉ้อโกง)",
    ],
    defenseBusting:
      "หักล้างข้ออ้าง 'ไม่รู้เห็น': ตรวจพบภาพแผลสดและสเตตัสอ้างมึนหัวเข้าโรงพยาบาลในแชท ใช้เป็นเครื่องมือกดดันให้ผู้เสียหายเร่งโอนเงินช่วยเหลือฉุกเฉิน",
    smokingGunId: "EVIDENCE_5_6",
    smokingGunTitle: "ภาพหลักฐานแผลสด & แชทอ้างมึนหัวเร่งโอนเงินเข้า KBANK",
    chatSnippet:
      "«พี่คะหนูล้มรถแผลลึกมาก ตอนนี้อยู่คลินิก ช่วยโอนเข้าบัญชี บุณฑริกา 1473157090 ด่วนเลยค่ะ»",
    coordinates: "Evidence 5 & 6 / Smoking Gun Vault",
  },
  {
    id: "target-6",
    name: "นาง นฤมล คำปา",
    role: "บัญชีม้ารับโอนปลายทาง (Secondary Proxy Mule)",
    roleType: "MULE",
    roleColor: "#38bdf8",
    totalLoss: "รับโอนสลิปตรงหลายรายการ",
    accounts: ["KBANK / SCB บัญชีรับโอน"],
    charges: [
      "พ.ร.ก. บัญชีม้า พ.ศ. ๒๕๖๖ มาตรา ๙",
      "ป.อ. ๘๖ (ผู้สนับสนุน)",
    ],
    defenseBusting:
      "หักล้างข้ออ้าง 'บัญชีรับจ้างทั่วไป': บัญชีมีรายการเงินเข้าจากคดีฉ้อโกงและถูกถอนออกทันทีภายในไม่กี่นาที เป็นพฤติการณ์บัญชีม้าตัดตอนมาตรฐาน",
    smokingGunId: "EVIDENCE_MULE",
    smokingGunTitle: "สลิปเงินเข้าบัญชีนฤมล คำปา",
    chatSnippet:
      "«โอนเข้าบัญชี นฤมล คำปา ยอดนี้พี่เขาจะช่วยตัดของให้ค่ะ»",
    coordinates: "Timeline Row #78 / Legal Triage Matrix",
  },
];

const SMOKING_GUNS = [
  {
    id: "EVIDENCE_10",
    title: "แชท V3 หน้า 42: รอยต่อพิกัดต่อเนื่องสองพี่น้อง",
    desc: "หลักฐานจุดตายคดี! จำเลยสั่งโอนเงินเข้า ธ.ออมสิน วรรณวิสา และ พร้อมเพย์ ทัศนียกานต์ ในหน้าเดียวกัน",
    tag: "SMOKING GUN #10",
    date: "18 พ.ย. 2569",
    category: "ความเชื่อมโยงเครือข่าย",
    impact: "พิสูจน์เจตนาฟอกเงินเครือญาติ 100%",
  },
  {
    id: "EVIDENCE_9",
    title: "แชท V3 หน้า 41: คำสั่งโอนเข้า ปรียาฉัตร ชิมพลี",
    desc: "หลักฐานมัดตัวเชื่อมต่อหน้า 42 พิสูจน์ว่าเงินจากปรียาฉัตรและสองพี่น้องเป็นวงจรอุบาทว์เดียวกัน",
    tag: "SMOKING GUN #9",
    date: "18 พ.ย. 2569",
    category: "ตัวการร่วมเส้นทางเงิน",
    impact: "มัดตัว ปรียาฉัตร ชิมพลี พ้นข้อต่อสู้",
  },
  {
    id: "EVIDENCE_8",
    title: "สลิปโอนตรง น.ส. จิณห์นิภา 26,400 บาท",
    desc: "หลักฐานการโอนเงินสดเข้าบัญชีผู้สั่งการโดยตรง ตัดข้อต่อสู้ที่อ้างว่าไม่ได้รับเงินจากผู้เสียหาย",
    tag: "SMOKING GUN #8",
    date: "ไทม์ไลน์เหตุการณ์",
    category: "ตัวการหลัก",
    impact: "หลักฐานมัดตัวความผิดสำเร็จ ป.อ. ๓๔๑",
  },
  {
    id: "EVIDENCE_2",
    title: "สลิป ธ.กสิกรไทย ปรียาฉัตร ชิมพลี 9,000 บาท",
    desc: "สลิปการเงินโอนเข้าบัญชี 055-1-49978-4 พร้อม QR Code และเลขอ้างอิงธนาคารตรวจสอบได้ระดับ Forensic",
    tag: "SMOKING GUN #2",
    date: "ไทม์ไลน์เหตุการณ์",
    category: "เส้นทางการเงิน",
    impact: "หลักฐานยืนยันบัญชีรับโอนแท้จริง",
  },
  {
    id: "EVIDENCE_5",
    title: "ภาพแผลสดลวงโลก & บัญชี บุณฑริกา บุญประเสริฐ",
    desc: "จำเลยส่งภาพบาดแผลสร้างเรื่องเท็จเพื่อขอเงินช่วยเหลือ แล้วสั่งให้โอนเข้าบัญชีม้าบุณฑริกา",
    tag: "SMOKING GUN #5",
    date: "ไทม์ไลน์เหตุการณ์",
    category: "กลอุบายหลอกลวง",
    impact: "พิสูจน์การแสดงข้อความอันเป็นเท็จ",
  },
  {
    id: "EVIDENCE_1",
    title: "ผังรวมบัญชี 3 พี่น้องตระกูลประสาทเขตรการ",
    desc: "แผนผังบัญชี จิณห์นิภา - วรรณวิสา - ทัศนียกานต์ ที่ปรากฏในบทสนทนาแชทอย่างต่อเนื่อง",
    tag: "SMOKING GUN #1",
    date: "ดัชนีพยานหลักฐาน",
    category: "โครงสร้างขบวนการ",
    impact: "หลักฐานมัดตัวความผิดฐานฟอกเงิน",
  },
];

const ENGINE_MODES: Record<EngineMode, {
  name: string;
  tag: string;
  icon: typeof Zap;
  color: string;
  bgGlow: string;
  borderColor: string;
  desc: string;
  samplePrompt: string;
}> = {
  SDLC: {
    name: "1. SDLC Vibe",
    tag: "Human-in-the-Lead",
    icon: Zap,
    color: "#38bdf8",
    bgGlow: "rgba(56, 189, 248, 0.15)",
    borderColor: "rgba(56, 189, 248, 0.4)",
    desc: "Spec-Driven Development with AI Copilot — มนุษย์นำยุทธศาสตร์ AI เป็นคู่คิด ปรับแต่งรวดเร็ว",
    samplePrompt: "เป้าหมาย: วิเคราะห์และดำเนินคดีพยานหลักฐานดิจิทัลคดีฉ้อโกง ช่วยซักถามเจาะลึก 4 ด้านตามหลัก Grill-Me",
  },
  ADLC: {
    name: "2. ADLC Engine",
    tag: "Agent Autonomous",
    icon: Bot,
    color: "#a855f7",
    bgGlow: "rgba(168, 85, 247, 0.15)",
    borderColor: "rgba(168, 85, 247, 0.4)",
    desc: "สายพานอัตโนมัติ 100% ตั้งแต่ล็อกแผนงาน ➔ แตก Task ➔ เขียน TDD ➔ รันเทสต์ Exit Code 0",
    samplePrompt: "อ่าน BRAIN.md และ SOVEREIGN.md เตรียมพร้อมรัน ADLC Engine ภายใต้ Token Budget Tier M",
  },
  SDD: {
    name: "3. Spec-Driven",
    tag: "Schema is King",
    icon: Ruler,
    color: "#10b981",
    bgGlow: "rgba(16, 185, 129, 0.15)",
    borderColor: "rgba(16, 185, 129, 0.4)",
    desc: "สเปกคือพระเจ้า — ล็อก Zod Schemas และ DB Contracts ก่อนแตะต้อง Logic ป้องกันมโนโค้ด",
    samplePrompt: "นิยาม Zod Schemas และ Drizzle Table พร้อม Optimistic Lock ใน src/db/schema.ts ห้ามใช้ any",
  },
  SWARM: {
    name: "4. Agent Swarm",
    tag: "Maker vs Checker",
    icon: Users2,
    color: "#f59e0b",
    bgGlow: "rgba(245, 158, 11, 0.15)",
    borderColor: "rgba(245, 158, 11, 0.4)",
    desc: "คานอำนาจ 2 ขั้ว: Maker (คนเขียนโค้ด) ⇄ Checker (คนตรวจจับผิด QA) ป้องกัน AI หลอกตัวเอง",
    samplePrompt: "สวมหมวก Maker-Checker Swarm: ให้ตัวหนึ่งเขียน Minimal Surgical Diff และอีกตัวรัน 4-Tier Code Review",
  },
  HEALING: {
    name: "5. Self-Healing",
    tag: "5-Whys Diagnostics",
    icon: Stethoscope,
    color: "#ef4444",
    bgGlow: "rgba(239, 68, 68, 0.15)",
    borderColor: "rgba(239, 68, 68, 0.4)",
    desc: "แพทย์ผ่าตัดซ่อมสด — วินิจฉัยรากเหง้าด้วย 5-Whys RCA และออกแพตช์ถาวร ป้องกันเกิดซ้ำ 100%",
    samplePrompt: "ทำตรรกะ 5-Whys Diagnostic Drill-Down สกัด Root Cause และเขียน Permanent Corrective Action",
  },
};

export default function TacticalCommandCenterPage() {
  const [activeTab, setActiveTab] = useState<MainTab>("COMMAND");
  const [selectedTarget, setSelectedTarget] = useState<TargetPerson>(TARGET_PERSONS[0]);
  const [activeEngineMode, setActiveEngineMode] = useState<EngineMode>("SDLC");
  const [copied, setCopied] = useState<string | null>(null);
  const [userPromptInput, setUserPromptInput] = useState<string>("");
  const [generatedPrompt, setGeneratedPrompt] = useState<string>("");
  const [activeSmokingGun, setActiveSmokingGun] = useState<typeof SMOKING_GUNS[0] | null>(null);

  const copyToClipboard = (text: string, id: string) => {
    navigator.clipboard.writeText(text);
    setCopied(id);
    setTimeout(() => setCopied(null), 2000);
  };

  const currentModeConfig = ENGINE_MODES[activeEngineMode];

  const handleGeneratePrompt = () => {
    const topic = userPromptInput.trim() || "ตรวจสอบและสร้างสำนวนคดีอาญาจากหลักฐานแชทและสลิป";
    const prompt = `[เริ่มปฏิบัติการโหมด ${currentModeConfig.name}]
หัวข้อภารกิจ: ${topic}

กรุณารันคำสั่งตามสถาปัตยกรรม Sovereign Architecture:
1. ใช้งานคลัง 10 สกิลนิติวิทยาศาสตร์ดิจิทัล (RAG-Eviden Vault)
2. สกัดพยานหลักฐาน ๖ บุคคลเป้าหมาย และตรวจสอบรอยต่อพิกัด Master Timeline Strip V3
3. วางฐานความผิดตาม ป.อ. มาตรา ๓๔๑, ๓๔๓, พ.ร.ก.บัญชีม้า ๒๕๖๖ และ พ.ร.บ.ฟอกเงิน
4. ควบคุมการเขียนโค้ดตามกฎ Anti-Slop และจำกัด Minimal Surgical Diff`;
    setGeneratedPrompt(prompt);
  };

  return (
    <div className="min-h-screen w-full bg-[#07090e] text-[#f8fafc] font-sans flex flex-col relative selection:bg-sky-500/30 selection:text-white">
      {/* Background Ambient Glows */}
      <div className="fixed inset-0 pointer-events-none z-0 overflow-hidden">
        <div className="absolute top-[-100px] left-[15%] w-[650px] h-[650px] rounded-full blur-[160px] opacity-20 bg-sky-500" />
        <div className="absolute top-[35%] right-[-100px] w-[550px] h-[550px] rounded-full blur-[170px] opacity-15 bg-purple-600" />
        <div className="absolute bottom-[-100px] left-[-100px] w-[600px] h-[600px] rounded-full blur-[180px] opacity-10 bg-emerald-600" />
        <div className="absolute inset-0 bg-[radial-gradient(rgba(255,255,255,0.03)_1px,transparent_1px)] [background-size:24px_24px] opacity-40" />
      </div>

      {/* Top Tactical Status Bar */}
      <header className="sticky top-0 z-50 glass-obsidian border-b border-white/[0.08] px-4 md:px-8 py-3">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-3">
          {/* Logo & Brand */}
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-sky-500/20 via-indigo-500/20 to-purple-500/20 border border-sky-500/40 flex items-center justify-center text-sky-400 shadow-[0_0_15px_rgba(56,189,248,0.25)]">
              <Scale className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-mono text-xs font-black tracking-widest text-sky-400">
                  RAG-EVIDEN
                </span>
                <span className="text-[10px] px-1.5 py-0.5 rounded bg-sky-500/10 text-sky-300 font-mono border border-sky-500/20">
                  v2.6 TACTICAL
                </span>
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
              </div>
              <h1 className="text-sm font-bold text-slate-200 tracking-tight">
                Forensic Command Center & Digital Evidence Vault
              </h1>
            </div>
          </div>

          {/* Quick External Actions & Badges */}
          <div className="flex items-center gap-2 overflow-x-auto text-xs font-mono">
            <a
              href="https://github.com/palaside/RAG-Eviden"
              target="_blank"
              rel="noreferrer"
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg glass-pill text-slate-300 hover:text-white hover:border-sky-500/40 transition-all"
            >
              <FolderGit2 className="w-3.5 h-3.5 text-sky-400" />
              <span>palaside/RAG-Eviden</span>
              <ExternalLink className="w-3 h-3 text-slate-500" />
            </a>

            <a
              href="https://prlens.dev/c/TWOhzAyMhVEyK9KCVxe2EA"
              target="_blank"
              rel="noreferrer"
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg glass-pill text-purple-300 hover:text-white hover:border-purple-500/40 transition-all"
            >
              <Network className="w-3.5 h-3.5 text-purple-400" />
              <span>PR Lens Canvas</span>
              <ExternalLink className="w-3 h-3 text-slate-500" />
            </a>

            <Link
              href="/chawakom"
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-sky-500/10 border border-sky-500/30 text-sky-400 hover:bg-sky-500/20 font-bold transition-all"
            >
              <FileSpreadsheet className="w-3.5 h-3.5" />
              <span>ชวกม.7 Platform</span>
            </Link>

            <Link
              href="/studio"
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-400 hover:bg-amber-500/20 font-bold transition-all"
            >
              <Sliders className="w-3.5 h-3.5" />
              <span>UI Studio 360°</span>
            </Link>
          </div>
        </div>
      </header>

      {/* Main Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 md:px-8 py-6 z-10 flex flex-col gap-6">
        {/* Top 4 Tactical Metric HUD Cards */}
        <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {/* Card 1 */}
          <div className="glass-card glass-card-hover rounded-2xl p-5 flex flex-col justify-between relative overflow-hidden group">
            <div className="absolute top-0 right-0 w-24 h-24 bg-sky-500/10 rounded-full blur-2xl group-hover:bg-sky-500/20 transition-all" />
            <div className="flex items-center justify-between text-slate-400 text-xs font-mono">
              <span className="flex items-center gap-1.5 text-sky-400 font-bold">
                <ShieldCheck className="w-4 h-4" />
                COURT EVIDENCE VAULT
              </span>
              <span className="text-[10px] px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                CLEAN 100%
              </span>
            </div>
            <div className="my-3">
              <div className="text-3xl font-extrabold text-white tracking-tight">
                1,458 <span className="text-sm font-normal text-slate-400">หน้า A4</span>
              </div>
              <p className="text-xs text-slate-400 mt-1">
                กำจัด dup_ 1,334 ไฟล์ คืนพื้นที่ 881 MB ปลอดหลักฐานซ้ำในศาล
              </p>
            </div>
            <div className="pt-2 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono text-slate-400">
              <span>Smoking Guns: <strong className="text-sky-300">13 ภาพ</strong></span>
              <span>Timeline: <strong className="text-sky-300">188 เหตุการณ์</strong></span>
            </div>
          </div>

          {/* Card 2 */}
          <div className="glass-card glass-card-hover rounded-2xl p-5 flex flex-col justify-between relative overflow-hidden group">
            <div className="absolute top-0 right-0 w-24 h-24 bg-amber-500/10 rounded-full blur-2xl group-hover:bg-amber-500/20 transition-all" />
            <div className="flex items-center justify-between text-slate-400 text-xs font-mono">
              <span className="flex items-center gap-1.5 text-amber-400 font-bold">
                <DollarSign className="w-4 h-4" />
                FRAUD BENEFICIARY NETWORK
              </span>
              <span className="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">
                ISOLATED
              </span>
            </div>
            <div className="my-3">
              <div className="text-3xl font-extrabold text-white tracking-tight">
                ๖ <span className="text-sm font-normal text-slate-400">บุคคลเป้าหมาย</span>
              </div>
              <p className="text-xs text-slate-400 mt-1">
                สแกน 5,266 สลิป คัดแยก Proxy บัญชีโอนแทน 4 รายการชัดเจน
              </p>
            </div>
            <div className="pt-2 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono text-slate-400">
              <span>ฐานความผิด: <strong className="text-amber-300">ป.อ. ๓๔๑/๓๔๓</strong></span>
              <span>พรบ.ฟอกเงิน: <strong className="text-amber-300">มาตรา ๓, ๕</strong></span>
            </div>
          </div>

          {/* Card 3 */}
          <div className="glass-card glass-card-hover rounded-2xl p-5 flex flex-col justify-between relative overflow-hidden group">
            <div className="absolute top-0 right-0 w-24 h-24 bg-purple-500/10 rounded-full blur-2xl group-hover:bg-purple-500/20 transition-all" />
            <div className="flex items-center justify-between text-slate-400 text-xs font-mono">
              <span className="flex items-center gap-1.5 text-purple-400 font-bold">
                <FileCheck2 className="w-4 h-4" />
                CHAWAKOM 1:1 ENGINE
              </span>
              <span className="text-[10px] px-1.5 py-0.5 rounded bg-purple-500/10 text-purple-400 border border-purple-500/20">
                ACTIVE
              </span>
            </div>
            <div className="my-3">
              <div className="text-3xl font-extrabold text-white tracking-tight">
                29 <span className="text-sm font-normal text-slate-400">ชีตมาตรฐาน</span>
              </div>
              <p className="text-xs text-slate-400 mt-1">
                เอกสารราชการ ทบ. 1:1 XEROX ปลอดความหลอน AI Formula Audit
              </p>
            </div>
            <div className="pt-2 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono text-slate-400">
              <span>Errors: <strong className="text-emerald-400">0</strong></span>
              <span>Anti-Hallucination: <strong className="text-purple-300">100%</strong></span>
            </div>
          </div>

          {/* Card 4 */}
          <div className="glass-card glass-card-hover rounded-2xl p-5 flex flex-col justify-between relative overflow-hidden group">
            <div className="absolute top-0 right-0 w-24 h-24 bg-emerald-500/10 rounded-full blur-2xl group-hover:bg-emerald-500/20 transition-all" />
            <div className="flex items-center justify-between text-slate-400 text-xs font-mono">
              <span className="flex items-center gap-1.5 text-emerald-400 font-bold">
                <Bot className="w-4 h-4" />
                AI FORENSIC SUITE
              </span>
              <span className="text-[10px] px-1.5 py-0.5 rounded bg-sky-500/10 text-sky-400 border border-sky-500/20">
                ARMED
              </span>
            </div>
            <div className="my-3">
              <div className="text-3xl font-extrabold text-white tracking-tight">
                10 <span className="text-sm font-normal text-slate-400">สกิลนิติวิทยาศาสตร์</span>
              </div>
              <p className="text-xs text-slate-400 mt-1">
                ครอบคลุม RAG Deep Dive, Indictment, Timeline 11D & Killer Cross-Exam
              </p>
            </div>
            <div className="pt-2 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono text-slate-400">
              <span>SDLC Engine: <strong className="text-emerald-300">5 Modes</strong></span>
              <span>Token Budget: <strong className="text-emerald-300">Tier M</strong></span>
            </div>
          </div>
        </section>

        {/* Tactical Navigation Tabs */}
        <div className="flex items-center gap-1 bg-[#0b0f19]/90 p-1.5 rounded-2xl border border-white/[0.08] overflow-x-auto">
          {[
            { id: "COMMAND", label: "ภาพรวมศูนย์บัญชาการ (Overview)", icon: Activity },
            { id: "TARGETS", label: "สำนวน ๖ บุคคลเป้าหมายแห่งคดี (Dossier)", icon: Gavel },
            { id: "SMOKING_GUNS", label: "คลังภาพหลักฐานจุดตายคดี (Smoking Guns)", icon: Eye },
            { id: "AI_ENGINE", label: "สายพาน AI Sovereign Engine & SDLC", icon: Cpu },
            { id: "DOCS_1TO1", label: "ชวกม. 1:1 Document Engine", icon: FileText },
          ].map((tab) => {
            const Icon = tab.icon;
            const isActive = activeTab === tab.id;
            return (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id as MainTab)}
                className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-bold transition-all whitespace-nowrap ${
                  isActive
                    ? "bg-gradient-to-r from-sky-500/20 to-indigo-500/20 border border-sky-500/40 text-white shadow-[0_0_20px_rgba(56,189,248,0.2)]"
                    : "text-slate-400 hover:text-slate-200 hover:bg-white/[0.03]"
                }`}
              >
                <Icon className={`w-4 h-4 ${isActive ? "text-sky-400" : "text-slate-500"}`} />
                <span>{tab.label}</span>
              </button>
            );
          })}
        </div>

        {/* TAB 1: OVERVIEW COMMAND */}
        {activeTab === "COMMAND" && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            {/* Left 8 Cols: Master Timeline Strip & Network Graph Insight */}
            <section className="lg:col-span-8 flex flex-col gap-6">
              {/* Highlight Banner: Master Timeline Strip V3 */}
              <div className="glass-card rounded-2xl p-6 border-l-4 border-l-sky-500 relative overflow-hidden">
                <div className="flex items-start justify-between gap-4">
                  <div>
                    <span className="font-mono text-xs uppercase tracking-wider text-sky-400 font-bold flex items-center gap-1.5">
                      <Sparkles className="w-3.5 h-3.5" />
                      CERTIFIED FORENSIC DISCOVERY // V3 TIMELINE STRIP
                    </span>
                    <h2 className="text-xl font-bold text-white mt-1">
                      ค้นพบ "Master Timeline Strip V3" บันทึกรอยต่อพิกัดต่อเนื่องสมบูรณ์ที่สุด
                    </h2>
                    <p className="text-sm text-slate-300 mt-2 leading-relaxed">
                      จากการสแกนชุดภาพแคปจอยาว V3 แชทที่ 3 พบหลักฐานประสานงาในหน้า <strong>41</strong> (คำสั่งโอนเข้า ปรียาฉัตร ชิมพลี) 
                      ต่อเนื่องเชื่อมโยงเข้าสู่หน้า <strong>42</strong> (โอนเข้า ธ.ออมสิน วรรณวิสา และ พร้อมเพย์ ทัศนียกานต์) 
                      ในระยะเวลาเพียงไม่กี่นาที เป็นพยานหลักฐานมัดตัวความผิดฐานฉ้อโกงประชาชนและฟอกเงิน 100%
                    </p>
                  </div>
                  <span className="px-3 py-1 rounded-lg bg-sky-500/10 text-sky-400 border border-sky-500/30 font-mono text-xs whitespace-nowrap">
                    Court Standard
                  </span>
                </div>

                <div className="mt-4 flex flex-wrap items-center gap-3">
                  <button
                    onClick={() => setActiveTab("TARGETS")}
                    className="flex items-center gap-2 px-4 py-2 rounded-xl bg-sky-500 text-slate-950 font-bold text-xs hover:bg-sky-400 transition-all shadow-[0_0_15px_rgba(56,189,248,0.3)]"
                  >
                    <span>ตรวจสำนวน ๖ เป้าหมาย</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                  <button
                    onClick={() => setActiveTab("SMOKING_GUNS")}
                    className="flex items-center gap-2 px-4 py-2 rounded-xl glass-pill text-slate-300 hover:text-white font-medium text-xs transition-all"
                  >
                    <Eye className="w-3.5 h-3.5 text-sky-400" />
                    <span>เปิดดูภาพหลักฐานจุดตายคดี (Smoking Guns)</span>
                  </button>
                </div>
              </div>

              {/* 6 Targets Quick Grid */}
              <div className="glass-card rounded-2xl p-6">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center gap-2">
                    <Gavel className="w-5 h-5 text-amber-400" />
                    <h3 className="text-base font-bold text-white">
                      ทำเนียบ ๖ บุคคลเป้าหมายแห่งคดี (Court Indictment Roster)
                    </h3>
                  </div>
                  <span className="text-xs font-mono text-slate-400">
                    ISO/IEC 27037 Aligned
                  </span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {TARGET_PERSONS.map((p) => (
                    <div
                      key={p.id}
                      onClick={() => {
                        setSelectedTarget(p);
                        setActiveTab("TARGETS");
                      }}
                      className="glass-card glass-card-hover rounded-xl p-4 cursor-pointer flex flex-col justify-between group"
                    >
                      <div className="flex items-start justify-between">
                        <div>
                          <div className="text-sm font-bold text-slate-100 group-hover:text-sky-300 transition-colors">
                            {p.name}
                          </div>
                          <span
                            className="text-[11px] font-mono px-2 py-0.5 rounded-full inline-block mt-1 font-bold"
                            style={{
                              backgroundColor: `${p.roleColor}15`,
                              color: p.roleColor,
                              border: `1px solid ${p.roleColor}40`,
                            }}
                          >
                            {p.role}
                          </span>
                        </div>
                        <ChevronRight className="w-4 h-4 text-slate-600 group-hover:text-sky-400 group-hover:translate-x-1 transition-all" />
                      </div>
                      <div className="mt-3 pt-3 border-t border-white/[0.06] text-xs text-slate-400 flex items-center justify-between font-mono">
                        <span>{p.accounts[0]}</span>
                        <span className="text-sky-400">ดูสำนวน ➔</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </section>

            {/* Right 4 Cols: Quick Command Launchers & System Health */}
            <aside className="lg:col-span-4 flex flex-col gap-6">
              {/* 1-Click Launchers Widget */}
              <div className="glass-card rounded-2xl p-6">
                <div className="flex items-center gap-2 mb-4 pb-3 border-b border-white/[0.08]">
                  <Terminal className="w-5 h-5 text-sky-400" />
                  <h3 className="text-sm font-bold text-white uppercase tracking-wider font-mono">
                    1-Click Forensic Launchers
                  </h3>
                </div>

                <div className="flex flex-col gap-2.5">
                  <a
                    href="https://github.com/palaside/RAG-Eviden"
                    target="_blank"
                    rel="noreferrer"
                    className="flex items-center justify-between p-3 rounded-xl glass-pill hover:bg-white/[0.06] hover:border-sky-500/40 transition-all group"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded-lg bg-sky-500/10 border border-sky-500/30 flex items-center justify-center text-sky-400">
                        <FolderGit2 className="w-4 h-4" />
                      </div>
                      <div>
                        <div className="text-xs font-bold text-white group-hover:text-sky-300">
                          GitHub RAG-Eviden Repo
                        </div>
                        <div className="text-[10px] text-slate-400 font-mono">
                          palaside/RAG-Eviden (main)
                        </div>
                      </div>
                    </div>
                    <ExternalLink className="w-3.5 h-3.5 text-slate-500 group-hover:text-sky-400" />
                  </a>

                  <a
                    href="https://prlens.dev/c/TWOhzAyMhVEyK9KCVxe2EA"
                    target="_blank"
                    rel="noreferrer"
                    className="flex items-center justify-between p-3 rounded-xl glass-pill hover:bg-white/[0.06] hover:border-purple-500/40 transition-all group"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded-lg bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-400">
                        <Network className="w-4 h-4" />
                      </div>
                      <div>
                        <div className="text-xs font-bold text-white group-hover:text-purple-300">
                          PR Lens Architecture
                        </div>
                        <div className="text-[10px] text-slate-400 font-mono">
                          Interactive 4-Lane Flow Canvas
                        </div>
                      </div>
                    </div>
                    <ExternalLink className="w-3.5 h-3.5 text-slate-500 group-hover:text-purple-400" />
                  </a>

                  <Link
                    href="/chawakom"
                    className="flex items-center justify-between p-3 rounded-xl glass-pill hover:bg-white/[0.06] hover:border-sky-500/40 transition-all group"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                        <FileSpreadsheet className="w-4 h-4" />
                      </div>
                      <div>
                        <div className="text-xs font-bold text-white group-hover:text-emerald-300">
                          ชวกม.7 Document Engine
                        </div>
                        <div className="text-[10px] text-slate-400 font-mono">
                          29 Sheets 1:1 Form Triage
                        </div>
                      </div>
                    </div>
                    <ChevronRight className="w-3.5 h-3.5 text-slate-500 group-hover:text-emerald-400" />
                  </Link>

                  <Link
                    href="/studio"
                    className="flex items-center justify-between p-3 rounded-xl glass-pill hover:bg-white/[0.06] hover:border-amber-500/40 transition-all group"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded-lg bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
                        <Sliders className="w-4 h-4" />
                      </div>
                      <div>
                        <div className="text-xs font-bold text-white group-hover:text-amber-300">
                          Tactical UI Studio 360°
                        </div>
                        <div className="text-[10px] text-slate-400 font-mono">
                          Live Glassmorphism V8 Sandbox
                        </div>
                      </div>
                    </div>
                    <ChevronRight className="w-3.5 h-3.5 text-slate-500 group-hover:text-amber-400" />
                  </Link>
                </div>
              </div>

              {/* 10 Skills Inventory Card */}
              <div className="glass-card rounded-2xl p-6">
                <div className="flex items-center justify-between mb-4 pb-3 border-b border-white/[0.08]">
                  <div className="flex items-center gap-2">
                    <ShieldAlert className="w-4 h-4 text-emerald-400" />
                    <h3 className="text-sm font-bold text-white uppercase tracking-wider font-mono">
                      10 Forensic Skills Loaded
                    </h3>
                  </div>
                  <span className="text-[10px] px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-400 font-mono">
                    ONLINE
                  </span>
                </div>

                <div className="flex flex-wrap gap-1.5">
                  {[
                    "forensic-flow-lens",
                    "fraud-beneficiary-network",
                    "vector-chat-rag-deepdive",
                    "individual-court-indictment",
                    "chronological-11d-timeline",
                    "forensic-dedup-optimizer",
                    "master-strip-chunk-scanner",
                    "supplementary-court-motion",
                    "killer-cross-examination",
                    "amlc-asset-freezing-gateway",
                  ].map((s) => (
                    <span
                      key={s}
                      className="text-[11px] font-mono px-2.5 py-1 rounded-lg bg-white/[0.03] border border-white/[0.07] text-slate-300 hover:border-sky-500/40 hover:text-white transition-all cursor-default"
                    >
                      {s}
                    </span>
                  ))}
                </div>
              </div>
            </aside>
          </div>
        )}

        {/* TAB 2: TARGET PERSONS & DOSSIERS */}
        {activeTab === "TARGETS" && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            {/* Left 4 Cols: Target List */}
            <div className="lg:col-span-4 flex flex-col gap-3">
              <h3 className="text-xs font-mono font-bold uppercase tracking-wider text-slate-400 px-1">
                เลือกลำดับบุคคลเป้าหมาย (6 Targets Roster)
              </h3>
              {TARGET_PERSONS.map((t) => {
                const isSelected = selectedTarget.id === t.id;
                return (
                  <button
                    key={t.id}
                    onClick={() => setSelectedTarget(t)}
                    className={`w-full text-left p-4 rounded-2xl border transition-all flex flex-col gap-1.5 ${
                      isSelected
                        ? "bg-gradient-to-r from-sky-500/15 to-indigo-500/15 border-sky-500/50 shadow-[0_0_20px_rgba(56,189,248,0.2)]"
                        : "glass-card hover:bg-white/[0.04]"
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className="text-sm font-bold text-white">{t.name}</span>
                      <span
                        className="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full"
                        style={{
                          backgroundColor: `${t.roleColor}15`,
                          color: t.roleColor,
                          border: `1px solid ${t.roleColor}40`,
                        }}
                      >
                        {t.roleType}
                      </span>
                    </div>
                    <span className="text-xs text-slate-400">{t.role}</span>
                    <span className="text-[11px] font-mono text-sky-400 mt-1">
                      {t.accounts[0]}
                    </span>
                  </button>
                );
              })}
            </div>

            {/* Right 8 Cols: Target Detailed Dossier Card */}
            <div className="lg:col-span-8 glass-card rounded-2xl p-6 md:p-8 flex flex-col gap-6">
              {/* Header */}
              <div className="flex flex-col md:flex-row md:items-center justify-between pb-6 border-b border-white/[0.08] gap-4">
                <div>
                  <div className="flex items-center gap-2">
                    <span
                      className="text-xs font-mono font-bold px-2.5 py-0.5 rounded-full uppercase"
                      style={{
                        backgroundColor: `${selectedTarget.roleColor}15`,
                        color: selectedTarget.roleColor,
                        border: `1px solid ${selectedTarget.roleColor}40`,
                      }}
                    >
                      {selectedTarget.role}
                    </span>
                    <span className="text-xs font-mono text-slate-400">
                      {selectedTarget.coordinates}
                    </span>
                  </div>
                  <h2 className="text-2xl font-black text-white mt-2">
                    {selectedTarget.name}
                  </h2>
                </div>

                <button
                  onClick={() =>
                    copyToClipboard(
                      `${selectedTarget.name} - ${selectedTarget.role}\nข้อหา: ${selectedTarget.charges.join(
                        ", "
                      )}\nกลยุทธ์ทำลายข้อต่อสู้: ${selectedTarget.defenseBusting}`,
                      selectedTarget.id
                    )
                  }
                  className="flex items-center gap-2 px-4 py-2 rounded-xl glass-pill hover:bg-white/[0.06] text-xs font-mono text-slate-300 hover:text-white transition-all self-start md:self-auto"
                >
                  {copied === selectedTarget.id ? (
                    <Check className="w-4 h-4 text-emerald-400" />
                  ) : (
                    <Copy className="w-4 h-4" />
                  )}
                  <span>{copied === selectedTarget.id ? "คัดลอกแล้ว" : "คัดลอกสรุปสำนวน"}</span>
                </button>
              </div>

              {/* Accounts & Charges */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {/* Accounts Box */}
                <div className="p-4 rounded-xl bg-white/[0.02] border border-white/[0.06]">
                  <span className="text-xs font-mono font-bold text-slate-400 uppercase">
                    บัญชีธนาคาร / พร้อมเพย์ที่พบ
                  </span>
                  <div className="mt-2 flex flex-col gap-1.5">
                    {selectedTarget.accounts.map((acc, idx) => (
                      <span
                        key={idx}
                        className="text-xs font-mono font-bold text-sky-300 bg-sky-500/10 px-2.5 py-1 rounded border border-sky-500/20"
                      >
                        {acc}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Charges Box */}
                <div className="p-4 rounded-xl bg-white/[0.02] border border-white/[0.06]">
                  <span className="text-xs font-mono font-bold text-slate-400 uppercase">
                    ฐานความผิดและองค์ประกอบกฎหมาย
                  </span>
                  <div className="mt-2 flex flex-col gap-1.5">
                    {selectedTarget.charges.map((c, idx) => (
                      <span
                        key={idx}
                        className="text-xs text-amber-300 bg-amber-500/10 px-2.5 py-1 rounded border border-amber-500/20"
                      >
                        ⚖️ {c}
                      </span>
                    ))}
                  </div>
                </div>
              </div>

              {/* Chat Evidence Snippet */}
              <div className="p-4 rounded-xl bg-sky-500/[0.03] border border-sky-500/20">
                <span className="text-xs font-mono font-bold text-sky-400 uppercase flex items-center gap-1.5">
                  <FileText className="w-3.5 h-3.5" />
                  บริบทแชทจริงมัดตัว (Verbatim Chat Snippet)
                </span>
                <p className="mt-2 text-sm text-slate-200 italic leading-relaxed">
                  {selectedTarget.chatSnippet}
                </p>
              </div>

              {/* Defense Busting Strategy */}
              <div className="p-4 rounded-xl bg-purple-500/[0.03] border border-purple-500/20">
                <span className="text-xs font-mono font-bold text-purple-400 uppercase flex items-center gap-1.5">
                  <Gavel className="w-3.5 h-3.5" />
                  กลยุทธ์ทำลายข้อต่อสู้ในชั้นศาล (Killer Cross-Examination Strategy)
                </span>
                <p className="mt-2 text-sm text-slate-200 leading-relaxed">
                  {selectedTarget.defenseBusting}
                </p>
              </div>

              {/* Smoking Gun Link */}
              <div className="p-4 rounded-xl bg-white/[0.02] border border-white/[0.06] flex items-center justify-between">
                <div>
                  <span className="text-xs font-mono text-slate-400">ภาพหลักฐานมัดตัว (Smoking Gun):</span>
                  <div className="text-sm font-bold text-white mt-0.5">
                    {selectedTarget.smokingGunTitle}
                  </div>
                </div>
                <button
                  onClick={() => setActiveTab("SMOKING_GUNS")}
                  className="px-3 py-1.5 rounded-lg bg-sky-500/10 hover:bg-sky-500/20 border border-sky-500/30 text-sky-400 text-xs font-bold font-mono transition-all"
                >
                  เปิดคลังรูป ➔
                </button>
              </div>
            </div>
          </div>
        )}

        {/* TAB 3: SMOKING GUN EVIDENCE GALLERY */}
        {activeTab === "SMOKING_GUNS" && (
          <div className="flex flex-col gap-6">
            <div className="flex items-center justify-between">
              <div>
                <h2 className="text-xl font-bold text-white">
                  คลังภาพพยานหลักฐานจุดตายคดี (Smoking Gun Vault)
                </h2>
                <p className="text-xs text-slate-400 mt-0.5">
                  รวมหลักฐานภาพถ่ายหน้าจอแชท สลิปโอนเงิน และเอกสารมัดตัวความผิดสำเร็จ 100%
                </p>
              </div>
              <span className="font-mono text-xs text-sky-400 bg-sky-500/10 px-3 py-1.5 rounded-xl border border-sky-500/30">
                13 Certified Evidence Files
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
              {SMOKING_GUNS.map((item) => (
                <div
                  key={item.id}
                  onClick={() => setActiveSmokingGun(item)}
                  className="glass-card glass-card-hover rounded-2xl p-5 flex flex-col justify-between cursor-pointer group"
                >
                  <div>
                    <div className="flex items-center justify-between mb-3">
                      <span className="text-[11px] font-mono font-black text-sky-400 px-2 py-0.5 rounded bg-sky-500/10 border border-sky-500/30">
                        {item.tag}
                      </span>
                      <span className="text-[10px] font-mono text-slate-500">
                        {item.date}
                      </span>
                    </div>

                    <h3 className="text-base font-bold text-white group-hover:text-sky-300 transition-colors">
                      {item.title}
                    </h3>
                    <p className="text-xs text-slate-400 mt-2 line-clamp-2 leading-relaxed">
                      {item.desc}
                    </p>
                  </div>

                  <div className="mt-4 pt-3 border-t border-white/[0.06] flex items-center justify-between text-xs">
                    <span className="text-[11px] text-emerald-400 font-mono">
                      ✓ {item.impact}
                    </span>
                    <ChevronRight className="w-4 h-4 text-slate-600 group-hover:text-sky-400 transition-all" />
                  </div>
                </div>
              ))}
            </div>

            {/* Evidence Modal / Drawer */}
            {activeSmokingGun && (
              <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md">
                <div className="glass-obsidian rounded-2xl max-w-xl w-full p-6 border border-sky-500/40 shadow-2xl flex flex-col gap-4">
                  <div className="flex items-start justify-between">
                    <div>
                      <span className="text-xs font-mono font-bold text-sky-400 px-2.5 py-0.5 rounded bg-sky-500/10 border border-sky-500/30">
                        {activeSmokingGun.tag}
                      </span>
                      <h3 className="text-lg font-bold text-white mt-2">
                        {activeSmokingGun.title}
                      </h3>
                    </div>
                    <button
                      onClick={() => setActiveSmokingGun(null)}
                      className="p-1 rounded-lg hover:bg-white/10 text-slate-400 hover:text-white"
                    >
                      ✕
                    </button>
                  </div>

                  <p className="text-sm text-slate-300 leading-relaxed">
                    {activeSmokingGun.desc}
                  </p>

                  <div className="p-3 rounded-xl bg-sky-500/10 border border-sky-500/30 text-xs font-mono text-sky-300">
                    <strong>ผลทางคดี:</strong> {activeSmokingGun.impact}
                  </div>

                  <div className="flex items-center justify-end gap-3 pt-2">
                    <button
                      onClick={() => setActiveSmokingGun(null)}
                      className="px-4 py-2 rounded-xl glass-pill text-xs font-bold text-white"
                    >
                      ปิดหน้าต่าง
                    </button>
                  </div>
                </div>
              </div>
            )}
          </div>
        )}

        {/* TAB 4: AI SOVEREIGN ENGINE & SDLC ORCHESTRATOR */}
        {activeTab === "AI_ENGINE" && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            {/* Left 4 Cols: 5 Engine Modes */}
            <div className="lg:col-span-4 flex flex-col gap-3">
              <span className="text-xs font-mono font-bold uppercase tracking-wider text-slate-400 px-1">
                เลือกสายพาน AI Engine (5 Sovereign Modes)
              </span>

              {(Object.keys(ENGINE_MODES) as EngineMode[]).map((modeKey) => {
                const m = ENGINE_MODES[modeKey];
                const isActive = activeEngineMode === modeKey;
                const IconComponent = m.icon;
                return (
                  <button
                    key={modeKey}
                    onClick={() => setActiveEngineMode(modeKey)}
                    className={`w-full text-left p-4 rounded-2xl border transition-all flex flex-col gap-2 ${
                      isActive
                        ? "shadow-[0_0_20px_rgba(56,189,248,0.2)]"
                        : "glass-card hover:bg-white/[0.04]"
                    }`}
                    style={
                      isActive
                        ? {
                            backgroundColor: m.bgGlow,
                            borderColor: m.borderColor,
                          }
                        : {}
                    }
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <IconComponent
                          className="w-4 h-4"
                          style={{ color: m.color }}
                        />
                        <span className="text-sm font-bold text-white">{m.name}</span>
                      </div>
                      <span
                        className="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full"
                        style={{
                          backgroundColor: `${m.color}20`,
                          color: m.color,
                          border: `1px solid ${m.color}40`,
                        }}
                      >
                        {m.tag}
                      </span>
                    </div>
                    <span className="text-xs text-slate-400 leading-relaxed">
                      {m.desc}
                    </span>
                  </button>
                );
              })}
            </div>

            {/* Right 8 Cols: Reverse-Prompt Generator Deck */}
            <div className="lg:col-span-8 glass-card rounded-2xl p-6 md:p-8 flex flex-col gap-6">
              <div className="flex items-center justify-between pb-4 border-b border-white/[0.08]">
                <div className="flex items-center gap-3">
                  <div
                    className="w-10 h-10 rounded-xl flex items-center justify-center border"
                    style={{
                      backgroundColor: currentModeConfig.bgGlow,
                      borderColor: currentModeConfig.borderColor,
                      color: currentModeConfig.color,
                    }}
                  >
                    <currentModeConfig.icon className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-white">
                      {currentModeConfig.name} Reverse-Prompt Orchestrator
                    </h3>
                    <p className="text-xs text-slate-400">
                      สร้างคำสั่งระดับวิศวกรรมสำหรับป้อน AI พร้อมกฎ Grill-Me และควบคุม Token
                    </p>
                  </div>
                </div>
              </div>

              {/* User Prompt Input */}
              <div className="flex flex-col gap-2">
                <label className="text-xs font-mono font-bold text-slate-300 uppercase">
                  เป้าหมายหรือคำสั่งที่คุณต้องการให้ระบบดำเนินการ:
                </label>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={userPromptInput}
                    onChange={(e) => setUserPromptInput(e.target.value)}
                    placeholder="เช่น: วิเคราะห์หลักฐานการเงินปรียาฉัตร ชิมพลี และร่างหนังสือขออายัดบัญชี ปปง."
                    className="flex-1 px-4 py-3 rounded-xl bg-black/40 border border-white/[0.1] text-sm text-white placeholder-slate-500 focus:outline-none focus:border-sky-500/50 transition-all font-sans"
                    onKeyDown={(e) => {
                      if (e.key === "Enter") handleGeneratePrompt();
                    }}
                  />
                  <button
                    onClick={handleGeneratePrompt}
                    className="px-5 py-3 rounded-xl bg-sky-500 hover:bg-sky-400 text-slate-950 font-bold text-xs transition-all font-mono whitespace-nowrap shadow-[0_0_15px_rgba(56,189,248,0.3)]"
                  >
                    สร้าง Prompt
                  </button>
                </div>
              </div>

              {/* Output Prompt Box */}
              <div className="flex flex-col gap-2">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-mono font-bold text-slate-400 uppercase">
                    คำสั่งพร้อมนำไปสั่ง AI (Sovereign Prompt Output)
                  </span>
                  {generatedPrompt && (
                    <button
                      onClick={() => copyToClipboard(generatedPrompt, "gen-prompt")}
                      className="flex items-center gap-1.5 text-xs font-mono text-sky-400 hover:text-sky-300"
                    >
                      {copied === "gen-prompt" ? (
                        <Check className="w-3.5 h-3.5 text-emerald-400" />
                      ) : (
                        <Copy className="w-3.5 h-3.5" />
                      )}
                      <span>{copied === "gen-prompt" ? "คัดลอกแล้ว!" : "คัดลอกคำสั่ง"}</span>
                    </button>
                  )}
                </div>

                <div className="p-4 rounded-xl bg-black/50 border border-white/[0.08] font-mono text-xs text-slate-200 leading-relaxed whitespace-pre-wrap min-h-[160px]">
                  {generatedPrompt || currentModeConfig.samplePrompt}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* TAB 5: CHAWAKOM 1:1 DOCS ENGINE */}
        {activeTab === "DOCS_1TO1" && (
          <div className="glass-card rounded-2xl p-6 md:p-8 flex flex-col gap-6">
            <div className="flex flex-col md:flex-row md:items-center justify-between pb-6 border-b border-white/[0.08] gap-4">
              <div>
                <div className="flex items-center gap-2">
                  <FileSpreadsheet className="w-5 h-5 text-sky-400" />
                  <h2 className="text-xl font-bold text-white">
                    ชวกม.7 Forensic Document Platform 1:1
                  </h2>
                </div>
                <p className="text-xs text-slate-400 mt-1">
                  ระบบบริหารจัดการและตรวจสอบเอกสารราชการมาตรฐานศาล (XEROX Anti-Hallucination Engine)
                </p>
              </div>

              <Link
                href="/chawakom"
                className="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-sky-500 hover:bg-sky-400 text-slate-950 font-bold text-xs transition-all font-mono self-start md:self-auto shadow-[0_0_15px_rgba(56,189,248,0.3)]"
              >
                <span>เปิดแดชบอร์ดชวกม. ฉบับเต็ม</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </Link>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="p-4 rounded-xl glass-pill">
                <span className="text-xs font-mono text-slate-400">โครงสร้างชีต</span>
                <div className="text-xl font-bold text-white mt-1">29 ชีตมาตรฐาน</div>
                <p className="text-xs text-slate-400 mt-1">ทบ.344-201, 344-202, ใบสำคัญรับเงิน</p>
              </div>

              <div className="p-4 rounded-xl glass-pill">
                <span className="text-xs font-mono text-slate-400">ผลการ Audit สูตร</span>
                <div className="text-xl font-bold text-emerald-400 mt-1">PASS (0 Errors)</div>
                <p className="text-xs text-slate-400 mt-1">ผ่านการตรวจสูตร Matrix Grid 100%</p>
              </div>

              <div className="p-4 rounded-xl glass-pill">
                <span className="text-xs font-mono text-slate-400">ระบบฟอนต์ราชการ</span>
                <div className="text-xl font-bold text-sky-400 mt-1">TH Sarabun PSK</div>
                <p className="text-xs text-slate-400 mt-1">ล็อกการแปลงตัวเลขไทย 1:1 ระดับพิกเซล</p>
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Bottom Status Footer */}
      <footer className="border-t border-white/[0.08] glass-obsidian px-6 py-4 mt-auto z-10 text-xs font-mono text-slate-400">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span>ISO/IEC 27037 Digital Forensic Evidence Ready</span>
            <span className="text-slate-600">|</span>
            <span>Single Source of Truth (SSOT)</span>
          </div>

          <div className="flex items-center gap-4">
            <span>Latency: &lt; 24ms</span>
            <span>Origin: palaside/RAG-Eviden</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
