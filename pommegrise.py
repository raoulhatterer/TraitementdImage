from PIL import Image
img = Image.open("pomme.jpg")
largeur_image=480
hauteur_image=300
for y in range(hauteur_image):
    for x in range(largeur_image):
        r,v,b=img.getpixel((x,y))
        n_r=(v+b+r)//3
        n_v=(v+b+r)//3
        n_b=(v+b+r)//3
        img.putpixel((x,y),(n_r,n_v,n_b))
img.show()
img.save("pommegrise.jpg")
