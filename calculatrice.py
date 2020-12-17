import tkinter as tk


racine = tk.Tk()




canvas1 = tk.Canvas(racine, width= 500, height=500, bg="black")
canvas1.grid()

label1= tk.Label(racine, text="Bienvenue sur la calculatrice")
Label1.grid()


carac = ""

a = 0

def afficher(c):
    label1.config(text=c)

def effacer():
    global carac
    if len(carac) != 0:
        carac.pop(-1)

def caractere(c):
    global carac, a

    if a == 0:
        a = 1
        if c not in ['+','-','*','/']:
            carac = carac + c
    else:
        carac = carac + c
        afficher(carac)


def calcule():
    global carac, a, resultat
    a= carac.count('+') + carac.count('-') + carac.count('*') + carac.count('/') 



    if carac.count>1 or carac.count == 0 or carac[0] in ['+', '-', '*', '+'] or carac[-1] in ['+', '-', '*', '+']:
        afficher('error')

    else:
        for i in range(len(carac)):
            if carac[i] in ['+', '-', '*', '/']:
                A = carac[0:i]
                B = carac[i+1: -1]
                Z= carac[i]
                break

        try:
            A= float(A)
            B= float(A)
            if(Z == '+'):
                resultat = A + B
                afficher(resultat)
            elif(Z == '-'):
                resultat = A - B
                afficher(resultat)
            elif(Z == '*'):
                resultat = A * B
                afficher(resultat)
            else:
                if B == 0:
                    afficher('error')
                else:
                    resultat = A / B
                    afficher(resultat)


        except:
            afficher('error')



          
            


        a cette premiere occurence placer, la partie gauche dans partieGaucge
        et la partie droite dans partieDroit

        si la partie gauche n'est pas un int ou float ou si la partie droit n'est pas une int ou float
            afficher(error)
            a=1
        sinon
            si la premier occurence trouvée a été un fois, moins ou plus:
                enregistrer= A + B
            sinon 
                enregistrer= A* B
            sinon enregistrer = A-B
            sinon
                si B =0
                    afficher(error infini)
                    a=1
                sinon enregistrer= A/B
        





button1 = tk.Button(canvas1, text="1", command= lambda: caractere("1"))
button1.grid()

button2 = tk.Button(canvas1, text="2", command= lambda: caractere("2"))
button2.grid()

button3 = tk.Button(canvas1, text="3", command= lambda:caractere("3"))
button3.grid()

button4 = tk.Button(canvas1, text="4", command= lambda:caractere("4"))
button4.grid()

button5 = tk.Button(canvas1, text="5", command= lambda:caractere("5"))
button5.grid()

button6= tk.Button(canvas1, text="6", command= lambda:caractere("6"))
button6.grid()

button7= tk.Button(canvas1, text="7", command= lambda:caractere("7"))
button7= tk.Button(canvas1, text="7", command= lambda:caractere("7"))

button8= tk.Button(canvas1, text="8", command= lambda:caractere(8))
button8.grid()

button9= tk.Button(canvas1, text="9", command= lambda:caractere("9"))
button9.grid()


buttonVirgule = tk.Button(canvas1, text=".", command= lambda:caractere("."))
buttonVirgule.grid()

buttonplus = tk.Button(canvas1, text="+", command= lambda:caractere("+"))
buttonplus.grid()

buttonmoins = tk.Button(canvas1, text="-", command= lambda: caractere("-"))
buttonmoins.grid()

buttonfois = tk.Button(canvas1, text="*", command= lambda:caractere("*"))
buttonfois.grid()

buttondiv = tk.Button(canvas1, text="/", command= lambda:caractere("/"))
buttondiv.grid()

labeltext= tk.Label(canvas1, text="bienvenue sur la calculatrice")
labeltext.grid()

calcule = tk.Button(canvas1, text="=", command= lambda:calcule())
calcule.grid()


less = tk.Button(canvas1, text="effacer", command= lambda:effacer())
less.grid()

racine.mainloop()