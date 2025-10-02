/// <reference types="vitest" />
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,              // 👉 agrega `expect`, `describe`, `it` automáticamente
    environment: "jsdom",       // 👉 simula navegador
    setupFiles: "./vitest.setup.js", // 👉 carga jest-dom
  },
});
