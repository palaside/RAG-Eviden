"use client";
import { Power } from "lucide-react";

export default function EngineStarter() {
  const startEngine = async () => {
    try {
      const res = await fetch('/api/start');
      const data = await res.json();
      alert(data.status);
    } catch (e) {
      alert('Error starting engine');
    }
  };

  return (
    <button
      onClick={startEngine}
      className="flex items-center gap-2 p-2 bg-gray-800 rounded-full hover:bg-gray-700"
      title="Start Full Engine"
    >
      <Power className="w-6 h-6 text-white" />
    </button>
  );
}

