// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import { themes as prismThemes } from "prism-react-renderer";

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "CS50AI Notes",
  tagline: "Dinosaurs are cool",
  favicon: "images/favicon.ico",

  url: "https://cs50ai.shahtech.info",
  baseUrl: "/",

  organizationName: "busycaesar",
  projectName: "Harvard_CS50AI",
  deploymentBranch: "Deployment",
  trailingSlash: false,

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  staticDirectories: ["static"],

  presets: [
    [
      "classic",
      {
        docs: {
          path: "docs",
          routeBasePath: "/",
          sidebarPath: "./sidebars.js",
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: "CS50AI Notes",
      logo: {
        alt: "My Site Logo",
        src: "images/logo.svg",
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "sections",
          position: "left",
          label: "Learn",
        },
        {
          href: "https://github.com/busycaesar/Harvard_CS50AI",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Community",
          items: [
            {
              label: "X",
              href: "https://x.com/busycaesar",
            },
            {
              label: "GitHub",
              href: "https://github.com/busycaesar",
            },
            {
              label: "LinkedIn",
              href: "https://linkedin.com/in/busycaesar",
            },
          ],
        },
        {
          title: "More",
          items: [
            {
              label: "Blogs",
              href: "https://dev.to/busycaesar",
            },
            {
              label: "YouTube",
              href: "https://youtube.com/@busycaesar",
            },
            {
              label: "Instagram",
              href: "https://instagram.com/busycaesar",
            },
          ],
        },
        {
          title: "Support",
          items: [
            {
              label: "Buy Me a Coffee",
              href: "https://buymeacoffee.com/busycaesar",
            },
            {
              label: "Topmate",
              href: "https://topmate.io/busycaesar",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} shahtech.info. All Rights Reserved.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },
};

export default config;
