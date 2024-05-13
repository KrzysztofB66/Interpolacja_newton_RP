import math
# Podane dane
f_x = [-524, -36, -4, -44, -540]
x = [-4, -2, 0, 2, 4]
h = 2


def roznice_progresywne(y):
    if len(y) < 2:
        return y
    else:
        d = [y[i+1] - y[i] for i in range(len(y)-1)]
        return [y[0]] + roznice_progresywne(d)


def oblicz_wspolczynniki(roznice_prog, h):
    d = []
    for i in range(0, len(roznice_prog)):
        if i == 0:
            d.append(roznice_prog[0])
        else:
            d.append(roznice_prog[i] / (math.factorial(i) * h**i))
    return d


def oblicz_wielomian(wspolczyniki, x_, x):
    wynik = 0
    iloczyn = 1
    for i in range(0, len(wspolczyniki)):
        if i == 0:
            wynik += wspolczyniki[0]
        else:
            for j in range(0, i):
                iloczyn *= (x - x_[j])
            wynik += wspolczyniki[i] * iloczyn
            iloczyn = 1
    return wynik


print(oblicz_wielomian(oblicz_wspolczynniki(roznice_progresywne(f_x), h), x, 3))
