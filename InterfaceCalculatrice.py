import tkinter as tk

racine = tk.Tk()
racine.title("racine")

racine.geometry(800*800+50+50)




canvas1 = tk.Canvas(racine, width= "470px", height="540px")
canvas1.grid()

label1 = tk.Label(canvas, width="380px", height="120px", text="bienvenue sur la calculatrice")
label1.grid()

button = []

a = 2
b = 0  

for i in range(0, 11, 1):
    if(b == 2):
        b = -1
        a = a + 1
    b = b + 1

    button.append(tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE(str(i)))
    button[i].grid(column=a, row=b)

buttonOperation = ['' ,'' ,'' ,'' ]

buttonOperation[0] = tk.Button(canvas, width="80", height="60", text="+", command= lambda: operation(" + "))
buttonOperation[1] = tk.Button(canvas, width="80", height="60", text="-", command= lambda: operation(" - "))
buttonOperation[2] = tk.Button(canvas, width="80", height="60", text="*", command= lambda: operation(" * "))
ButtonOperation[3] = tk.Button(canvas, width="80", height="60", text="/", command= lambda: operation(" / "))

for i in range(2, 5, 1):
    buttonOperation[i].grid(column=0, row=i)

buttonCalcule= tk.Button(canvas, width="80", height="60", command= calculer())
buttonCalcule.grid(column=3,row=5)

racine.mainloop()