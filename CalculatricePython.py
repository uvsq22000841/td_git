


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


def afficher(jo):
    #config d'un label pour afficher tout
    print(jo)


def reinitialize():
    global b, ve, z, nombre
    b = 0
    z = 0
    ve = 0
    o = 0
    nombre = ""


def nombreE(a):
    global b, ye, z
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
    global b, ve, y, o, nombre, sauvegarde, A
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
    global sNombre, A, B ye, o, enregistrer

    if len(sNombre) == 0
            afficher("erreur veuillez entrez un nombre")
            reinitialize():
    else:
        B = int(sNombre)
        o = 1

        if ye == " / ":  
            if B == 0:
                afficher("division par zero impossible, infinity")
            else:
                enregistrer = A / B
        else if ye == " + ":
            enregistrer = A + B
        else if ye == " - ":
            enregistrer = A - B
        else if ye == " * ":
            enregistrer = A * B

        afficher(enregistrer)



   

 
 
