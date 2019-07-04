from tkinter import *


class MainView:

    def __init__(self):
        self.answers_car = []
        self.results_participant = []
        self.window = Tk()

        label_vr = Label(self.window, text="Habitué(e) à la VR :")
        value_vr = IntVar()
        button_vr_oui = Radiobutton(self.window, text="Oui", variable=value_vr, value=1)
        button_vr_non = Radiobutton(self.window, text="Non", variable=value_vr, value=2)

        label_state = Label(self.window, text="Etat :")
        value_state = IntVar()
        button_state_motion = Radiobutton(self.window, text="Mobile", variable=value_state, value=1)
        button_state_motionless = Radiobutton(self.window, text="Immobile", variable=value_state, value=2)

        label_gau = Label(self.window, text="Nombre de réponses au GAU :")
        value_gau = StringVar()
        value_gau.set("")
        input_gau = Entry(self.window, textvariable=value_gau, width=3)

        label_car = Label(self.window, text="Bonnes réponses au CAR :")

        list_q = [k for k in range(1, 18)]
        c = 2
        for i in range(17):
            c += 1
            item = list_q[i]
            button = Checkbutton(self.window, indicatoron=0, text=item,
                                 command=lambda x=item: self.save_car(x))
            button.grid(row=3, column=c)
        button_save = Button(self.window, text="Sauvegarder",
                             command=lambda: self.save_data(value_state.get(), value_vr.get(),
                                                            value_gau.get(),
                                                            self.answers_car))
        button_quit = Button(self.window, text="Quitter",
                             command=self.window.quit)

        label_vr.grid(row=1, column=0, sticky=E)
        button_vr_oui.grid(row=1, column=1)
        button_vr_non.grid(row=1, column=2)

        label_state.grid(row=2, column=0, sticky=E)
        button_state_motion.grid(row=2, column=1)
        button_state_motionless.grid(row=2, column=2)

        label_gau.grid(row=3, column=0, sticky=E)
        input_gau.grid(row=3, column=1, sticky=W)

        label_car.grid(row=3, column=2, sticky=E)

        button_save.grid(row=4, column=1)
        button_quit.grid(row=4, column=2)

    def run(self):
        self.window.title("Time to Explain")
        self.window.mainloop()

    def save_car(self, x):
        if x in self.answers_car:
            self.answers_car.remove(x)
        else:
            self.answers_car.append(x)

    def save_data(self, value_state, value_vr, gau, car):
        if value_state == 1:
            state = "motion"
        else:
            state = "motionless"

        if value_vr == 1:
            used_to_vr = "yes"
        else:
            used_to_vr = "no"
        if gau == "":
            gau = -1
        self.results_participant = [state, used_to_vr, int(gau), car]
        self.window.destroy()


if __name__ == '__main__':
    w = MainView()
    w.run()
