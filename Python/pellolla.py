ELAIMET = {
    "a": "aasi",
    "k": "koira",
    "@": "kissa",
    "h": "hemuli",
    "l": "lammas"
}
pelto = [
    [" ", "a", " ", " ", "l"],
    [" ", "k", "@", "k", " "],
    ["h", " ", "a", "k", " "]
]
def tutki_ruutu(merkkijono, rivi, sarake):
    """
    Funktio tutkii ruudun - jos siellä on eläin, se tulostaa eläimen sijainnin sekä nimen.
    """
    if merkkijono in ELAIMET:
        print(f"Ruudusta ({sarake}, {rivi}) löytyy {ELAIMET[merkkijono]}")

def tutki_kentta(pelto_1):
    """
    Funktio tutkii kentän sisällön käymällä sen kokonaan läpi kutsuen tutki_ruutu-funktiota
    jokaiselle kentän sisällä olevalle alkiolle.
    """
    for i, rivi in enumerate(pelto_1):
        for k, sana in enumerate(rivi):
            if sana in ELAIMET:
                tutki_ruutu(sana, i, k)

tutki_kentta(pelto)
