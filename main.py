#importation des fonctions externes
from mika_create import *
from mika_export import *

#importation des biliothèques
from time import time, sleep

def mika_image():
    fichierImage=input("Quelle image voulez-vous traiter ? ")
    temps=time()
    export2Png(listeDeCaract(tableau2Ascii(numpy2Tableau(image2Numpy(reduireTaille(recupererImage(fichierImage),250000))))))
    print("Votre image a bien été exportée en "+str(int(time()-temps))+" secondes par le Programme Mika. Toute l'équipe des Roues Détachables vous remercie.")

def mika_video():
    fichierVideo=input("Quelle video voulez-vous traiter ? ")
    temps=time()
    nb,duree=video2Images(fichierVideo)
    print(duree)
    liste_chemins=[]
    for i in range(nb):
        export2Png(listeDeCaract(tableau2Ascii(numpy2Tableau(image2Numpy(reduireTaille(recupererImage("./data/frame"+str(i)+".jpg")))))),i,"./data/frame_export")
        print("L'image "+str(i)+" a ete exportee")
        liste_chemins.append("./data/frame_export"+str(i)+".png")
    print("Toutes les images ont bien ete exportees, creation de la video en cours...")
    export2Avi(liste_chemins,nb/duree)
    print("Vidéo intermédiaire créée, création de la vidéo finale...")
    combinerVidEtAudio(fichierVideo)
    print("Votre video finale a bien ete exportee en "+str(int(time()-temps))+" secondes par le programme Mika. Toute l'equipe des roues detachables vous remercie")

def mika_webcam(cap):
    afficherTerminal(listeDeCaract(tableau2Ascii(numpy2Tableau(image2Numpy(reduireTaille(capturerWebcam(cap),15000))),[" ",".",":",";","*","=","(","{","$","&","@","#"]),-1,-1))



if int(input("Pour quel type de fichier voulez-vous utiliser ce programme ? (1=Video ; 0=Photo)")):
    if int(input("Voulez-vous convertir une vidéo 0=déjà enregistrée ou 1=en directe via votre webcam ?")):
        import cv2
        cap = cv2.VideoCapture(0)
        while True:
            mika_webcam(cap)
            sleep(0.1)
    else:
        mika_video()
else:
    mika_image()
