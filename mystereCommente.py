from PIL import Image                        # Importation de la librairie PILLOW (gestion image)
img = Image.open("pomme.jpg")                # Mise en mémoire dans la variable "img" du fichier 
#--------------------------------------------# pomme.jpg qui doit être dans le même répertoire que
#--------------------------------------------# le programme
largeur_image,hauteur_image=img.size         # Python autorise les affectations multiples.
#--------------------------------------------# img.size est un attribut (une variable intrinsèque
#--------------------------------------------# à la variable img) avec les dimensions de l'image
#--------------------------------------------# sous forme de tupple (= liste non modifiable). 

for y in range(hauteur_image):               # Boucle pour parcourir les toutes les lignes
    for x in range(largeur_image):           # Boucle imbriquée pour parcourir les pixels de la
#--------------------------------------------# ligne en cours
        rouge,vert,bleu=img.getpixel((x,y))  # Méthode getpixels() appliquée à la variable img qui
#--------------------------------------------# renvoie les valeurs R,V,B du pixel à la position x,y
        nouveau_rouge=vert                   # Le vert prend l'intensité du rouge
        nouveau_vert=bleu                    # Le bleu prend l'intensité du vert
        nouveau_bleu=rouge                   # Le rouge prend l'intensité du bleu
        img.putpixel((x,y),(nouveau_rouge,nouveau_vert,nouveau_bleu)) # Méthode putpixel()
#--------------------------------------------# qui remplace les valeurs R, V, B du pixel en x,y 

img.show()                                   # Affichage de l'image
img.save("pommeMystere.jpg")                 # Sauvegarde de l'image obtenue
print(img.size)                              # Affichage du tupple avec la taille de l'image
