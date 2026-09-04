/**
 * vite.config.js — nTrust.ai Customer Dashboard build config (Weaver 2026-09-04)
 * Binds 0.0.0.0 so containers are externally reachable (localhost-bind trap guard).
 * Deploy target: port 55127 (Revenue Operations Center) per platform convention;
 * fallback 5173 for local previews.
 */
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 55127,
    strictPort: false,
    hmr: false
  },
  preview: {
    host: '0.0.0.0',
    port: 55127
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
    chunkSizeWarningLimit: 900,
    rollupOptions: {
      output: {
        manualChunks: {
          react: ['react', 'react-dom'],
          router: ['react-router-dom']
        }
      }
    }
  }
});
