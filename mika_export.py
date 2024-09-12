#importation des bibliothèques
from PIL import Image,ImageFont,ImageDraw

def imprimTxt(liste):
    """
    La fonction imprimTxt (jamais utilisée dans ce programme) sert à écrire une liste de chaines de caractères dans un fichier .txt.
    Exemple : imprimTxt(["abc","bla"])
    Ce fichier texte passeras à la ligne entre chaque case de la liste.
    Résultat de l'exemple (dans le fichier file.txt) :
    ------
    abc
    bla
    ------
    """
    fichier=open("file.txt","w")
    for i in range(len(liste)):
        fichier.write("\n"+liste[i])
    fichier.close()

def export2Png(liste,num="",nom="mika_export"):
    """
    Pour utiliser la fonction export2Png(), il faut mettre de 1 à 3 arguments :
    liste : doit être une liste de chaines de caractères.
    num : doit être, dans l'idéal, un chiffre ou un nombre (et prend par défaut la valeur "").
    nom : doit être également une chaine de caractères (et prend par défaut la valeur "mika_export").
    Exemple : export2Png(["abc","bla"],6,"monmika")
    La fonction imprimeras donc dans une image nommée "monmika6.png" (nom+str(num)+".png") les caractères compris dans l'argument liste.
    """
    font = ImageFont.truetype("FUTRFW.TTF", 20)
    img = Image.new("RGB", (len(liste[0])*20,len(liste)*20), color = "white")
    draw = ImageDraw.Draw(img)
    for i in range(len(liste)):
        draw.text((0, i*20),liste[i],(0,0,0),font=font)
    img.save(nom+str(num)+".png")

def export2Avi(images,fpsvid=10):
    """
    Pour utiliser export2Avi() il faut mettre en argument une liste de chemins d'accès vers des fichiers images (.png) et, si on le souhaite, une valeur pour fpsvid.
    Exemple : export2Avi(["1.png","2.png"],24)
    Les images seront alors assemblés en une vidéo avec un fps de 10 (ou dans ce cas, de 24).
    """
    import cv2
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape
    size = (width, height)
    out = cv2.VideoWriter("mika_export.avi", cv2.VideoWriter_fourcc(*'DIVX'), fpsvid, size)
    for image in images:
        img = cv2.imread(image)
        out.write(img)
    out.release()
