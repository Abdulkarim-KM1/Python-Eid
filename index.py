import arabic_reshaper #pip install arabic-reshaper 
from bidi.algorithm import get_display  # pip install python-bidi
from PIL import Image, ImageFont, ImageDraw # pip install pillow

text= 'عبدالكريم'
reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)
im = Image.open("IE.png")
font = ImageFont.truetype("Sahel.ttf", size=190)
(x,y)=im.size
print(x,y)
d = ImageDraw.Draw(im)
d.multiline_text((1900,2800), bidi_text, font=font, fill='white', spacing=15, align="center")
im.save(text+".png")