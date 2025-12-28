import type { NextConfig } from "next";
import path from "path";
// @ts-ignore - The plugin likely lacks type definitions
import WasmPackPlugin from "@wasm-tool/wasm-pack-plugin";

const nextConfig: NextConfig = {
  webpack: (config) => {
    // 1. Enable WebAssembly experiments
    config.experiments = {
      ...config.experiments,
      asyncWebAssembly: true,
      layers: true,
    };

    // 2. Add the WasmPackPlugin
    // We use process.cwd() because __dirname is not available in ES modules
    config.plugins.push(
      new WasmPackPlugin({
        crateDirectory: path.resolve(process.cwd(), "visualizer_core"),
        outDir: path.resolve(process.cwd(), "visualizer_core/pkg"),
      }),
    );

    return config;
  },
};

export default nextConfig;
