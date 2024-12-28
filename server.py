"""Judge images as hotdog or not hotdog. """
from typing import Tuple
from fastapi import FastAPI
import numpy as np
from PIL import Image
from pydantic import BaseModel
# from . import serverutils


app = FastAPI()


class RawImage(BaseModel):
    """Expected image format to receive from client devices. """
    mode: str              # ex: RGB
    size: Tuple[int, int]  # width x height
    data: str


@app.post('/score/')
async def score_image(raw: RawImage) -> bool:
    """Score a user image.

    Args:
        raw (RawImage): hex-encoded flattened image

    Returns:
        bool: hotdog or not hotdog
    """

    # preprocess image for inference engine
    data = bytes.fromhex(raw.data)  # undo client conversion to hex/str
    img = Image.frombytes(raw.mode, raw.size, data)
    img = np.array(img)
    img = np.transpose(img, [2, 0, 1])
    img = img.astype(np.float32) / 255

    # inference
    # score = serverutils.score_image(img)

    return True
