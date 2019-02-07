from PIL import Image
img = Image.open("pomme.jpg")
largeur_image,hauteur_image=img.size

for y in range(hauteur_image):
    tailleDiag=y*largeur_image//hauteur_image
    for x in range(tailleDiag):
       rouge,vert,bleu=img.getpixel((x,y))
       nouveau_rouge=(vert+bleu+rouge)//3
       nouveau_vert=(vert+bleu+rouge)//3
       nouveau_bleu=(vert+bleu+rouge)//3
       img.putpixel((x,y),(nouveau_rouge,nouveau_vert,nouveau_bleu))

img.show()
img.save("pommemisgrise.jpg")
