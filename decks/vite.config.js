import { defineDeckConfig } from 'deck-engine/vite';

// The engine — reveal.js setup, styles, deck assembly — lives in
// https://codeberg.org/open-source-ecosystem/deck-engine. Only what this
// repository's decks share is declared here.
export default defineDeckConfig({
  root: import.meta.dirname,
  site: {
    logo: 'assets/bfh-logo.svg',
    logoAlt: 'BFH',
    links: [
      { href: 'https://www.bfh.ch/de/forschung/forschungsbereiche/public-sector-transformation/', text: 'Institute for Public Sector Transformation' },
      { href: 'mailto:lukas.smith@bfh.ch', text: 'lukas.smith@bfh.ch' },
      { href: 'https://mastodon.green/@lsmith', text: '@lsmith@mastodon.green', rel: 'me' },
    ],
  },
});
