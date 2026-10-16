# LangChain

[`langchain-emaki`](https://pypi.org/project/langchain-emaki/) gives a LangChain agent two tools: `emaki_video_generator` ([Seedance 2.5](https://emaki.ai/seedance-2-5) text to video and [image to video](https://emaki.ai/image-to-video)) and `emaki_image_generator`. Both return the file URL.

```bash
pip install langchain-emaki
export EMAKI_API_KEY=sk-...   # https://emaki.ai/settings/apikeys
```

```python
from langchain_emaki import EmakiImageGenerator, EmakiVideoGenerator

video = EmakiVideoGenerator()   # model="seedance_2_5"
image = EmakiImageGenerator()   # model="nano_banana_2_lite"

video.invoke({"prompt": "a paper boat drifting down a rain gutter, low angle", "duration": 5})
```

```python
from langchain.agents import create_agent

agent = create_agent("openai:gpt-5", tools=[image, video])
agent.invoke({"messages": [("user", "Make a still of a lighthouse in fog, then a 5-second clip that starts from it")]})
```

| Tool | Input | Returns |
|---|---|---|
| `emaki_video_generator` | `prompt`, optional `image_url` (first frame), `duration`, `resolution`, `aspect_ratio` | clip URL |
| `emaki_image_generator` | `prompt`, optional `aspect_ratio` | image URL |

Set `model=` on either tool for another id from [Models and parameters](../models.md). Refusals (missing key, empty balance, a model that needs a purchase, a run already generating, a filtered prompt) come back to the agent as text, so it can react instead of crashing. Each run costs credits on your emaki account, the same price as on the website.

Source: [hanshs474/langchain-emaki](https://github.com/hanshs474/langchain-emaki).
