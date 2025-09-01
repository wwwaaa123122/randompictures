let cache = null;

export default {
  async fetch(request) {
    // 如果缓存为空，调用 GitHub API 获取仓库图片列表
    if (!cache) {
      const repo = "wwwaaa123122/randompictures";   // GitHub 仓库
      const path = "public";              // 仓库中存放图片的目录
      const apiUrl = `https://api.github.com/repos/${repo}/contents/${path}`;

      const resp = await fetch(apiUrl, {
        headers: { "User-Agent": "Random-Image-API" }
      });

      if (!resp.ok) {
        return new Response("GitHub API 请求失败", { status: 500 });
      }

      const data = await resp.json();

      cache = data
        .filter(f => f.type === "file")
        .map(f => ({
          url: f.download_url,
          ext: f.name.split(".").pop().toLowerCase()
        }));
    }

    // 随机选一张
    const file = cache[Math.floor(Math.random() * cache.length)];

    // 获取图片内容
    const imgResp = await fetch(file.url);
    let contentType = imgResp.headers.get("content-type");

    // 如果 GitHub 没给 Content-Type，则根据扩展名兜底
    if (!contentType) {
      if (file.ext === "png") contentType = "image/png";
      else if (file.ext === "gif") contentType = "image/gif";
      else if (file.ext === "webp") contentType = "image/webp";
      else contentType = "image/jpeg";
    }

    return new Response(await imgResp.arrayBuffer(), {
      headers: { "Content-Type": contentType }
    });
  }
}