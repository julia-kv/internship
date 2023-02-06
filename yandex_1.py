import math
from random import uniform

def generate1():
    a = uniform(0, 1)
    b = uniform(0, 1)
    return (a * math.cos(2 * math.pi * b), a * math.sin(2 * math.pi * b))


def generate2():
    while True:
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return (x, y)


def tr(n):
    gen1 = []
    gen2 = []
    for _ in range(n):
        gen1.append(yandex_1.generate1())
        gen2.append(yandex_1.generate2())

    sum_gen1 = [0, 0]
    sum_gen2 = [0, 0]
    for a, b in zip(gen1, gen2):
        sum_gen1[0] += a[0]
        sum_gen1[1] += a[1]
        sum_gen2[0] += b[0]
        sum_gen2[1] += b[1]
    print(f" {sum_gen1[0] / n} | {sum_gen1[1] / n}")
    print(f" {sum_gen2[0] / n} | {sum_gen2[1] / n}")
    print("_____")
    return gen1, gen2

def plots():
    gen1_x = []
    gen1_y = []
    for _ in range(1000):
        x = yandex_1.generate1()
        gen1_x.append(x[0])
        gen1_y.append(x[1])

    print(np.var(gen1_x))
    print(np.var(gen1_y))
    # plt.hist(gen1_x)
    # plt.title("Gen2")
    # plt.show()
    # plt.hist(gen1_y)
    # plt.title("Gen1")
    # plt.show()

    gen2_x = []
    gen2_y = []
    for _ in range(1000):
        x = yandex_1.generate2()
        gen2_x.append(x[0])
        gen2_y.append(x[1])
    # plt.hist(gen2_x)
    # plt.title("Gen2")
    # plt.show()
    #
    # plt.hist(gen2_y)
    # plt.title("Gen2")
    # plt.show()
    print(np.var(gen2_x))
    print(np.var(gen2_y))


def res():
    l = [float(x) for x in input().split()]
    s1, s2 = 0, 0
    for a in range(0, 2000, 2):
        s1 += l[a]
    s1 = s1 / 1000

    d1, d2 = 0, 0
    for a in range(0, 2000, 2):
        d1 += (l[a] - s1) ** 2
    d1 = d1 / 999
    if d1 < 0.2:
        print("1")
    else:
        print("2")