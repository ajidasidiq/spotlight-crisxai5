// Spotlight @crisxai5 entry (Node 22, standard library only).
//
// The entry is the X post itself: a public post carrying the spotlight
// graphic, @crisxai5, and one of the entrant's make.fun play codes. The
// house reads the post's engagement from X; this program's only job is to
// hand the post's address over, by copying POST.json from the repository
// root into the output directory where the gate reads it.
//
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const repoDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = join(repoDir, "POST.json");
const target = join(outDir, "POST.json");

if (!existsSync(source)) {
  console.error(`no POST.json found in ${repoDir}`);
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
console.log(`POST.json -> ${target}`);
