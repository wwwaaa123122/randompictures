let cache = null;

export default {
  async fetch(request) {
    // 首次加载时从 GitHub API 拉取文件列表
    if (!cache) {
      const repo = "wwwaaa123122/randompictures";   // 你的 GitHub 仓库
      const path = "public";              // 图片目录（对应 Vercel 的 public）
      const apiUrl = `https://api.github.com/repos/${repo}/contents/${path}`;

      const resp = await fetch(apiUrl, {
        headers: { "User-Agent": "Cloudflare-Worker" }
      });
      const data = await resp.json();

      // 只取图片类型文件
      cache = data
        .filter(f => f.type === "file")
        .map(f => f.download_url);
    }

    // 随机选一张
    const url = cache[Math.floor(Math.random() * cache.length)];

    // 获取图片内容
    const imgResp = await fetch(url);
    const contentType = imgResp.headers.get("content-type") || "image/jpeg";

    return new Response(await imgResp.arrayBuffer(), {
      headers: { "Content-Type": contentType }
    });
  }
}