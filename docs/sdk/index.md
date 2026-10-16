# SDKs

Official SDK clients for emaki (emaki.ai), the Japanese-language AI video generator for Seedance 2.5 and Seedance 2.0. Every client has the same surface: `generate_video(prompt, model="seedance_2_5", ...)` and `generate_image(prompt, model="nano_banana_2_lite", ...)` wait for the run and return the file URL; `submit`, `status` and `credits` are there for finer control. All of them read `EMAKI_API_KEY` ([create a key](https://emaki.ai/settings/apikeys)).

| Language | Install | Source |
|---|---|---|
| Python | `pip install emaki` | [hanshs474/emaki-py](https://github.com/hanshs474/emaki-py) |
| JavaScript / TypeScript | `npm install emaki-ai` | [hanshs474/emaki-ts](https://github.com/hanshs474/emaki-ts) |
| Go | `go get github.com/hanshs474/emaki-go` | [hanshs474/emaki-go](https://github.com/hanshs474/emaki-go) |
| Rust | `cargo add emaki` | [hanshs474/emaki-rs](https://github.com/hanshs474/emaki-rs) |
| Java / Kotlin | `io.github.hanshs474:emaki` | [hanshs474/emaki-java](https://github.com/hanshs474/emaki-java) |

From an agent instead of code: the [MCP server](../integrations/mcp.md). Writing your own client: the [HTTP API](../http.md) is two calls.

Default video model: [Seedance 2.5](https://emaki.ai/seedance-2-5). For [image to video](https://emaki.ai/image-to-video), pass a first-frame URL as `image`.
