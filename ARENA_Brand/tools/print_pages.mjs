// Print 1600x900 HTML pages to PDF + per-page PNGs with the preinstalled Playwright Chromium.
import {createRequire} from 'node:module';
const require = createRequire(import.meta.url);
const {chromium} = require('playwright');
const b = await chromium.launch();
for (const html of process.argv.slice(2)) {
  const p = await b.newPage({viewport: {width: 1600, height: 900}});
  await p.goto('file://' + html);
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({path: html.replace(/\.html$/, '.pdf'), width: '1600px', height: '900px', printBackground: true});
  const els = await p.$$('section.pg');
  for (let i = 0; i < els.length; i++) {
    await els[i].screenshot({path: html.replace(/\.html$/, `_${String(i + 1).padStart(2, '0')}.png`)});
  }
  console.log('printed', html, els.length);
}
await b.close();
