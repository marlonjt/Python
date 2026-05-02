from tkinter import *
from tkinter import messagebox

root = Tk()


def modal_information():
    messagebox.showinfo("Information", "Tkinter information modal and tools.")


def information_licencia():
    messagebox.showwarning("Warning", "Licencia error")


def exit_application():
    value = messagebox.askquestion("exit", "sure exit application?")
    if value == "yes":
        root.destroy()


def out_file():
    valor = messagebox.askretrycancel("Reintentar", "Not valid action")
    if valor == False:
        root.destroy


navbar = Menu(root)
root.config(menu=navbar, width=500, height=300)


file_menu = Menu(navbar, tearoff=0)
file_menu.add_command(label="Nuevo")
file_menu.add_command(label="Guardar", command=out_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=exit_application)


tools = Menu(navbar, tearoff=0)
tools.add_command(label="Terminal")
tools.add_command(label="Run")

preferences = Menu(navbar, tearoff=0)
preferences.add_command(label="Licencia", command=modal_information)
preferences.add_command(label="Vencimiento", command=information_licencia)

navbar.add_cascade(label="file", menu=file_menu)
navbar.add_cascade(label="tools", menu=tools)
navbar.add_cascade(label="preferences", menu=preferences)

root.mainloop()
