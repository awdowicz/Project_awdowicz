from io import BytesIO
from PIL import Image
import PIL.ImageOps
from fastapi import File, FastAPI
from pierwsza import czy_pierwsza
from starlette.responses import StreamingResponse
import io

app = FastAPI()

@app.get("/pierwsza/{liczba}")
async def pierwsza(liczba: int):
    return czy_pierwsza(liczba)

@app.post("/zdjecie/invert")
async def invert(file: bytes = File()):
    image = Image.open(io.BytesIO(file))
    inverted_image = PIL.ImageOps.invert(image)
    responseImage = io.BytesIO()
    inverted_image.save(responseImage, "JPEG")
    responseImage.seek(0)
    return StreamingResponse(responseImage, media_type="image/jpeg")