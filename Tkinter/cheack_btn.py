import tkinter as tk

root = tk.Tk()
root.title("Tourism Options")
root.geometry("300x250")


beach = tk.IntVar()
mountain = tk.IntVar()
natural_trails = tk.IntVar()

def update_options():
    selected = []

    if beach.get() == 1:
        selected.append("Beach")

    if mountain.get() == 1:
        selected.append("Mountain")

    if natural_trails.get() == 1:
        selected.append("Natural Trails")

    lbl_destino.config(text=", ".join(selected))

main_frame = tk.Frame(root)
main_frame.pack(pady=10)

tk.Label(main_frame, text="Elige tu destino:", font=("Arial", 12, "bold")).pack()


tk.Checkbutton(main_frame, text="Beach", variable=beach, command=update_options).pack(anchor="w")
tk.Checkbutton(main_frame, text="Mountain", variable=mountain, command=update_options).pack(anchor="w")
tk.Checkbutton(main_frame, text="Natural Trails", variable=natural_trails, command=update_options).pack(anchor="w")


lbl_destino = tk.Label(main_frame, text="", fg="blue")
lbl_destino.pack(pady=20)

root.mainloop()
