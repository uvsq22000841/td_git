


#les boutons 0,1,2,3,4,5,6,7,8,9 appel la fonction nombreE avec en paramètre leurs nombre sous forme string "0", "1", "2", "3"...

#le bouton plus appel la fonction plus
#le bouton moins appel la fonction moins
#le bouton fois appel la fonction fois
#le bouton diviser appeller la fonction diviser

#le bouton calculer appel la fonction calculer

## et pour finir:
#la variable variableAfficher doit être remplacer par un config d'un label 

b = 0
z = 0

nombre = ""
sNombre = ""
#
#

ve = 0

def reset():
    global b, ve, z, nombre
    b = 0
    z = 0
    ve = 0
    o = 0
    nombre = ""


def nombreE(a):
    global b
    b = b + 1

    if b == 11:
        variableAfficher = "plus de 10 chiffres"
    else:
        if z == 0
            nombre = nombre + a
        else:
            sNombre = sNombre + a


def plus():
    global b, ve
    b = 0
    if ve == 1:
        variableAfficher = "erreur 2 opérations à la suite 3 operations"
        reset():

    else:
        ve = 1
        y = "plus"

        if len(nombre) == 0:
            if o == 0:
                variableAfficher = "veuillez entrer un chiffre"
            else:
                nombre = enregistrer
                variableAfficher = str(A) + " + "

        else:
            A = int(nombre)

            variableAfficher = 
        
            

a) plus 
	b=0 #pour que le nombre de chiffre compté reviennent a 0 et soit dorénavcant compter pour le second Nombre
	si ve == 1
		variableaAfficher= "erreur 2 opérations à la suite ou 3 operations"
	sinon
		ve=  1
		y= "plus"

		si lengh(nombre) =0 #condition qui verifie si la premiere variable est vide
			si O=0 #on n'a jamais enregistrer de réponse
				variableAfficher= "veuillez entrer un chiffre"
			sinon
				nombre= enregistrer #et qui prend la réponse précedente
				variableaAfficher= str(A) + " + "

 		sinon
			for i in range lenght(nombre)
				A= int(nombre[i])

			variableaAfficher= str(A) + " + "



b)  	
	b= 0	
	si ve == 1
	
		variableaAfficher= "erreur 2 opérations à la suite ou 3 operations"
	sinon
		ve=  1
		y= "moins"

		si lengh(nombre) =0 #condition qui verifie si la premiere variable est vide
			si O=0 #on n'a jamais enregistrer de réponse
				variableAfficher= "veuillez entrer un chiffre"
			sinon
				nombre= enregistrer #et qui prend la réponse précedente
				sauvegarde = str(A) + " - " 
				variableaAfficher= sauvegarde

 		sinon
			for i in range lenght(nombre)
				A= int(nombre[i])
			sauvegarde = str(A) + " - " 
			variableaAfficher= sauvegarde


c) 	
	b= 0
	si ve == 1
		variableaAfficher= "erreur 2 opérations à la suite ou 3 operations"
	sinon
		ve=  1
		y= "fois"

		si lengh(nombre) =0 #condition qui verifie si la premiere variable est vide
			si O=0 #on n'a jamais enregistrer de réponse
				variableAfficher= "veuillez entrer un chiffre"
			sinon
				nombre= enregistrer #et qui prend la réponse précedente
				sauvegarde = str(A) + " * "
				variableaAfficher= sauvegarde

 		sinon
			for i in range lenght(nombre)
				A= int(nombre[i])
			sauvegarde = str(A) + " * "
			variableaAfficher= sauvegarde

d) 	
	b= 0
	si ve == 1
		variableaAfficher= "erreur 2 opérations à la suite ou 3 operations"
	sinon
		ve=  1
		y= "divide"

		si lengh(nombre) =0 #condition qui verifie si la premiere variable est vide
			si O=0 #on n'a jamais enregistrer de réponse
				variableAfficher= "veuillez entrer un chiffre"
			sinon
				nombre= enregistrer #et qui prend la réponse précedente
				sauvegarde = str(A) + " / " 
#toujours plus de mémoire plutôt que de réaficher le resultat final avec (dans f(calcul) variableAfficher = str(A) + " / " + str(B) + " = " +str(enregistrer)    "
				variableaAfficher= sauvegarde

 		sinon
			for i in range lenght(nombre)
				A= int(nombre[i])

			variableaAfficher= str(A) + " / "





				
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

