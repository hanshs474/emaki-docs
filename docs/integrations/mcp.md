# MCP server (Claude, Cursor, Gemini CLI)

[`emaki-mcp`](https://github.com/hanshs474/emaki-mcp) is a stdio MCP server that gives any MCP client four tools: `generate_video`, `generate_image`, `check_status` and `credits`. Ask for a [Seedance 2.5](https://emaki.ai/seedance-2-5) clip in chat and get the file URL back.

```json
{
  "mcpServers": {
    "emaki": {
      "command": "npx",
      "args": ["-y", "emaki-mcp"],
      "env": { "EMAKI_API_KEY": "sk-..." }
    }
  }
}
```

- Claude Code: `claude mcp add emaki -e EMAKI_API_KEY=sk-... -- npx -y emaki-mcp`
- Gemini CLI: `gemini extensions install https://github.com/hanshs474/emaki-mcp`
- Claude Code plugin: `claude plugin marketplace add hanshs474/emaki-mcp`, then `claude plugin install emaki@emaki`

| Tool | What it does |
|---|---|
| `generate_video` | Text to video, or [image to video](https://emaki.ai/image-to-video) with `image_url`. Default model `seedance_2_5`. Returns a run id unless `wait: true` |
| `generate_image` | Text to image (default `nano_banana_2_lite`); returns the URL |
| `check_status` | Status of a run and its URL when ready |
| `credits` | Credits left on the account, free |

Video takes minutes, so `generate_video` returns a run id by default and the model calls `check_status` later.
