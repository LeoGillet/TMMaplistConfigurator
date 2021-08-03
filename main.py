#This is main.py
from functions import *
from tkinter import *

def start():
    def clear_fields():
        ent_mlname.delete(0, END)
        ent_dirpath.delete(0, END)

    window = Tk()
    window.title("Trackmania Maplist Configurator")
    frame = Frame(window, width=450, height=100)
    frame.grid(row=10, column=2)

    lbl_mlname = Label(text="Maplist file name :").grid(row=1, column=1)
    ent_mlname = Entry(width=20)
    ent_mlname.grid(row=1, column=2)

    ent_dirpath = Entry(width=60)
    ent_dirpath.insert(0, "C:/path/to/my/maps/")
    ent_dirpath.grid(row=2, column=2)
    lbl_dirpath = Label(text="Absolute path of the directory containing .Gbx map files :").grid(row=2, column=1)

    lbl_mapCount = Label(text="Waiting").grid(row=5, column=2)

    btn_clear = Button(text="Clear", command=clear_fields).grid(row=10, column=1)
    btn_generate = Button(text="Generate...", command=generate_file).grid(row=10, column=2)


    window.bind("<Key>", key_pressed)
    window.mainloop()

if __name__ == '__main__':
    print('Deploying Window...')
    start()