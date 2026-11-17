import { NextResponse } from 'next/server';
import { spawn } from 'child_process';

export async function GET() {
  // ใช้ PowerShell เพื่อรันสคริปต์ start‑engine.ps1 ภายใน First_Project
  const proc = spawn('powershell', ['-ExecutionPolicy', 'Bypass', '-File', 'scripts/start-engine.ps1'], {
    detached: true,
    stdio: 'ignore',
    cwd: process.cwd(), // project root of First_Project
  });
  proc.unref(); // ปลดจาก parent process เพื่อให้ API ตอบเร็ว
  return NextResponse.json({ status: 'engine started' });
}

