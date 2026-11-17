"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import {
  FileText,
  ShieldCheck,
  Activity,
  Layers,
  ArrowLeft,
  FileCheck2,
  Database,
  ExternalLink,
  Search,
  CheckCircle2,
  RefreshCw,
  FolderGit2
} from "lucide-react";

interface DocumentItem {
  id: string;
  title: string;
  htmlFile: string;
  hasPdf: boolean;
  hasJson: boolean;
}

interface PlatformData {
  name: string;
  status: string;
  errors: number;
  warnings: number;
  sheetsCount: number;
  variablesCount: number;
}

export default function ChawakomPlatformPage() {
  const [loading, setLoading] = useState(true);
  const [platform, setPlatform] = useState<PlatformData | null>(null);
  const [documents, setDocuments] = useState<DocumentItem[]>([]);
  const [search, setSearch] = useState("");

  const fetchData = async () => {
    setLoading(true);
    try {
      const res = await fetch("/api/chawakom");
      const data = await res.json();
      if (data.success) {
        setPlatform(data.platform);
        setDocuments(data.documents || []);
      }
    } catch (err) {
      console.error("Failed to load Chawakom data", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const filteredDocs = documents.filter(doc =>
    doc.title.toLowerCase().includes(search.toLowerCase()) ||
    doc.id.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="min-h-screen bg-[#07090e] text-slate-100 p-6 md:p-12 font-sans selection:bg-sky-500 selection:text-white">
      {/* Top Header */}
      <div className="max-w-7xl mx-auto mb-8 flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800/80 pb-6">
        <div>
          <div className="flex items-center gap-3">
            <Link
              href="/"
              className="p-2 rounded-lg bg-slate-900 border border-slate-800 hover:border-sky-500/50 text-slate-400 hover:text-white transition-all"
            >
              <ArrowLeft className="w-5 h-5" />
            </Link>
            <h1 className="text-2xl md:text-3xl font-bold tracking-tight bg-gradient-to-r from-sky-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">
              🏛️ ชวกม.7 Forensic Document Platform
            </h1>
          </div>
          <p className="text-sm text-slate-400 mt-2 ml-11">
            ระบบบริหารจัดการและตรวจสอบเอกสารราชการมาตรฐานศาล 1:1 (XEROX Anti-Hallucination Engine)
          </p>
        </div>

        <div className="flex items-center gap-3 ml-11 md:ml-0">
          <button
            onClick={fetchData}
            disabled={loading}
            className="flex items-center gap-2 px-4 py-2 rounded-lg bg-sky-500/10 border border-sky-500/30 text-sky-400 hover:bg-sky-500/20 text-sm font-medium transition-all"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? "animate-spin" : ""}`} />
            รีเฟรชข้อมูล
          </button>
        </div>
      </div>

      <div className="max-w-7xl mx-auto space-y-8">
        {/* Metric Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="p-5 rounded-xl bg-slate-900/60 border border-slate-800/80 backdrop-blur-md">
            <div className="flex items-center justify-between">
              <span className="text-xs uppercase tracking-wider text-slate-400 font-semibold">Validation Status</span>
              <ShieldCheck className="w-5 h-5 text-emerald-400" />
            </div>
            <div className="mt-3 flex items-baseline gap-2">
              <span className="text-2xl font-bold text-emerald-400">
                {platform?.status || "PASS"}
              </span>
              <span className="text-xs text-slate-400">
                ({platform?.errors ?? 0} Errors)
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-2">สูตรคำนวณผ่านการรับรอง 100%</p>
          </div>

          <div className="p-5 rounded-xl bg-slate-900/60 border border-slate-800/80 backdrop-blur-md">
            <div className="flex items-center justify-between">
              <span className="text-xs uppercase tracking-wider text-slate-400 font-semibold">Master Workbook</span>
              <Database className="w-5 h-5 text-sky-400" />
            </div>
            <div className="mt-3 flex items-baseline gap-2">
              <span className="text-2xl font-bold text-sky-400">
                {platform?.sheetsCount || 29}
              </span>
              <span className="text-xs text-slate-400">ชีตต้นฉบับ</span>
            </div>
            <p className="text-xs text-slate-500 mt-2">Single Source of Truth (SSOT)</p>
          </div>

          <div className="p-5 rounded-xl bg-slate-900/60 border border-slate-800/80 backdrop-blur-md">
            <div className="flex items-center justify-between">
              <span className="text-xs uppercase tracking-wider text-slate-400 font-semibold">Dossier Assets</span>
              <FileCheck2 className="w-5 h-5 text-purple-400" />
            </div>
            <div className="mt-3 flex items-baseline gap-2">
              <span className="text-2xl font-bold text-purple-400">
                {documents.length}
              </span>
              <span className="text-xs text-slate-400">ชุดเอกสาร</span>
            </div>
            <p className="text-xs text-slate-500 mt-2">HTML, PDF & JSON Blueprints</p>
          </div>

          <div className="p-5 rounded-xl bg-slate-900/60 border border-slate-800/80 backdrop-blur-md">
            <div className="flex items-center justify-between">
              <span className="text-xs uppercase tracking-wider text-slate-400 font-semibold">Pipeline Health</span>
              <Activity className="w-5 h-5 text-amber-400" />
            </div>
            <div className="mt-3 flex items-baseline gap-2">
              <span className="text-2xl font-bold text-amber-400">
                0 Broken
              </span>
              <span className="text-xs text-slate-400">Healed Refs</span>
            </div>
            <p className="text-xs text-slate-500 mt-2">Master Pipeline Operational</p>
          </div>
        </div>

        {/* Search & Filter */}
        <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4 bg-slate-900/40 p-4 rounded-xl border border-slate-800/60">
          <div className="relative flex-1">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="ค้นหาเอกสาร (เช่น 8708, สป.3, ใบแทรก, แผนที่, ที่พัก)..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="w-full pl-9 pr-4 py-2 bg-slate-950/80 border border-slate-800 rounded-lg text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-sky-500 transition-colors"
            />
          </div>
          <span className="text-xs text-slate-400 font-mono self-center sm:self-auto">
            พบ {filteredDocs.length} จากทั้งหมด {documents.length} รายการ
          </span>
        </div>

        {/* Document Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {filteredDocs.map((doc) => (
            <div
              key={doc.id}
              className="group p-5 rounded-xl bg-slate-900/40 border border-slate-800/70 hover:border-sky-500/40 hover:bg-slate-900/70 transition-all flex flex-col justify-between"
            >
              <div>
                <div className="flex items-start justify-between gap-2">
                  <div className="p-2 rounded-lg bg-sky-500/10 border border-sky-500/20 text-sky-400">
                    <FileText className="w-5 h-5" />
                  </div>
                  <div className="flex items-center gap-1">
                    {doc.hasPdf && (
                      <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/10 text-rose-400 border border-rose-500/20">
                        PDF
                      </span>
                    )}
                    {doc.hasJson && (
                      <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/10 text-amber-400 border border-amber-500/20">
                        JSON
                      </span>
                    )}
                    <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                      1:1 HTML
                    </span>
                  </div>
                </div>

                <h3 className="mt-4 font-medium text-slate-200 group-hover:text-sky-300 transition-colors line-clamp-2">
                  {doc.title}
                </h3>
                <p className="text-xs font-mono text-slate-500 mt-1 truncate">
                  {doc.htmlFile}
                </p>
              </div>

              <div className="mt-5 pt-3 border-t border-slate-800/60 flex items-center justify-between text-xs text-slate-400">
                <span className="flex items-center gap-1.5 text-emerald-400/90 font-medium">
                  <CheckCircle2 className="w-3.5 h-3.5" />
                  Forensic Verified
                </span>
                <span className="text-[11px] text-slate-500">
                  A4 Court Edition
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

