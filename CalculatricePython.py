


#les boutons 0,1,2,3,4,5,6,7,8,9 appel la fonction nombreE avec en paramètre leurs nombre sous forme string "0", "1", "2", "3"...

#les boutons plus, moins, fois, diviser appel la fonction operation avec en paramètre leurs opération respective avec la forme exacte:
# " + ", " - ", " * ", " / "

#le bouton calculer appel la fonction calculer


b = 0
z = 0

nombre = ""
sNombre = ""
#
#

ve = 0


def afficher():
    #config d'un label pour afficher tout

def reinitialize():
    global b, ve, z, nombre
    b = 0
    z = 0
    ve = 0
    o = 0
    nombre = ""


def nombreE(a):
    global b, ye
    b = b + 1

    if b == 11:
        Afficher("plus de 10 chiffres")
    else:
        if z == 0
            nombre = nombre + a
            Afficher(nombre)
        else:
            sNombre = sNombre + a
            Afficher(nombre + ye + sNombre)

        


def operation(c):
    global b, ve
    b = 0
    if ve == 1:
        Afficher("erreur 2 opérations à la suite 3 operations")
        reinitialize():

    else:
        ve = 1
        y = c

        if len(nombre) == 0:
            if o == 0:
                Afficher("veuillez entrer un chiffre")
            else:
                nombre = enregistrer
                sauvegarde = str(A) + c
                Afficher(sauvegarde)

        else:
            A = int(nombre)

            sauvegarde = str(A) + c
            Afficher(sauvegarde)
        

def calculer():
    global sNombre, A, ye, o

    if len(sNombre) == 0
            afficher("erreur veuillez entrez un nombre")
            reinitialize():
    else:
        B = int(sNombre)

        if ye == " / ":  
            if B == 0:
                afficher("division par zero impossible, infinity")
            else:
                o = 1
            enregistrer = A / B
        else:


    afficher(enregistrer)


   

    if ye == " + "
        rengistrer 
    elif ye == " - ":
    elif ye == " * ":
    else:


Calculer:
	#dans l'ordre des operation les plus courantes pour gagner en performance
	si ye== plus
	sinon si ye == moins
	sinon si ye == fois
	sinon
		si lenght(sNombre)==0
			variableAfficher ="vous n'avez pas entrer de second nombre"
			#afficher que le resultat précedent n'existe pas
			O= 0
		sinon
			for j in range lenght(sNombre)
				B= int(nombre[j])
			if B==0
				variableAfficher ="division par zero impossible, infinity"
			sinon
				o= 1
				enregistrer= A / B
				variableAfficher = sauvegarde + str(B) + " = " +str(enregistrer)   


			

P
a chaque fois qu'on a une erreur 
reinitilisaliser toutes les variables
I
intilisaliser toutes les variable necessaire
C
mettre en global les variables utilisées
D
verifier que pour la première execution qu'on déjà enregistrer une première réponse [enregistrer] car sinon on afficher une erreur

