from tkinter import *
from tkinter import filedialog

root = Tk()


def abrir_archivo():

    fichero = filedialog.askopenfilename(
        title="abrir",
        initialdir="/home/marlon/Descargas",
        filetypes=(("ficheros word", "*.docx"), ("ficheros txt", "*.txt"), ("Todos los ficheros", "*.*")),
    )

    print(fichero)


Button(root, text="Abrir", command=abrir_archivo).pack()


root.mainloop()
