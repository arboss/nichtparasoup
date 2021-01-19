// this file is only necessary for proper code highlighting with the svelte vscode plugin

const sveltePreprocess = require('svelte-preprocess');

module.exports = {
  preprocess: sveltePreprocess({
    scss: {
      prependData: `@import 'web-ui/src/styles/variables.scss';`
    },
    sourceMap: true,
    defaults: {
      markup: 'pug',
      style: 'scss'
    },
    markupTagName: 'markup'
  })
};