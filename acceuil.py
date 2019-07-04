from tkinter import *


class Acceuil:
    def __init__(self):
        self.window = Tk()

        button_add = Button(self.window, text="Add",
                            command=lambda: self.action_add() )
        button_show = Button(self.window, text="Show",
                             command=lambda: self.action_show())
        button_quit = Button(self.window, text="Quit",
                             command=self.window.quit)

        button_add.pack()
        button_show.pack()
        button_quit.pack()

    def run(self):
        self.window.title("Time to Explain")
        self.window.mainloop()

    def action_add(self):
        self.window.quit()
        return "add"

    def action_show(self):
        self.window.quit()
        return "show"


if __name__ == '__main__':
    w = Acceuil()
    w.run()
