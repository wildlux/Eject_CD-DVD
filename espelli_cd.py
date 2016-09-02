#!/usr/bin/python
from Tkinter import *
import os

def term():
	os.system("&& echo exit status $ && exit 1")
	os.system("drutil tray ejec")
	os.system("drutil eject")
	os.system("drutil eject 0")
	os.system("drutil eject 1")
	os.system("drutil eject 2")
	os.system("drutil eject 3")
	os.system("drutil eject 4")
	
testo="Benvenuto! Questo e il programma scritto ed ideato da : Paolo Lo Bello, Grazie per averlo utilizzato!"
f=Tk()
f.title("Eject Cdrom!")
f.geometry("%dx%d%+d%+d" % (340,200,599, 417))
Label(f,text="Eject CD/DVD", justify = LEFT).pack()
Pulsante=Button(f,text="Forza CD/DVD",command=term).pack()
os.system("say "+testo)
Label(f,text = "Prova a premere il tasto espulsione nella tastiera").pack()
Label(f,text = "se non il tasto premi questo pulsante", justify = LEFT).pack()
Label(f,text = "per forzare l'uscita del CD/DVD dal vano disco.", justify = LEFT).pack()
Label(f,text = "Premi il tasto eject.", justify = LEFT).pack()
f.mainloop()
#f.destroy()