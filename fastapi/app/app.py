import io
from fastapi import FastAPI, Response # pip install fastapi
import arabic_reshaper #pip install arabic-reshaper 
from bidi.algorithm import get_display  # pip install python-bidi
from PIL import Image, ImageFont, ImageDraw # pip install pillow

app = FastAPI()

@app.post("/", tags=["images"])
async def get_images(info: dict):
    print(info)
    text = info["Name"]

    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    path, color = get_image_path(info["Club"])
    size, height = get_font_size(info["Club"], 10)
    font = ImageFont.truetype("fastapi//resources//sahel.ttf", size=size)
    im = Image.open(path)
    d = ImageDraw.Draw(im)
    (w, h) = d.textsize(bidi_text, font=font)
    print(w)

    size, height = get_font_size(info["Club"], w)
    font = ImageFont.truetype("fastapi//resources//sahel.ttf", size=size)
    (w, h) = d.textsize(bidi_text, font=font)
    (W, H) = im.size
    print(W, H)
   
   

    d.text(((W-w)/2, height), bidi_text, font=font, fill=color, align="center")
    img_byte_arr = io.BytesIO()
    im.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return Response(img_byte_arr, media_type="image/png")



def get_image_path(text):
    if text == "IE-club":
        path = "fastapi//resources//IE-club.png"
        color = 'white'
    elif text == "SANI":
        path = "fastapi//resources//SANI.png"
        color = 'white'
    elif text == "Law":
        path = "fastapi//resources//Law.png"
        color = '#3E8B91'
    return path, color

def get_font_size(text, width):
    if text == "IE-club":
        if width <= 2000:
            size = 190
            height = 2750
        elif width >= 2000 and width < 3000:
            size = 150
            height = 2775
        elif width >= 3000:
            size = 100
            height = 2825
    elif text == "SANI":
        if width <= 1000:
            size = 175
            height = 2100
        elif width <= 1500:
            size = 125
            height = 2125
        elif width <= 2000:
            size = 100
            height = 2140
        elif width >= 2000 and width < 2500:
            size = 75
            height = 2170
        elif width >= 2500:
            size = 50
            height = 2200
    elif text == "Law":
        if width <= 300:
            size = 50
            height = 1135
        elif width <= 450:
            size = 35
            height = 1145
        elif width <= 600:
            size = 25
            height = 1155
        elif width <= 750:
            size = 20
            height = 1170
        elif width > 750:
            size = 15
            height = 1170
    return size, height
    