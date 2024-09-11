#importation des bibliothèques
from PIL import Image
from numpy import asarray

#la fonction video2Images décompose une vidéo en 10 images par secondes
def video2Images(lienVid):
    import cv2
    vidcap = cv2.VideoCapture(lienVid)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps / 10)
    success, image = vidcap.read()
    count = 0
    frame_count = 0
    while success:
        if frame_count % frame_interval == 0:
            cv2.imwrite("./data/frame%d.jpg" % count, image)
            count = count+1
        success, image = vidcap.read()
        frame_count=frame_count+1
    TMP=vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    vidcap.release()
    return count,round(round(TMP)/round(fps))

#la fonction recupererImage prend en entrée la source de l'image, l'importe dans python et la convertit en noir et blanc
def recupererImage(lien):
    return Image.open(lien).convert("L")

#la fonction reduireTaulle reduit la qualité d'une image
def reduireTaille(image,taille=10000):
    x=image.size[0]
    y=image.size[1]
    taille=x*y/taille
    x=x/(taille**0.5)
    y=y/(taille**0.5)
    return image.resize((int(x), int(y)))

#la fonction image2Numpy convertit l'image en noir et blanc dans un tableau Numpy
def image2Numpy(image):
    return asarray(image)

#la fonction numpy2Tableau convertit entre autre un tableau Numpy en une liste de listes
def numpy2Tableau(tableau):
    tab = []
    for i in range(len(tableau)):
        liste = []
        for j in tableau[i]:
            liste.append(int(j/256*12))
        tab.append(liste)
    return tab

#la fonction tableau2Ascii prend une liste de listes en entrée et remplace chaque nombre par le cararctère approprié
def tableau2Ascii(tableau):
    liste=["#","@","&","$","{","(","=","*",";",":","."," "]
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            tableau[i][j]=liste[tableau[i][j]]
    return tableau

#la fonction listeDeCaract convertit une liste de listes en une liste de chaines de caractères
def listeDeCaract(tableau):
    liste=[]
    for i in range(len(tableau)):
        caracInter=""
        for j in tableau[i]:
            caracInter=caracInter+j
        liste.append(caracInter)
    return liste