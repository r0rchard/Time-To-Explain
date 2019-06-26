from tkinter import *


def save_car(answers_car, x):
    if x in answers_car:
        answers_car.remove(x)
    else:
        answers_car.append(x)


def save_data(value_state, value_vr, gau, car):
    if value_state == 1:
        state = "motion"
    else:
        state = "motionless"

    if value_vr == 1:
        used_to_vr = "yes"
    else:
        used_to_vr = "no"

    d = [used_to_vr, state, int(gau), car]
    return d


def display():
    answers_car = []
    data = []
    window = Tk()

    label_vr = Label(window, text="Habitué(e) à la VR :")
    value_vr = IntVar()
    button_vr_oui = Radiobutton(window, text="Oui", variable=value_vr, value=1)
    button_vr_non = Radiobutton(window, text="Non", variable=value_vr, value=2)

    label_state = Label(window, text="Etat :")
    value_state = IntVar()
    button_state_motion = Radiobutton(window, text="Mobile", variable=value_state, value=1)
    button_state_motionless = Radiobutton(window, text="Immobile", variable=value_state, value=2)

    label_gau = Label(window, text="Nombre de réponses au GAU :")
    value_gau = StringVar()
    value_gau.set("")
    input_gau = Entry(window, textvariable=value_gau, width=3)

    label_car = Label(window, text="Bonnes réponses au CAR :")

    list_q = [k for k in range(1, 18)]
    c = 2
    for i in range(17):
        c += 1
        item = list_q[i]
        button = Checkbutton(window, indicatoron=0, text=item,
                             command=lambda x=item: save_car(answers_car, x))
        button.grid(row=3, column=c)
    button_save = Button(window, text="Sauvegarder",
                         command=window.quit)

    label_vr.grid(row=1, column=0, sticky=E)
    button_vr_oui.grid(row=1, column=1)
    button_vr_non.grid(row=1, column=2)

    label_state.grid(row=2, column=0, sticky=E)
    button_state_motion.grid(row=2, column=1)
    button_state_motionless.grid(row=2, column=2)

    label_gau.grid(row=3, column=0, sticky=E)
    input_gau.grid(row=3, column=1, sticky=W)

    label_car.grid(row=3, column=2, sticky=E)

    button_save.grid(row=4, column=2)
    window.mainloop()
    return [value_vr.get(), value_state.get(), value_gau.get(), answers_car]


if __name__ == '__main__':
    display()
