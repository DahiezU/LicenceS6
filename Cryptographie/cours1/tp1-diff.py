from PIL import Image, ImageFont, ImageDraw

img1 = Image.open("C:\\Users\\dahie\\Documents\\SDN-S6\\Cryptographie\\cours1\\exo_2a.png")
img2 = Image.open("C:\\Users\\dahie\\Documents\\SDN-S6\\Cryptographie\\cours1\\\exo_2b.png")

imgmess = Image.new("1",(img1.width,img1.height))

for i in range(img1.width):
    for j in range (img1.height):
        if(img1.getpixel((i, j)) == img2.getpixel((i, j))):
            imgmess.putpixel((i, j), 1)

imgmess.show()
imgmess.save("exo_diff.png")

