import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// nTrust.ai dashboard UI modules — Weaver deliverable (2026-09-04)
// 0.0.0.0 bind per org rule (localhost bind trap); relative base for multi-path hosting.
export default defineConfig({
  plugins: [react()],
  base: './',
  build: { outDir: 'dist', sourcemap: false, target: 'es2020' },
  server: { host: '0.0.0.0', port: 5199 },
});
