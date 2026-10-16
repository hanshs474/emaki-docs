# ComfyUI

[ComfyUI-emaki](https://github.com/hanshs474/ComfyUI-emaki) adds three nodes under the **emaki** category. No local GPU and no model downloads.

| Node | Inputs | Outputs |
|---|---|---|
| emaki Text to Video (Seedance 2.5) | prompt, model, duration, resolution, aspect ratio, audio | saved MP4 path, url |
| emaki Image to Video (Seedance 2.5) | IMAGE (first frame), prompt, model, duration, resolution, aspect ratio, audio | saved MP4 path, url |
| emaki Generate Image | prompt, model, aspect ratio | IMAGE, url |

Install with ComfyUI Manager (search **ComfyUI-emaki**) or `git clone https://github.com/hanshs474/ComfyUI-emaki` into `custom_nodes`. Paste a key from [emaki.ai/settings/apikeys](https://emaki.ai/settings/apikeys) into the node, or set `EMAKI_API_KEY` before starting ComfyUI.

Image to Video uploads the frame and passes its URL to [Seedance 2.5 image to video](https://emaki.ai/image-to-video). The MP4 lands in ComfyUI's output folder.
