// @ts-check
import { defineConfig } from 'astro/config';

const site = process.env.SITE || 'http://localhost:4321';

// https://astro.build/config
export default defineConfig({
  site,
  base: site.includes('github.io') ? '/parish-template' : '/',
});
