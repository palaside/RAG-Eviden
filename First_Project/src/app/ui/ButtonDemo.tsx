export default function ButtonDemo() {
  return (
    <button
      className="px-4 py-2 bg-sky-500 hover:bg-sky-600 text-white rounded font-medium transition-colors"
      onClick={() => alert("Clicked!")}
    >
      ปุ่มตัวอย่าง
    </button>
  );
}

