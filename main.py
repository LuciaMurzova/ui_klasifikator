import random
import time
import math

vsetky_x = []
vsetky_y = []
vsetky_f = []

uspene_klasifikovane: int
pocet_bodov: int = 5000

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
    novy_bod = (x, y)
    vzdialenost = []

    if k != 15:
        vyskyt = [i for i, x1 in enumerate(vsetky_x) if x1 == x]
        for index in vyskyt:
            if vsetky_y[index] == y:
                prehladava_po_index = index
    else:
        prehladava_po_index = len(vsetky_x)

    # vypocita Euklidovske vzdialenosti od vsetkych bodov
    for index in range(prehladava_po_index):
        porovnavany_bod = (vsetky_x[index], vsetky_y[index])
        v = math.sqrt((pow((novy_bod[0] - porovnavany_bod[0]), 2) + pow((novy_bod[1] - porovnavany_bod[1]), 2)))
        vzdialenost.append((v, index))

    # usporiadanie pola vzdialenosti - prekopirovanie do noveho pola aby sme vedeli dohladat index miest
    usporiadane = sorted(vzdialenost, key=lambda x: x[0])

    cervena = zelena = modra = fialova = 0

    for najblizsi in range(k):
        index = usporiadane[najblizsi][1]
        farba = vsetky_f[index]
        if farba == R:
            cervena += 1
            continue
        elif farba == G:
            zelena += 1
            continue
        elif farba == B:
            modra += 1
            continue
        elif farba == P:
            fialova += 1

    usporiadane.clear()
    vzdialenost.clear()

    if cervena >= fialova and cervena >= modra and cervena >= zelena:
        return R
    elif modra >= cervena and modra >= zelena and modra >= fialova:
        return B
    elif zelena >= cervena and zelena >= modra and zelena >= fialova:
        return G
    else:
        return P


def kontrola_rovnakych(hladane_x, hladane_y):
    vyskyty = [i for i, x in enumerate(vsetky_x) if x == hladane_x]

    for rovnake_x in vyskyty:
        if vsetky_y[rovnake_x] == hladane_y:
            return True

    return False


def vygeneruj_unikatne(x_od, x_do, y_od, y_do, farba, k: int):
    global uspene_klasifikovane

    x = random.randint(x_od, x_do)  # vsetky_x[0]
    y = random.randint(y_od, y_do)  # vsetky_y[0]

    while kontrola_rovnakych(x, y):
        x = random.randint(x_od, x_do)
        y = random.randint(y_od, y_do)

    # klasifikacia
    pridelena_farba = klasifikuj(x, y, k)

    # porovnanie vratenej triedy s tou v ktorej bola vygenerovana
    if pridelena_farba == farba:
        uspene_klasifikovane += 1

    # pridanie do pola vsetkych bodov
    vsetky_x.append(x)
    vsetky_y.append(y)
    vsetky_f.append(pridelena_farba)


def generuj_cervene(k: int):
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

    vygeneruj_unikatne(x_od, x_do, y_od, y_do, R, k)


def generuj_zelene(k: int):
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

    vygeneruj_unikatne(x_od, x_do, y_od, y_do, G, k)


def generuj_modre(k: int):
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

    vygeneruj_unikatne(x_od, x_do, y_od, y_do, B, k)


def generuj_fialove(k: int):
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

    vygeneruj_unikatne(x_od, x_do, y_od, y_do, P, k)


def zapis(suborx, subory, suborf):
    vystupx = open(suborx, 'w')
    for x in vsetky_x:
        vystupx.write('%s\n' % x)
    vystupx.close()

    vystupy = open(subory, 'w')
    for x in vsetky_y:
        vystupy.write('%s\n' % x)
    vystupy.close()

    vystupf = open(suborf, 'w')
    for x in vsetky_f:
        vystupf.write('%s\n' % x)
    vystupf.close()


def otestuj_bez_generovania(k, suborx, subory, suborf):
    global uspene_klasifikovane
    uspene_klasifikovane = 0

    for g in range(20, pocet_bodov*4+20, 4):
        vsetky_f[g] = klasifikuj(vsetky_x[g], vsetky_y[g], k)
        if vsetky_f[g] == R:
            uspene_klasifikovane += 1

        vsetky_f[g+1] = klasifikuj(vsetky_x[g+1], vsetky_y[g+1], k)
        if vsetky_f[g+1] == G:
            uspene_klasifikovane += 1

        vsetky_f[g+2] = klasifikuj(vsetky_x[g+2], vsetky_y[g+2], k)
        if vsetky_f[g+2] == B:
            uspene_klasifikovane += 1

        vsetky_f[g+3] = klasifikuj(vsetky_x[g+3], vsetky_y[g+3], k)
        if vsetky_f[g+3] == P:
            uspene_klasifikovane += 1

    zapis(suborx, subory, suborf)
    print("Uspesnost k=7", uspene_klasifikovane / (pocet_bodov * 4))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    start_time = time.time()

    uspene_klasifikovane = 0
    inicializacia()

    k = 15
    for g in range(pocet_bodov):
        generuj_cervene(k)
        generuj_zelene(k)
        generuj_modre(k)
        generuj_fialove(k)

    zapis('vystup15x.txt', 'vystup15y.txt', 'vystup15f.txt')
    print("Uspesnost k=15", uspene_klasifikovane / (pocet_bodov * 4))
    print("--- %s seconds ---" % (time.time() - start_time))

    otestuj_bez_generovania(7, 'vystup7x.txt', 'vystup7y.txt', 'vystup7f.txt')
    otestuj_bez_generovania(3, 'vystup3x.txt', 'vystup3y.txt', 'vystup3f.txt')
    otestuj_bez_generovania(1, 'vystup1x.txt', 'vystup1y.txt', 'vystup1f.txt')
