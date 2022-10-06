def zakres(szukana, liczba, tablica):
    """
    :param szukana:
    :param liczba:
    :param tablica:
    :return: zakres adresu:
    """
    dmax = liczba - 1
    if szukana == tablica[dmax]:
        for i in tablica[dmax:]:
            if dmax < len(tablica) and szukana == tablica[dmax]:
                # print(tablica.index(i, dmax, (len(tablica) - 1)))
                dmax += 1
        dmin = liczba - 1
        for i in tablica[:(liczba)][::-1]:
            if dmin > 0 and szukana == tablica[dmin]:
                dmin -= 1
            elif dmin == 0 and szukana == tablica[dmin]:
                dmin = 0
            else:
                dmin += 1
                break
        return [dmin, (dmax - 1)]
    else:
        return "None"


def compare_list(lista1, lista2, zakres):
    x = zakres[0]
    y = zakres[1]
    print(x, y)
    tmp_list = list()
    for i in range(x, y+1):
        tmp_list.append(1) if lista1[i] == lista2[i] else tmp_list.append(0)
    print(tmp_list)


name1 = [1, 1, 0, 1, 1, 1, 1]
name2 = [1, 1, 1, 1, 0, 0, 1]
name3 = [0, 0, 1, 1, 0, 1, 1]
name4 = [1, 0, 0, 1, 1, 1, 1]
name5 = ["a", "b", "c", "d", "e", "f", "g", "h"]

szukana = 1
liczba = 4
print(zakres(szukana, liczba, name1))
d = zakres(szukana, liczba, name1)
compare_list(name1, name2, d)
