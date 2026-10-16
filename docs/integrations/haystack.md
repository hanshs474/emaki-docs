# Haystack

[`emaki-haystack`](https://pypi.org/project/emaki-haystack/) adds two Haystack components: `EmakiVideoGenerator` ([Seedance 2.5](https://emaki.ai/seedance-2-5) by default) and `EmakiImageGenerator`.

```bash
pip install emaki-haystack
export EMAKI_API_KEY=sk-...   # https://emaki.ai/settings/apikeys
```

```python
from emaki_haystack import EmakiVideoGenerator

EmakiVideoGenerator(duration=5, aspect_ratio="9:16").run(prompt="a lighthouse beam sweeping across fog at night")
# {"videos": ["https://cdn.emaki.ai/..."]}
```

| Component | `run()` input | Output |
|---|---|---|
| `EmakiVideoGenerator` | `prompt`, optional `image_url` (first frame, [image to video](https://emaki.ai/image-to-video)) | `{"videos": [url]}` |
| `EmakiImageGenerator` | `prompt` | `{"images": [url]}` |

Init parameters: `model`, `duration`, `resolution`, `aspect_ratio`, `generate_audio` (video) and `model`, `aspect_ratio` (image). The key is a Haystack `Secret` read from `EMAKI_API_KEY`; both components serialize with `to_dict` / `from_dict`. Errors raise the `emaki` client's exceptions.

Source: [hanshs474/emaki-haystack](https://github.com/hanshs474/emaki-haystack).
