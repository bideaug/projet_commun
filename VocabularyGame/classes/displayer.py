import tkinter

class Displayer:
    def __init__(self):
        self.app = tkinter.Tk()
        self.app.geometry("640x480")
        self.app.title("Vocabulary Game!")
        self.createMenu()
        self.app.mainloop()


    def hello(self):
        print("coucou")

    def show_about(self):
        self.about_window = tkinter.Toplevel(self.app)
        self.about_window.title("A propos")
        self.lb = tkinter.gabel(self.about_window, text="Bonjour !")
        self.lb.pack()

    def createMenu(self):
        self.mainmenu = tkinter.Menu(self.app)

        self.first_menu = tkinter.Menu(self.mainmenu, tearoff=0)
        self.first_menu.add_command(label="Level 1")
        self.first_menu.add_command(label="Level 2")
        self.first_menu.add_command(label="Level 3")
        self.first_menu.add_command(label="Level 4")
        self.first_menu.add_command(label="Quitter", command=self.app.quit)

        # self.second_menu = tkinter.Menu(self.mainmenu, tearoff=0)
        # self.second_menu.add_command(label="Command1")
        # self.second_menu.add_command(label="A propos", command=self.show_about)

        self.mainmenu.add_cascade(label="Levels ", menu=self.first_menu)
        # self.mainmenu.add_cascade(label="Second", menu=self.second_menu)

        self.app.config(menu=self.mainmenu)
