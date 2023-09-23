from PIL import Image, ImageFont, ImageDraw, ImageChops
from pathlib import Path
import numpy

flag = Path("flag.txt").read_text().strip()

font = ImageFont.truetype("COMIC.TTF", 60)
_, _, w, h = font.getbbox(flag)
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)

img = Image.new("RGBA", (w, h), white)
d = ImageDraw.Draw(img)
d.text((0, 0), flag, font=font, fill=black)

m1 = img.copy()
d = ImageDraw.Draw(m1)
d.rectangle([(0, 0), (w // 2, h)], fill=white)

m2 = img.copy()
d = ImageDraw.Draw(m2)
d.rectangle([(w // 2, 0), (w, h)], fill=white)

rng = numpy.random.rand(h, w, 3) * 255
key = Image.fromarray(rng.astype("uint8")).convert("1")

c1 = ImageChops.logical_xor(m1.convert("1"), key)
c2 = ImageChops.logical_xor(m2.convert("1"), key)

c1.save("c1.png")
c2.save("c2.png")
