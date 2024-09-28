#importation des bibliothèques
from PIL import Image
from numpy import asarray

def video2Images(lienVid):
    """
    Pour utiliser cette fonction, il faut mettre en argument un lien vers une vidéo locale sous le format String.
    Exemple : video2Images("mika.mp4")
    La vidéo sera alors décomposée en images (environ 10 par secondes)...
    Par ailleurs, cette fonction retourne deux variables : le nombre d'images et la durée de la vidéo.
    Voici donc comment l'utiliser : nImages,duree = video2Images("mika.mp4")
    """
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

def recupererImage(lien):
    """
    Pour utiliser cette fonction, il faut mettre en argument un lien vers une image locale sous le format String.
    Exemple : recupererImage("mika.jpg")
    L'image sera alors convertie en nuance de gris et retournée.
    Voici donc comment l'utiliser : imageWB = recupererImage("mika.jpg")
    """
    return Image.open(lien).convert("L")

def capturerWebcam(cap):
    import cv2
    ret, frame = cap.read()
    #cap.release()
    #cv2.destroyAllWindows()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image)
    return pil_image.convert("L")

def reduireTaille(image,taille=10000):
    """
    Pour utiliser cette fonction, il faut mettre en argument une image déjà importée dans Python ainsi que, si on le souhaite, un entier (int).
    Exemple : reduireTaille(image,5000)
    L'image sera alors rétrécie pour qu'elle prenne environ 10,000.00 pixels (ou autre selon le deuxième argument).
    Par ailleurs, la fonction reverra l'image rétrécie...
    Voici donc comment l'utiliser : imageReduite = reduireTaille(image, 12000)
    """
    x=image.size[0]
    y=image.size[1]
    taille=x*y/taille
    x=x/(taille**0.5)
    y=y/(taille**0.5)
    return image.resize((int(x), int(y)))

def image2Numpy(image):
    """
    La fonction image2Numpy prend en entrée une image et la retourne convertie en tableau Numpy.
    Exemple : tableau = image2Numpy(image)
    """
    return asarray(image)

def numpy2Tableau(tableau,nb=12):
    """
    La fonction numpy2Tableau convertit et retourne un tableau Numpy en une liste de liste en remplacant chaque élément du tableau par le calcul x=x/256*12 (le nombre 12 peut être remplacé dans l'appel de la fonction.
    Exemple d'utilisation : liDeLi = numpy2Tableau(tabNumpy,12)
    Son objectif est principalement de pouvoir l'utiliser plus tard pour faire de l'ASCII art.
    """
    tab = []
    for i in range(len(tableau)):
        liste = []
        for j in tableau[i]:
            liste.append(int(j/256*nb))
        tab.append(liste)
    return tab

def tableau2Ascii(tableau,liste=0):
    """
    Pour utiliser cette fonction, il faut mettre en argument une liste de listes d'entiers.
    Exemple : tableau2Ascii([[...],[...],...])
    Pour chaque case de la liste de listes, le programme prendra le caractère qui a pour indice la valeur de la case.
    Exemple d'utilisation :
    La commande print(tableau2Ascii([[2,4],[4,2]])) renverra [["&","{"],["{","&"]].
    """
    if type(liste) != list:
        liste=["#","@","&","$","{","(","=","*",";",":","."," "]
    
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            tableau[i][j]=liste[tableau[i][j]]
    return tableau

def listeDeCaract(tableau,coef=1,depart=0):
    """
    Pour utiliser cette fonction, il faut mettre en argument une liste de listes.
    Exemple : listeDeCaract([[...],[...],...])
    Dans chaque sous-liste, le programme regroupe chaque élément comme une chaine de caractères.
    Exemple d'utilistion :
    La commande print(listeDeCaract([["&","{"],["{","&"]])) renverra ["&{","{&"]
    """
    liste=[]
    for i in range(len(tableau)):
        caracInter=""
        for j in range(depart,len(tableau[i])*coef-depart,coef):
            caracInter=caracInter+tableau[i][j]
        liste.append(caracInter)
    return liste
