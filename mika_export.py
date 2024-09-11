#importation des bibliothèques
from PIL import Image,ImageFont,ImageDraw

#la foncion imprimTxt prend une liste de chaines de caractères en entrée et inscrit ses chaines de caractères dans un fichier txt
def imprimTxt(liste):
    fichier=open("file.txt","w")
    for i in range(len(liste)):
        fichier.write("\n"+liste[i])
    fichier.close()

#la fonction export2Png écrit une liste de chaines de caractères dans un fichier .png
def export2Png(liste,num="",nom="mika_export"):
    font = ImageFont.truetype("FUTRFW.TTF", 20)
    img = Image.new("RGB", (len(liste[0])*20,len(liste)*20), color = "white")
    draw = ImageDraw.Draw(img)
    for i in range(len(liste)):
        draw.text((0, i*20),liste[i],(0,0,0),font=font)
    img.save(nom+str(num)+".png")

#la fonction export2Avi met toutes les images d'une liste dans un fichier .avi.
def export2Avi(images,fpsvid=10):
    import cv2
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape
    size = (width, height)
    out = cv2.VideoWriter("mika_export.avi", cv2.VideoWriter_fourcc(*'DIVX'), fpsvid, size)
    for image in images:
        img = cv2.imread(image)
        out.write(img)
    out.release()