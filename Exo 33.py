tab = [5,0,7,9,1,2]


def partition(tab, pivot) :
    i = 0
    for j in range(0, len(tab)) :
        if tab[j] <= pivot :
            interm = tab[i]
            tab[i] = tab[j]
            tab[j] = interm
            i = i +1
    pos = i - 1
    return pos

def tri_rapide(tab) :
    if len(tab) > 1 :
        pos = position(tab, tab[0])
        inter = tab[0]
        tab[0] = tab[pos]
        tab[pos] = inter
        tri_rapide(tab[:pos])
        tri_rapide(tab[pos + 1:])


print(tri_rapide(tab))