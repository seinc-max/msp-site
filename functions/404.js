export async function onRequest(context) {
  const asset = await context.env.ASSETS.fetch(context.request);
  const headers = new Headers(asset.headers);
  headers.set("cache-control", "no-store");
  return new Response(asset.body, {
    status: 404,
    statusText: "Not Found",
    headers,
  });
}
