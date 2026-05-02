from tkinter import *

root = Tk()
root.title("Formulario")

mi_frame = Frame(root, width=500, height=400)
mi_frame.pack()

# variable para btn
get_name = StringVar()
gender_choice = StringVar(value="Option 1")

# labels de campos informativos
name = Label(mi_frame, text="Name:")
name.grid(row=0, column=0, sticky="e", padx=5)

lastName = Label(mi_frame, text="Last Name:")
lastName.grid(row=1, column=0, sticky="e", padx=5)

password = Label(mi_frame, text="Password:")
password.grid(row=2, column=0, sticky="e", padx=5)

address = Label(mi_frame, text="Address:")
address.grid(row=3, column=0, sticky="e", padx=5)

gender = Label(mi_frame, text="Gender:")
gender.grid(row=4, column=0, sticky="e", padx=5)

notes = Label(mi_frame, text="Notes:")
notes.grid(row=6, column=0, sticky="e", padx=10)

# cuadros de texto
name_texto = Entry(mi_frame, textvariable=get_name)
name_texto.grid(row=0, column=1)

lastName_texto = Entry(mi_frame)
lastName_texto.grid(row=1, column=1)

password_texto = Entry(mi_frame)
password_texto.grid(row=2, column=1)
password_texto.config(show="*")

address_texto = Entry(mi_frame)
address_texto.grid(row=3, column=1)

# radio bottoms tkinter
gender_male = Radiobutton(
    mi_frame, text="Male", variable=gender_choice, value="Option 1"
)
gender_male.grid(row=4, column=1, sticky="w")

gender_female = Radiobutton(
    mi_frame, text="Female", variable=gender_choice, value="Option 2"
)
gender_female.grid(row=5, column=1, sticky="w")

notes_texto = Text(mi_frame, width=20, height=5)
notes_texto.grid(row=6, column=1)

# scrollbar en notes
notes_scroll = Scrollbar(mi_frame, command=notes_texto.yview)
notes_scroll.grid(row=6, column=2, sticky="nsew")
notes_texto.config(yscrollcommand=notes_scroll.set)


# botones con tkinter
def nameBtn():
    get_name.set("Marlon")


btn_send = Button(root, text="Send", command=nameBtn)
btn_send.pack()

root.mainloop()
