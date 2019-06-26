import matplotlib.pyplot as plt
from questions import q
from interface import MainView
import csv


def results_to_csv(data):
    end = [["number", "state", "usedtoVR", "Gau"] + ["Car" + str(i + 1) for i in range(17)]]
    end.extend([[r[0], r[1], r[2], r[3]] for r in data])
    for i in range(1, len(end)):
        car = [0] * 17
        for value in data[i - 1][4]:
            car[value - 1] = 1
        end[i].extend(car)
    return end


def write_csv(file, data):
    data = results_to_csv(data)
    with open(file, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerows(data)


def read_csv(file):
    data = []
    with open(file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    data = csv_to_results(data)
    return data


def csv_to_results(data):
    data2 = [[int(r[0]), r[1], r[2], int(r[3]), [i + 1 for i, x in enumerate(r[4:21]) if x == '1']] for r in data[1:]]
    return data2


def create_boxplot():
    fig1 = plt.figure()
    fig1.suptitle('Motion VS Motionless')
    fig1.canvas.set_window_title('LAMPA Experiment')

    ax1 = fig1.add_subplot(221)
    ax1.set_title('CRA_motion')
    ax1.set_ylim(0, 17)
    ax1.boxplot(CRA_motion)

    ax2 = fig1.add_subplot(222)
    ax2.set_title('CRA_motionless')
    ax2.set_ylim(0, 17)
    ax2.boxplot(CRA_motionless)

    ax3 = fig1.add_subplot(223)
    ax3.set_title('GAU_motion')
    ax3.set_ylim(0, 30)
    ax3.boxplot(GAU_motion)

    ax4 = fig1.add_subplot(224)
    ax4.set_title('GAU_motionless')
    ax4.set_ylim(0, 30)
    ax4.boxplot(GAU_motionless)

    for k in range(4):
        plt.gcf().get_axes()[k].xaxis.set_ticklabels([""])
    for r in results:
        print(r)
    if results[-1][1] == "motion":
        ax1.plot(1, len(results[-1][4]), 'g.')
        ax3.plot(1, results[-1][3], 'g.')
    else:
        ax2.plot(1, len(results[-1][4]), 'g.')
        ax4.plot(1, results[-1][3], 'g.')

    plt.tight_layout()


def create_histogram(color):
    fig2 = plt.figure()
    fig2.canvas.set_window_title('LAMPA Experiment')

    ax1 = fig2.add_subplot(121)
    ax1.set_title('Motion')
    ax1.grid(True, axis='x', ls='dotted')
    ax1.tick_params(top=False, right=False)
    ax1.xaxis.set_major_locator(plt.MaxNLocator(5))

    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    ax1.set_ylim(0, 18)
    ax1.yaxis.set_ticks(range(1, 18))
    ax1.yaxis.set_ticklabels(q)
    ax1.set_xlabel('% de réponses similaires')
    ax1.set_ylabel('Answer Number')

    #  label is green if answer is right, else black.
    [t.set_color(i) for (i, t) in
     zip(color, ax1.yaxis.get_ticklabels())]

    #  Create histograms
    answers_inverse = []
    for k in range(1, 18):
        answers_inverse.extend([k] * (len(results) - answers.count(k)))

    weights_answers = [100 / len(results) for value in answers]
    weights_answers_inverse = [100 / len(results) for value in answers_inverse]

    N, bins, hist_true = ax1.hist(answers, stacked=True, bins=range(1, 19), align='left',
                                  edgecolor='black', weights=weights_answers,
                                  orientation='horizontal')
    N2, bins2, hist_false = ax1.hist(answers_inverse, stacked=True, bins=range(1, 19), align='left',
                                     edgecolor='black', weights=weights_answers_inverse,
                                     orientation='horizontal')
    front_hist(17, hist_true, hist_false, color)  # if answer is right show the true_hist, else show false_hist

    # Set the formatter to show %
    # formatter = FuncFormatter(to_percent)
    # plt.gca().xaxis.set_major_formatter(formatter)
    # plt.gca().xaxis.set_major_formatter(PercentFormatter(5))

    plt.tight_layout()


def front_hist(nbr, hist1, hist2, color):
    for k in range(nbr):
        if color[k] == "green":
            hist1[k].set_facecolor('blue')
            hist1[k].set_zorder(1)
            hist2[k].set_facecolor('white')
            hist2[k].set_edgecolor('white')
            hist2[k].set_zorder(0)
        else:
            hist1[k].set_facecolor('white')
            hist1[k].set_edgecolor('white')
            hist1[k].set_zorder(0)
            hist2[k].set_facecolor('blue')
            hist2[k].set_zorder(0)


def to_percent(value, tick_number):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    e, d = str(value * 100 / len(results)).split(".")
    return e


def add_participant():
    w = MainView()
    w.run()
    r = w.results_participant
    # print(r)
    # state_sujet = r[0]
    # type_sujet = r[1]
    #
    # if r[0] == 1:
    #     state_sujet = "yes"
    # else:
    #     state_sujet = "no"
    # if r[1] == 1:
    #     type_sujet = "motion"
    # else:
    #     type_sujet = "motionless"
    #
    answers_sujet = r[3]

    results.append([len(results) + 1, r[0], r[1], r[2], r[3]])
    write_csv("data.csv", results)

    color = ["black"] * 17
    for value in answers_sujet:
        color[value - 1] = "green"

    show_results(color)

    return color


def show_results(color=None):
    if color is not None:
        create_histogram(color)
    create_boxplot()
    plt.show()


if __name__ == "__main__":
    GAU_motion = []
    CRA_motion = []

    GAU_motionless = []
    CRA_motionless = []

    answers = []

    results = read_csv("data.csv")
    for r in results:
        if r[1] == 'motion':
            GAU_motion.append(r[3])
            CRA_motion.append(len(r[4]))
        else:
            GAU_motionless.append(r[3])
            CRA_motionless.append(len(r[4]))
        answers += r[4]

    while True:
        x = input("Commande (add/show/exit)\n")
        if x == "add":
            add_participant()
        elif x == "show":
            show_results()
        elif x == "exit":
            exit()
