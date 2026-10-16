# Dify

The emaki Dify plugin ([source](https://github.com/hanshs474/emaki-dify-plugin)) adds three tools to workflows and agents:

| Tool | What it does |
|---|---|
| `generate_video` | Prompt (and optional first-frame URL) in, clip URL out; [Seedance 2.5](https://emaki.ai/seedance-2-5) by default |
| `generate_image` | Prompt in, image URL out |
| `check_status` | Run id in, clip URL out once ready |

`generate_video` waits about four minutes, under Dify's tool timeout; a longer run returns its run id for `check_status`. Paste a key from [emaki.ai/settings/apikeys](https://emaki.ai/settings/apikeys) into the plugin's credentials; validation reads the balance and costs nothing.
