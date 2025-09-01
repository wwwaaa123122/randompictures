import fs from "fs";
import path from "path";

export default function handler(req, res) {
  const dirPath = path.join(process.cwd(), "public"); // public 目录
  const files = fs.readdirSync(dirPath).filter(f => !f.startsWith("."));

  if (files.length === 0) {
    res.status(404).send("No images found");
    return;
  }

  const randomFile = files[Math.floor(Math.random() * files.length)];
  const filePath = path.join(dirPath, randomFile);

  // 设置合适的 Content-Type
  const ext = path.extname(randomFile).toLowerCase();
  let type = "image/jpeg";
  if (ext === ".png") type = "image/png";
  if (ext === ".gif") type = "image/gif";
  if (ext === ".webp") type = "image/webp";

  const img = fs.readFileSync(filePath);
  res.setHeader("Content-Type", type);
  res.send(img);
}