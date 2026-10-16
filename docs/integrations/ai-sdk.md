# Vercel AI SDK

[`emaki-ai-provider`](https://www.npmjs.com/package/emaki-ai-provider) is an AI SDK provider: `emaki.video()` works with `experimental_generateVideo`, `emaki.image()` with `generateImage`.

```bash
npm install emaki-ai-provider ai
export EMAKI_API_KEY=sk-...   # https://emaki.ai/settings/apikeys
```

```ts
import { experimental_generateVideo as generateVideo } from 'ai';
import { emaki } from 'emaki-ai-provider';

const { video } = await generateVideo({
  model: emaki.video(),   // seedance_2_5
  prompt: 'a paper boat drifting down a rain gutter, low angle',
  duration: 5,
  resolution: '1280x720',
  image: 'https://example.com/first-frame.png',   // optional: image to video
});
```

`resolution` is mapped to the short side (`1280x720` → `720p`); `frameImages` with `last_frame` sets the closing frame; `providerOptions.emaki` passes any other model parameter through. Failures throw `EmakiError` with a `reason` (`auth`, `quota`, `plan`, `busy`, `rejected`, `failed`, `timeout`).

Default video model: [Seedance 2.5](https://emaki.ai/seedance-2-5). Other ids are on [Models and parameters](../models.md).

Source: [hanshs474/emaki-ai-provider](https://github.com/hanshs474/emaki-ai-provider).
