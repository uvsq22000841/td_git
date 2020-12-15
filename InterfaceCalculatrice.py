import tkinter as tk


racine = tk.Tk()
racine.title("racine")





canvas = tk.Canvas(racine, width= "470", height="540")


label1 = tk.Label(canvas, width="380", height="120", text="bienvenue sur la calculatrice")
label1.grid(column=0, row=0, columnspan=2, rowspan=4, padx=10, pady=10)


button0 = tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE("0"))
button0.grid(column=0, row=5, padx=10, pady=10)

button1 = tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE("1"))
button1.grid(column=0, row=2, padx=10, pady=10)

button2 = tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE("2"))
button2.grid(column=1, row=2, padx=10, pady=10)

button3 = tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE("3"))
button3.grid(column=2, row=2, padx=10, pady=10)

button4 = tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE("4"))
button4.grid(column=0, row=3, padx=10, pady=10)

button5 = tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE("5"))
button5.grid(column=1, row=3, padx=10, pady=10)

button6 = tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE("6"))
button6.grid(column=2, row=3, padx=10, pady=10)

button7 = tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE("7"))
button7.grid(column=0, row=4, padx=10, pady=10)

button8 = tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE("8"))
button8.grid(column=1, row=4, padx=10, pady=10)

button9 = tk.Button(canvas, width="80", height="60", text="0", command= lambda:nombreE("9"))
button9.grid(column=2, row=4, padx=10, pady=10)


plus = tk.Button(canvas, width="80", height="60", text="+", command= lambda: operation(" + "))
plus.grid(column=3, row=2, padx=10, pady=10)

moins = tk.Button(canvas, width="80", height="60", text="-", command= lambda: operation(" - "))
moins.grid(column=3, row=3, padx=10, pady=10)

fois = tk.Button(canvas, width="80", height="60", text="*", command= lambda: operation(" * "))
fois.grid(column=3, row=4, padx=10, pady=10)

divi = tk.Button(canvas, width="80", height="60", text="/", command= lambda: operation(" / "))
divi.grid(column=3, row= 5, padx=10, pady=10)


buttonCalcule= tk.Button(canvas, width="80", height="60", command= calculer())
buttonCalcule.grid(column=1,row=5, columnspan=2, padx=10, pady=10)

racine.mainloop()