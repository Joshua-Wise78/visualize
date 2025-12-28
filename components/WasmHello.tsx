"use client";

import { useEffect, useState } from "react";

export default function WasmHello() {
  const [wasm, setWasm] = useState<
    typeof import("../visualizer_core/pkg") | null
  >(null);
  const [result, setResult] = useState<number | null>(null);

  useEffect(() => {
    import("../visualizer_core/pkg").then((module) => {
      setWasm(module);
    });
  }, []);

  const handleClick = () => {
    if (wasm) {
      wasm.greet("Next.js");
    }
  };

  const calculate = () => {
    if (wasm) {
      const sum = wasm.add(20, 5);
      setResult(sum);
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>WebAssembly with Next.js</h2>
      <button
        onClick={handleClick}
        disabled={!wasm}
        style={{ padding: "10px 20px", fontSize: "16px" }}
      >
        {wasm ? "Greet World" : "Loading Wasm..."}
      </button>
      <br />
      <button
        onClick={calculate}
        className="bg-blue-500 text-white px-4 py-2 rounded mt-2"
        disabled={!wasm}
      >
        Add 20 + 5
      </button>
      {result !== null && (
        <p className="mt-2 text-xl">Result from WASM: {result}</p>
      )}
    </div>
  );
}
