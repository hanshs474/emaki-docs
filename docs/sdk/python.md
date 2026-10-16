# Python

```bash
pip install emaki
```

Standard library only. Each call waits for the run and returns the URL of the finished file.

```python
from emaki import generate_video, generate_image, credits

print(credits())  # remaining credits, free to call

clip = generate_video("a fox trotting through fresh snow at dawn, tracking shot",
                      duration=8, resolution="720p", aspect_ratio="9:16")

# image to video: the image becomes the first frame
clip = generate_video("the camera slowly orbits the statue", image="https://example.com/statue.jpg")

pic = generate_image("isometric diorama of a ramen shop at night", aspect_ratio="1:1")
```

The default video model is [Seedance 2.5](https://emaki.ai/seedance-2-5) (`seedance_2_5`); other ids are on the [models](../models.md) page. Extra keyword arguments go into `parameters` as they are. Set `EMAKI_API_KEY` or pass `api_key=`. Source: [hanshs474/emaki-py](https://github.com/hanshs474/emaki-py).
