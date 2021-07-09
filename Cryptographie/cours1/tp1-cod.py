from PIL import Image , ImageFont, ImageDraw

mon_modele = Image.open("C:\\Users\\dahie\\Documents\\SDN-S6\\Cryptographie\\cours1\\exo_3a.png")

mon_modele1 = Image.open("C:\\Users\\dahie\\Documents\\SDN-S6\\Cryptographie\\cours1\\exo_3b.png")

'''mon_image = Image.new("0", (600,400))
draw = ImageDraw.Draw(mon_image)
'''
mon_image = Image.new("1", (mon_modele.width,mon_modele.height))

font = ImageFont.truetype("C:\\Windows\\Fonts\\Tahoma.ttf", 30)


draw = ImageDraw.Draw(mon_image)

a = []
b = []
for x in range(mon_modele.width ) :
    for y in range(mon_modele.height ):
        if( mon_modele.getpixel((x,y)) == mon_modele1.getpixel((x,y))):
            mon_image.putpixel((x,y),1)


mon_image.show()

for x in range(mon_image.width):
    if((mon_image.getpixel((x,0))) == 1 ):
        if(len(a) < 8):
            a.append(0)
        else:
            b.append(a)
            a = []
            a.append(0)
    else:
        if(len(a) < 8):
            a.append(1)
        else:
            b.append(a)
            a = []
            a.append(1)

#print(b)

ints = [1,2,3]
string_ints = [str(int) for int in ints]


str_of_ints = ",".join(string_ints)





c = []
for elem in b:
    elem.reverse()
    string_ints = [str(int) for int in elem]
    str_of_ints = "".join(string_ints)
    #print(str_of_ints)
    c.append(int(str_of_ints,2))



print(c)

r = ''.join(map(chr,c))
print(r)

#mon_image.save("test.png")



"""
A => HAUT;
B => BAS;
C => GAUCHE;
D => DROITE.
 """