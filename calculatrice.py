import tkinter as tk


racine = tk.Tk()




canvas1 = tk.Canvas(racine, width= 500, height=500, bg="black")
canvas1.grid()

label1= tk.Label(racine, text="Bienvenue sur la calculatrice")
label1.grid()


carac = ""

a = 0

def afficher(c):
    label1.config(text=c)

def effacer():
    global carac
    if len(carac) != 0:
        carac = carac[0:-2]

    afficher(carac)

def caractere(c):
    global carac, a, reponse, resultat

    if a == 0:
        a = 1
        if c not in ['+','-','*','/']:
            carac = carac + c
            afficher(carac)
        else:
            carac = str(resultat) + c
            afficher('rep' + c)
    else:
        carac = carac + c
        afficher(carac)

def reset():
    global carac, a
    carac= ''
    a= 0
    reponse = 0

def calcule():
    global carac, a, resultat, reponse


    j= carac.count('+') + carac.count('-') + carac.count('*') + carac.count('/') 


    if j > 1 or j == 0 or carac[0] in ['+', '-', '*', '+'] or carac[-1] in ['+', '-', '*', '+']:
        afficher('error')
        reset()

    else:




        for i in range(len(carac)):
            if carac[i] in ['+', '-', '*', '/']:
                A = carac[0:i]
                B = carac[i+1: -1] + carac[-1]
                Z= carac[i]
                break

        
        O= list(A)
        V= list(B)

        for i in range(len(O)):
            if '_' == O[i]:
                O[i] = '-'



        for i in range(len(V)):
            if '_' in V:
                V[i] = '-'
        

        
        print(A)
        print(B)
                

                



        try:


            A= float(A)
            B= float(B)

            if(Z == '+'):
                resultat = A + B
                afficher(resultat)
                reset()
                reponse = 1
            elif(Z == '-'):
                resultat = A - B
                afficher(resultat)
                reset()
                reponse = 1

            elif(Z == '*'):
                resultat = A * B
                afficher(resultat)
                reset()
                reponse = 1
            else:
                if B == 0:
                    afficher('error')
                    reset()
                else:
                    resultat = A / B
                    afficher(resultat)
                    reset()
                    reponse = 1


        except:
            afficher('error')
            reset()



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

button8= tk.Button(canvas1, text="8", command= lambda:caractere("8"))
button8.grid()

button9= tk.Button(canvas1, text="9", command= lambda:caractere("9"))
button9.grid()

button0= tk.Button(canvas1, text="0", command= lambda:caractere("0"))
button0.grid()

buttonVirgule = tk.Button(canvas1, text=".", command= lambda:caractere("."))
buttonVirgule.grid()

buttonplus = tk.Button(canvas1, text="+", command= lambda:caractere("+"))
buttonplus.grid()

buttonmoins = tk.Button(canvas1, text="-", command= lambda: caractere("-"))
buttonmoins.grid()

buttondepmoins = tk.Button(canvas1, text="_", command= lambda: caractere("_"))
buttondepmoins.grid()

buttonfois = tk.Button(canvas1, text="*", command= lambda:caractere("*"))
buttonfois.grid()

buttondiv = tk.Button(canvas1, text="/", command= lambda:caractere("/"))
buttondiv.grid()

labeltext= tk.Label(canvas1, text="bienvenue sur la calculatrice")
labeltext.grid()

buttoncalcule = tk.Button(canvas1, text="=", command= lambda:calcule())
buttoncalcule.grid()


less = tk.Button(canvas1, text="effacer", command= lambda:effacer())
less.grid()

racine.mainloop()