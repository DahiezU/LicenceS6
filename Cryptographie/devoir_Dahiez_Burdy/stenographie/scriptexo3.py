from PIL import Image, ImageFont, ImageDraw
import numpy as np
imag = "C:\\Users\\dahie\\Documents\\SDN-S6\\Cryptographie\\devoir_Dahiez_Burdy\\stenographie\\exo_2b.png"

# Burdy Simon & Dahiez Ulysse.

#////////// W A R N I N G ///////////
#n'oubliez pas de changer les paths des images dans le programmes. car nous n'avons pas réussi avec les paths plus court. 
#   Merci.


# 1. Implantez cette transformation en Python.

def reduire(image):
    img = Image.open(image)
    size = img.size

    res = Image.new(img.mode,(2*int(np.ceil(size[0]/2)),2*int(np.ceil(size[1]/2))))
    for i in range(size[0]):
        for j in range(size[1]):
            if (i+j)%4 == 0:
                color = img.getpixel((i,j))
                res.putpixel((i//2,j//2),color)
                res.putpixel((i//2 + int(np.ceil(size[0]/2)),j//2),color)
                res.putpixel((i//2,j//2 + int(np.ceil(size[1]/2))),color)
                res.putpixel((i//2 + int(np.ceil(size[0]/2)),j//2 + int(np.ceil(size[1]/2))),color)
    res.save("C:\\Users\\dahie\\Documents\\SDN-S6\\Cryptographie\\devoir_Dahiez_Burdy\\stenographie\\reduction.png")    
    
    return res
    

# 2. Que peut-on dire de cette transformation ?

# Nous pouvons en déduire que la fonction est bijective 


# 3. Question mystère ! vous devez implanter en python une fonction en relation avec la propriété précédente 
def reduireboucle (image, repetition):
    
    img = Image.open(image)
    size = img.size
    res = Image.new(img.mode,(2*int(np.ceil(size[0]/2)),2*int(np.ceil(size[1]/2))))
    reduire(image)
    for i in range (0, repetition-1):
        res = reduire("C:\\Users\\dahie\\Documents\\SDN-S6\\Cryptographie\\devoir_Dahiez_Burdy\\stenographie\\reduction.png")
    
    res.show()

#reduireboucle(imag, 8)
#reduireboucle(imag, 24)

# 4. En quoi le développement de question précédente prouve la propriété énoncé en 2.

# Nous pouvons constater que la photo tend vers un même resultat, quelques soit le nombre de répétition. comme une fonction bijective.

# 5. Que se passe-t-il si on répète le procédé ?

# Si nous répétons le procédé, nous revenons à une photo déjà vu.

#6. Prouvez le !

# nous nouvons voir que les deux photos sont identique alors qu'elles n'ont pas le même nombre de répetition. nous avons prouvé ca par la fonction isSame qui revoit un photo uniquement blanche. 
#25 & 5
reduireboucle(imag, 5)
reduireboucle(imag, 25)

chat5 = Image.open("C:\\Users\\dahie\\Documents\\SDN-S6\\Cryptographie\devoir_Dahiez_Burdy\\stenographie\\chat5.png")
chat25 = Image.open("C:\\Users\\dahie\\Documents\\SDN-S6\\Cryptographie\\devoir_Dahiez_Burdy\\stenographie\\chat25.png")

imgmess = Image.new("1",(chat5.width,chat5.height))
def isSame():

    for i in range(chat5.width):
        for j in range (chat25.height):
            if(chat5.getpixel((i, j)) == chat25.getpixel((i, j))):
                imgmess.putpixel((i, j), 1)
    imgmess.show()
isSame()