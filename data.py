import csv


def write_csv(file, data):
    with open(file, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerows(data)


def read_csv(file):
    data = []
    with open(file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


if __name__ == "__main__":
    print("start")
    # numéro, type, used, GAU, CAR

    results = [
        [1, "motion", "yes", 17, [1, 7, 10, 11, 17]],
        [2, "motion", "yes", 27, [1, 2, 4, 6, 10]],
        [3, "motion", "yes", 20, [1, 3, 6, 7, 9, 10, 11, 17]],
        [4, "motion", "yes", 12, [3, 4, 6, 7, 8, 9, 10, 11, 12, 16]],
        [5, "motionless", "yes", 15, [1, 3, 6, 8, 9, 12]]
    ]
    end_results = [["number", "state", "usedtoVR", "Gau"] + ["Car" + str(i + 1) for i in range(17)]]
    end_results.extend([[r[0], r[1], r[2], r[3]] for r in results])
    for i in range(1, len(end_results)):
        car = [0] * 17
        for value in results[i - 1][4]:
            car[value - 1] = 1
        end_results[i].extend(car)
    write_csv('data.csv', end_results)
    res = read_csv("data.csv")
    for r in res:
        print(r)
