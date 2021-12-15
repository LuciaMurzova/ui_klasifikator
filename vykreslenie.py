from matplotlib import pyplot as plt


def vykresli(suborx, subory, suborf):
    with open(suborx) as f:
        x15 = [int(x) for x in f]

    with open(subory) as f:
        y15 = [int(x) for x in f]

    with open(suborf) as f:
        fa15 = [x for x in f]

    for farba in range(len(fa15)):
        dlzka = len(fa15[farba])
        stara = fa15[farba]
        nova = stara[:dlzka - 1]
        fa15[farba] = nova

    plt.scatter(x15, y15, color=fa15, s=9)
    plt.xlim(-5300, 5300)
    plt.ylim(-5300, 5300)

    plt.xticks([-5000, -4000, -3000, -2000, -1000, -500, 0, 500, 1000, 2000, 3000, 4000, 5000], fontsize=7)
    plt.yticks([-5000, -2500, -500, 0, 500, 2500, 5000], fontsize=7)
    plt.show()


vykresli('vystup15x.txt', 'vystup15y.txt', 'vystup15f.txt')
vykresli('vystup7x.txt', 'vystup7y.txt', 'vystup7f.txt')
vykresli('vystup3x.txt', 'vystup3y.txt', 'vystup3f.txt')
vykresli('vystup1x.txt', 'vystup1y.txt', 'vystup1f.txt')

