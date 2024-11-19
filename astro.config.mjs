// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import tailwind from '@astrojs/tailwind';
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Tam\'s Cosmology Conundrums',
			social: {
				github: 'https://github.com/withastro/starlight',
			},
			head: [
				{tag: "script", attrs: {src:"https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.js", defer: true, crossorigin: "anonymous"}},
				{tag: "link", attrs: {rel: "stylesheet", href: "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.css", crossorigin: "anonymous"}}
			],
			sidebar: [
				{
					label: 'Cosmological Conundrums',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Redshifted photon energy', slug: 'redshifted_photons' },
					],
				}
			],
			customCss: ['./src/tailwind.css'],
		}),
		tailwind({ applyBaseStyles: false }),
	],
	markdown: {
		syntaxHighlight: "prism",
		remarkPlugins: [remarkMath],
		rehypePlugins: [rehypeKatex],
	},
});
