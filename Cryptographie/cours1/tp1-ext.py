from PIL import Image, ImageFont, ImageDraw

img = Image.open("C:\\Users\\dahie\\Documents\\SDN-S6\\Cryptographie\\cours1\\exo_4.png")


img.show()

li = []
for x in (0, img.height):
    for y in (0, img.width):
        li.imgmess.putpixel((x, y), 1)

print(li)