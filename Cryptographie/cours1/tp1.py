from PIL import Image, ImageFont, ImageDraw


mon_image_txt = Image.new("1",(600,400))

font = ImageFont.truetype("C:\\Windows\\Fonts\\Tahoma.ttf", 30)

draw = ImageDraw.Draw(mon_image_txt)

draw.text((10, 10),"Bienvenue dans le TP 1 de Cryptographie", font = font, align ="left" , fill= "white")
draw.text((10, 60), "Détour par la stéganographie", font = font, align ="left" , fill= "white")

mon_image_txt.show()
