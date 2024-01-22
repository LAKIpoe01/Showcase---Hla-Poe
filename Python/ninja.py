huone = [
    ['N', ' ', ' ', ' ', ' '],
    ['N', 'N', 'N', 'N', ' '],
    ['N', ' ', 'N', ' ', ' '],
    ['N', 'N', 'N', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]
def laske_ninjat(xkoordinaatti, ykoordinaatti, lista):
    """
Laskee annetussa huoneessa yhden ruudun ympärillä olevat ninjat ja palauttaa
niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
ole ninjaa - jos on, sekin lasketaan mukaan.
"""
    ninjoja = 0
    korkeus = len(lista)
    leveys = len(lista[0])

    for i in range(ykoordinaatti-1, ykoordinaatti+2):
        for k in range(xkoordinaatti-1, xkoordinaatti+2):
            if i >= 0 and k >= 0:
                if i <= korkeus-1 and k <= leveys-1:
                    if lista[i][k] == "N":
                        ninjoja += 1
    return ninjoja
print(" ", "- " * 5)
for rivi in huone:
    print("|", " ".join(rivi), "|")
print(" ", "- " * 5)
x_korpo = int(input("Anna x-koordinaatti: "))
y_korpo = int(input("Anna y-koordinaatti: "))
print(laske_ninjat(x_korpo, y_korpo, huone))
    