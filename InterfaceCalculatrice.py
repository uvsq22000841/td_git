import tkinter as tk


racine = tk.Tk()
racine.title("racine")

b = 0
z = 0

nombre = ""
sNombre = ""
#
#

ve = 0
o = 0
ye = 0

#
#

sauvegarde = ""
enregistrer = ""


canvas1 = tk.Canvas(racine, width=470, height=540)
canvas1.grid()

buttonv = tk.Button(canvas1, text="bienvenue sur la calculatrice")
buttonv.grid(column=4, row=4, columnspan=2, rowspan=4, padx=10, pady=10)


def Afficher(jo):
    buttonv.config(text=jo)


def reinitialize():
    global b, ve, z, nombre, o, sNombre
    b = 0
    z = 0
    ve = 0
    nombre = ""
    sNombre = ""


    o = 0


def nombreE(a):
    global b, ye, z, nombre, sNombre
    b = b + 1

    if b == 11:
        Afficher("plus de 10 chiffres")
    else:
        if z == 0:
            nombre = nombre + a
            Afficher(nombre)
        else:
            sNombre = sNombre + a
            Afficher(nombre + ye + sNombre)


def operation(c):
    global b, ve, ye, o, nombre, sauvegarde, A, sNombre, z
    b = 0
    z = 1
    if ve == 1:
        Afficher("erreur 2 opérations à la suite 3 operations")
        reinitialize()

    else:
        ve = 1
        ye = c

        if len(nombre) == 0:
            if o == 0:
                Afficher("veuillez entrer un chiffre")
            else:
                nombre = str(enregistrer)
                A = enregistrer
                sauvegarde = str(A) + c
                Afficher(sauvegarde)

        else:
            A = int(nombre)

            sauvegarde = str(A) + c
            Afficher(sauvegarde)


def calculer():
    global sNombre, A, B, ye, o, enregistrer

    print("quelquechose")

    if len(sNombre) == 0:
        Afficher("erreur veuillez entrez un nombre")
        reinitialize()
    else:
        B = int(sNombre)
        o = 1
        print("octoschoseS")
        if ye == " / ":
            if B == 0:
                Afficher("division par zero impossible, infinity")
            else:
                enregistrer = A / B
        elif ye == " + ":
            enregistrer = A + B
        elif ye == " - ":
            enregistrer = A - B
        elif ye == " * ":
            enregistrer = A * B

        Afficher(enregistrer)
        reinitialize()

        o = 1




button0 = tk.Button(canvas1, text="0", command=lambda: nombreE("0"))
button0.grid(column=0, row=5)

button1 = tk.Button(canvas1, text="1", command=lambda: nombreE("1"))
button1.grid(column=0, row=2)

button2 = tk.Button(canvas1, text="2", command=lambda: nombreE("2"))
button2.grid(column=1, row=2)

button3 = tk.Button(canvas1, text="3", command=lambda: nombreE("3"))
button3.grid(column=2, row=2)

button4 = tk.Button(canvas1, text="4", command=lambda: nombreE("4"))
button4.grid(column=0, row=3)

button5 = tk.Button(canvas1, text="5", command=lambda: nombreE("5"))
button5.grid(column=1, row=3)

button6 = tk.Button(canvas1, text="6", command=lambda: nombreE("6"))
button6.grid(column=2, row=3)

button7 = tk.Button(canvas1, text="7", command=lambda: nombreE("7"))
button7.grid(column=0, row=4)

button8 = tk.Button(canvas1,  text="8", command=lambda: nombreE("8"))
button8.grid(column=1, row=4)

button9 = tk.Button(canvas1, text="9", command=lambda: nombreE("9"))
button9.grid(column=2, row=4)


plus = tk.Button(canvas1, text="+", command=lambda: operation(" + "))
plus.grid(column=3, row=2)

moins = tk.Button(canvas1, text="-", command=lambda: operation(" - "))
moins.grid(column=3, row=3)

fois = tk.Button(canvas1, text="*", command=lambda: operation(" * "))
fois.grid(column=3, row=4)

divi = tk.Button(canvas1, text="/", command=lambda: operation(" / "))
divi.grid(column=3, row=5)


calcule = tk.Button(canvas1, text="=", command=lambda: calculer() )
calcule.grid(column=1, row=5, columnspan=2)

racine.mainloop()
