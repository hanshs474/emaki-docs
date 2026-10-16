# emaki API and SDKs

Official API and SDK documentation for emaki (emaki.ai), the Japanese-language AI video generator for Seedance 2.5 and Seedance 2.0.

[emaki](https://emaki.ai/?utm_source=readthedocs&utm_medium=docs) runs [Seedance 2.5](https://emaki.ai/seedance-2-5), [Seedance 2.0](https://emaki.ai/seedance-2) and a handful of image models behind one account. The same API key that the website gives you runs them from your own code: text to video, [image to video](https://emaki.ai/image-to-video) with a first frame you pass in, and images for that first frame. Finished clips can be sharpened with the [AI video upscaler](https://emaki.ai/video-upscaler) on the site.

日本語での使い方は [シーダンス](https://emaki.ai/) へ。

## Start in three steps

1. Sign in on [emaki.ai](https://emaki.ai/?utm_source=readthedocs&utm_medium=docs).
2. Create a key at [emaki.ai/settings/apikeys](https://emaki.ai/settings/apikeys).
3. `export EMAKI_API_KEY=sk-...` and call the API, an [SDK](sdk/README.md) or the [MCP server](integrations/mcp.md).

```bash
curl -s -X POST https://emaki.ai/api/video/ai \
  -H "Authorization: Bearer $EMAKI_API_KEY" -H "Content-Type: application/json" \
  -d '{"prompt":"a paper boat drifting on a calm lake at sunrise, slow dolly in","model":"seedance_2_5","parameters":{"duration":5}}'
```

Every run costs credits on your emaki account, the same price as on the website. Checking the balance is free.

## What every client does

1. `POST /api/video/ai` with a prompt, a model id and parameters; keep the returned `id`.
2. `POST /api/video/status` every 5 seconds until `status` is `completed` (the file URL is in `videoUrl`) or `failed`.

The [HTTP API](http.md) page describes both calls and every error, the [models](models.md) page lists ids and parameters.
