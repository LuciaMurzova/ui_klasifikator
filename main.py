import random
import time

import matplotlib.pyplot as plt

vsetky_x = []
vsetky_y = []
vsetky_f = []

uspene_klasifikovane: int

R = "red"
G = "green"
B = "blue"
P = "purple"


def inicializacia():
    for x in range(2):
        vsetky_x.extend([-4500, -4100, -1800, -2500, -2000, 4500, 4100, 1800, 2500, 2000])

    for y in range(2):
        vsetky_y.extend([-4400, -3000, -2400,  -3400, -1400])
    for y in range(2):
        vsetky_y.extend([4400, 3000, 2400, 3400, 1400])

    vsetky_f.extend([R, R, R, R, R, G, G, G, G, G, B, B, B, B, B, P, P, P, P, P])


def klasifikuj(x: int, y: int, k: int):
    # hladame k najblizsich susedov
    print('haha')


def kontrola_rovnakych(hladane_x, hladane_y):
    vyskyty = [i for i, x in enumerate(vsetky_x) if x == hladane_x]

    for rovnake_x in vyskyty:
        if vsetky_y[rovnake_x] == hladane_y:
            return True

    return False


def vygeneruj_unikatne(x_od, x_do, y_od, y_do, farba):
    x = random.randint(x_od, x_do)  # vsetky_x[0]
    y = random.randint(y_od, y_do)  # vsetky_y[0]

    while kontrola_rovnakych(x, y):
        x = random.randint(x_od, x_do)
        y = random.randint(y_od, y_do)

    vsetky_x.append(x)
    vsetky_y.append(y)
    vsetky_f.append(farba)


def generuj_cervene():
    pravdepodobnost = random.randint(1, 100)
    if pravdepodobnost == 1:
        x_od = -5000
        x_do = 5000
        y_od = -5000
        y_do = 5000
    else:
        x_od = -5000
        x_do = 500
        y_od = -5000
        y_do = 500

    vygeneruj_unikatne(x_od, x_do, y_od, y_do, R)


def generuj_zelene():
    pravdepodobnost = random.randint(1, 100)
    if pravdepodobnost == 1:
        x_od = -5000
        x_do = 5000
        y_od = -5000
        y_do = 5000
    else:
        x_od = -500
        x_do = 5000
        y_od = -5000
        y_do = 500

    vygeneruj_unikatne(x_od, x_do, y_od, y_do, G)


def generuj_modre():
    pravdepodobnost = random.randint(1, 100)
    if pravdepodobnost == 1:
        x_od = -5000
        x_do = 5000
        y_od = -5000
        y_do = 5000
    else:
        x_od = -5000
        x_do = 500
        y_od = -500
        y_do = 5000

    vygeneruj_unikatne(x_od, x_do, y_od, y_do, B)


def generuj_fialove():
    pravdepodobnost = random.randint(1, 100)
    if pravdepodobnost == 1:
        x_od = -5000
        x_do = 5000
        y_od = -5000
        y_do = 5000
    else:
        x_od = -500
        x_do = 5000
        y_od = -500
        y_do = 5000

    vygeneruj_unikatne(x_od, x_do, y_od, y_do, P)


def vykresli():
    # Dorobit 4 grafy v jednom - https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html

    plt.scatter(vsetky_x, vsetky_y, color=vsetky_f, s=5)
    plt.xlim(-5300, 5300)
    plt.ylim(-5300, 5300)

    plt.xticks([-5000, -4000, -3000, -2000, -1000, -500, 0, 500, 1000, 2000, 3000, 4000, 5000], fontsize=7)
    plt.yticks([-5000, -2500, -500, 0, 500, 2500, 5000], fontsize=7)

    plt.show()


if __name__ == '__main__':
    start_time = time.time()

    uspene_klasifikovane = 0
    inicializacia()

    # DOROBIT - klasifikaciu
    # kontrola rychlejsia pri rozdeleni do mensich stvorcov

    for g in range(5000):
        generuj_cervene()
        generuj_zelene()
        generuj_modre()
        generuj_fialove()

    print("--- %s seconds ---" % (time.time() - start_time))

    vykresli()

