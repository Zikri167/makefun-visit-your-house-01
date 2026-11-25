// main.ts — entry program for "Convince the AI Judge to Visit Your House".
// Reads entry.png next to this file, validates it against the gate
// (whole PNG, at most 1,048,576 bytes, at most 1024x1024), then writes it to
// $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png) and prints the
// byte count, dimensions and sha256. Node 22, stdlib only, deterministic.
import { createHash } from "node:crypto";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const MAX_BYTES = 1048576;
const MAX_DIM = 1024;
const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

const here = dirname(fileURLToPath(import.meta.url));
const srcPath = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const outPath = join(outDir, "entry.png");

if (!existsSync(srcPath)) {
  console.error(`missing input image: ${srcPath}`);
  process.exit(1);
}

const buf = readFileSync(srcPath);

if (buf.length > MAX_BYTES) {
  console.error(`image too large: ${buf.length} bytes > ${MAX_BYTES}`);
  process.exit(1);
}
if (buf.length < 33 || !buf.subarray(0, 8).equals(PNG_SIGNATURE)) {
  console.error("input is not a PNG file");
  process.exit(1);
}
if (buf.toString("ascii", 12, 16) !== "IHDR") {
  console.error("PNG has no IHDR chunk");
  process.exit(1);
}
const width = buf.readUInt32BE(16);
const height = buf.readUInt32BE(20);
if (width === 0 || height === 0 || width > MAX_DIM || height > MAX_DIM) {
  console.error(`bad dimensions: ${width}x${height} (max ${MAX_DIM}x${MAX_DIM})`);
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
writeFileSync(outPath, buf);

// Read the file back and confirm the copy is byte-identical to the input.
const written = readFileSync(outPath);
if (!written.equals(buf)) {
  console.error("verification failed: written file differs from input");
  process.exit(1);
}

const sha256 = createHash("sha256").update(buf).digest("hex");
console.log(`wrote ${outPath}`);
console.log(`bytes: ${buf.length}`);
console.log(`dimensions: ${width}x${height}`);
console.log(`sha256: ${sha256}`);
console.log("verified: output is byte-identical to entry.png");
