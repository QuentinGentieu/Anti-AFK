import win32api, win32con #Importation du module win32api et win32con
import random #Importation du module random 
import time #Importation du module time

c = int(input("Tous les combiens de temps voulez vous un Refresh (en seconde) ?\n")) #Assigne à la variable "c" un input de type int 

e = int(input("Pendant combien de temps vous voulez l'antiAFK (en minute) ?\n")) #Assigne à la variable "e" un input de type int 

def clic(x, y): #Creation d'une fonction "clic" qui prend en parametre 2 variables : x et y 

    i = 0.0 # Assigne à la variable i un nombre floattant de 0.0 pour prendre en compte les nombres apres la virgule d'une division euclidienne

    for i in range(y // x): #Creation d'une boucle qui prend les 2 variables mis en parametre qu'on divise avec une division euclidienne, calcule permettant de calculer le nombre de fois restant a faire l'operation de clic suivant
        a = random.randint(825,1050) #Assigne à la variable "a" un nombre au hasard entre 825 et 1050 à partir du module random 
        b = random.randint(325,550) #Assigne à la variable "b" un nombre au hasard entre 325 et 550 à partir du module random

        win32api.SetCursorPos((a,b)) # Place le curseur de la souris au position x et y qui sont reprensenté par les variables "a" pour la longueur et "b" pour la largeur de l'ecran, et le curseur est placé grace à une methode du module win32api
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,a,b,0,0) #Creation d'un evenement avec la souris grace au module win32api, puis appuye le clic droit sur les coordonnes créer a partir de la varible "a" et "b" grace à une methode du module win32con
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,a,b,0,0) #Creation d'un evenement avec la souris grace au module win32api, puis relache le clic droit sur les coordonnes créer a partir de la varible "a" et "b" grace à une methode du module win32con
        time.sleep(x) #Laisse un temps de repos entre chaque clic pour relancer la boucle et refaire un nouveau clic 

e *= 60  # Assigne à la variable "e" une multiplication permettant la conversion en minute

clic(c, e) #Appelle de la fonction prennant en parametre 2 variables, la premiere qui est le temps de rafraichissement, et le deuxieme qui est la duree de l'antiAFK

input("appuyer pour fermer") #Input permettant de laisser la console ouvert et pouvoir la fermer à tout moment pour arreter l'antiAFK à n'importe qu'elle moment




# ©TDLegends