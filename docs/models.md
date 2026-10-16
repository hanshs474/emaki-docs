# Models and parameters

Pass the id as `model` and the options inside `parameters`. Anything you leave out takes the default shown here. Prices are in credits on your emaki account, the same as on the website ([pricing](https://emaki.ai/pricing)).

## Video

| `model` | What it is | Parameters (default) |
|---|---|---|
| `seedance_2_5` | [Seedance 2.5](https://emaki.ai/seedance-2-5), the default | `duration` 4–30 (5) · `resolution` `480p` / `720p` / `1080p` (`480p`) · `aspect_ratio` `16:9` / `4:3` / `1:1` / `3:4` / `9:16` / `21:9` / `adaptive` (`16:9`) · `generate_audio` (true) · `image` first frame URL · `last_frame_image` |
| `seedance_2` | [Seedance 2.0](https://emaki.ai/seedance-2) | `duration` 4–15 · `resolution` `480p` / `720p` / `1080p` · `aspect_ratio` · `generate_audio` · `image` |
| `seedance_2_fast` | Seedance 2.0 Fast | `duration` 4–15 · `resolution` `480p` / `720p` · `aspect_ratio` · `generate_audio` · `image` |
| `seedance_2_mini` | Seedance 2.0 Mini, the lowest-cost video model | same as Fast |
| `minimax_h3` | MiniMax H3 | `duration` 5–15 · `aspect_ratio` · `image` |
| `veo_3_1` | Veo 3.1 | `resolution` `720p` / `1080p` / `4k` · `aspectRatio` `16:9` / `9:16` (camelCase) · `image` |

Pass `image` (a public https URL) to turn a still into a clip: that is [image to video](https://emaki.ai/image-to-video).

## Image

| `model` | What it is | Parameters |
|---|---|---|
| `nano_banana_2_lite` | Nano Banana 2 Lite, the lowest-cost model | `aspect_ratio` `1:1` / `4:3` / `3:4` / `16:9` / `9:16` / `2:3` / `3:2` / `21:9` / `5:4` / `4:5` |
| `nano_banana_2` | Nano Banana 2 | `aspect_ratio` · `resolution` `1K` / `2K` / `4K` |
| `seedream_5_lite` | Seedream 5 Lite | `aspect_ratio` · `quality` `basic` / `high` / `ultra` |
| `gpt_image_2` | GPT Image 2 | `aspect_ratio` · `resolution` `1K` / `2K` / `4K` |

The finished image URL comes back in `videoUrl` from the status call, the same field as video.
