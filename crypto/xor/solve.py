from PIL import Image, ImageFont, ImageDraw, ImageChops

with Image.open("c1.png") as c1:
    with Image.open("c2.png") as c2:
        flag = ImageChops.logical_xor(c1.convert("1"), c2.convert("1"))
        flag.save("flag.png")

