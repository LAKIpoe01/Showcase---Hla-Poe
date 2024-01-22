import random as r
import haravasto as h
import math as m
import time as t

tila = {
    "kentta": []
}
pkentta = {
    "kentta": []
}
muu = {
    "jaljella": 0,
    "kesto": 0,
    "aika": None,
    "vuorot": 0,
    "miina": 0,
    "tulos": False,
    "xleveys": 0,
    "ykorkeus": 0,
    "gamer": None,
    "lopetus": "Jäänyt kesken"
}
hiiri = {
    h.HIIRI_VASEN : "vasen",
    h.HIIRI_KESKI : "keski",
    h.HIIRI_OIKEA : "oikea"
}

def main():
    """
    Kutsuu kaikkia muita funktioita.
    """
    print("Tervetuloa pelaamaan Miinantallaajaa tuleva mestaripioneeri!")
    muu["gamer"] = input("Pelaajan nimi: ")
    while True:
        mode = valikko()
        if mode == 1:
            ky = kysykentta()
            muu["xleveys"] = ky[0]
            muu["ykorkeus"] = ky[1]
            muu["miina"] = ky[2]
            kentta = []
            for rivi in range(muu["ykorkeus"]):
                kentta.append([])
                for sarake in range(muu["xleveys"]):
                    kentta[-1].append(" ")
            dn = []
            for rivi in range(muu["ykorkeus"]):
                dn.append([])
                for sarake in range(muu["xleveys"]):
                    dn[-1].append(" ")
            tila["kentta"] = kentta
            pkentta["kentta"] = dn
            jaljella = []
            for xjaljella in range(muu["xleveys"]):
                for yjaljella in range(muu["ykorkeus"]):
                    jaljella.append((xjaljella, yjaljella))
            miinoita(tila["kentta"], jaljella, muu["miina"])
            h.lataa_kuvat(".\\spritet")
            h.luo_ikkuna(len(tila["kentta"][0])*40, len(tila["kentta"]*40))
            h.aseta_piirto_kasittelija(piirra_kentta)
            muu["lopetus"] = "Jäänyt kesken"
            muu["vuorot"] = 0
            muu["aika"] = t.localtime()
            muu["kesto"] = t.time()
            h.aloita()
            muu["kesto"] = t.time() - muu["kesto"]
            tilasto("kirjoitus")
        elif mode == 2:
            tilasto("katselu")
        else:
            break

def kysykentta():
    """
    Kysyy pelaajalta kentän leveyden, korkeuden ja miinojen määrän. Tarkistaa myös, että annetut arvot ovat toimivia ohjelmassa.
    """
    while True:
        try:
            leveys = int(input("Kentän leveys: "))
        except ValueError:
            print("Syötä leveys kokonaislukuna!")
        else:
            if leveys < 1:
                print("Anna luku, joka on suurempi kuin 0!")
            elif leveys > 48:
                print("Ei noin iso kenttä mahdu kuvaruudulle!")
            else:
                break
    while True:
        try:
            korkeus = int(input("Kentän korkeus: "))
        except ValueError:
            print("Syötä korkeus kokonaislukuna!")
        else:
            if korkeus < 1:
                print("Anna luku, joka on suurempi kuin 0!")
            elif korkeus > 27:
                print("Ei noin iso kenttä mahdu kuvaruudulle!")
            else:
                break
    while True:    
        try:
            miinat = int(input("Miinojen määrä: "))
        except ValueError:
            print("Syötä miinojen lukumäärä kokonaislukuna!")
        else:
            if miinat < 1:
                print("Anna luku, joka on suurempi kuin 0!")
            elif miinat > korkeus * leveys:
                print("Ei annetulle kentälle mahdu noin montaa miinaa!")
            else:
                return leveys, korkeus, miinat

def miinoita(kentta, ruudut, miinat):
    """
    Asettaa kentälle annetun määrän miinoja satunnaisiin paikkoihin. Jokainen miina korottaa
    viereisen ruudun arvoa yhdellä. Ottaa huomioon kaikki mahdolliset erityistapaukset, kuten nurkat.
    """
    miinoite = r.sample(ruudut, k=miinat)
    korkeus = len(kentta)
    leveys = len(kentta[0])
    muu["jaljella"] = muu["ykorkeus"] * muu["xleveys"] - muu["miina"]
    for x, y in miinoite:
        kentta[y][x] = "x"
        if (x >= 0 and x <=muu["xleveys"]-2) and (y >= 0 and y <= muu["ykorkeus"]-1):
            if kentta[y][x+1] != "x":
                if kentta[y][x+1] == " ":
                    kentta[y][x+1] = "1"
                elif kentta[y][x+1] == "1":
                    kentta[y][x+1] = "2"
                elif kentta[y][x+1] == "2":
                    kentta[y][x+1] = "3"
                elif kentta[y][x+1] == "3":
                    kentta[y][x+1] = "4"
                elif kentta[y][x+1] == "4":
                    kentta[y][x+1] = "5"
                elif kentta[y][x+1] == "5":
                    kentta[y][x+1] = "6"
                elif kentta[y][x+1] == "6":
                    kentta[y][x+1] = "7"
                else:
                    kentta[y][x+1] = "8"
                

        if (x >=1 and x <= muu["xleveys"]-1) and (y >= 0 and y <= muu["ykorkeus"]-1):
            if kentta[y][x-1] != "x":
                if kentta[y][x-1] == " ":
                    kentta[y][x-1] = "1"
                elif kentta[y][x-1] == "1":
                    kentta[y][x-1] = "2"
                elif kentta[y][x-1] == "2":
                    kentta[y][x-1] = "3"
                elif kentta[y][x-1] == "3":
                    kentta[y][x-1] = "4"
                elif kentta[y][x-1] == "4":
                    kentta[y][x-1] = "5"
                elif kentta[y][x-1] == "5":
                    kentta[y][x-1] = "6"
                elif kentta[y][x-1] == "6":
                    kentta[y][x-1] = "7"
                else:
                    kentta[y][x-1] = "8"
                
            
        if (x >= 1 and x <= muu["xleveys"]-1) and (y >= 1 and y <= muu["ykorkeus"]-1):
            if kentta[y-1][x-1] != "x":
                if kentta[y-1][x-1] == " ":
                    kentta[y-1][x-1] = "1"
                elif kentta[y-1][x-1] == "1":
                    kentta[y-1][x-1] = "2"
                elif kentta[y-1][x-1] == "2":
                    kentta[y-1][x-1] = "3"
                elif kentta[y-1][x-1] == "3":
                    kentta[y-1][x-1] = "4"
                elif kentta[y-1][x-1] == "4":
                    kentta[y-1][x-1] = "5"
                elif kentta[y-1][x-1] == "5":
                    kentta[y-1][x-1] = "6"
                elif kentta[y-1][x-1] == "6":
                    kentta[y-1][x-1] = "7"
                else:
                    kentta[y-1][x-1] = "8"
                

        if (x >= 0 and x <= muu["xleveys"]-2) and (y >= 1 and y <= muu["ykorkeus"]-1):
            if kentta[y-1][x+1] != "x":
                if kentta[y-1][x+1] == " ":
                    kentta[y-1][x+1] = "1"
                elif kentta[y-1][x+1] == "1":
                    kentta[y-1][x+1] = "2"
                elif kentta[y-1][x+1] == "2":
                    kentta[y-1][x+1] = "3"
                elif kentta[y-1][x+1] == "3":
                    kentta[y-1][x+1] = "4"
                elif kentta[y-1][x+1] == "4":
                    kentta[y-1][x+1] = "5"
                elif kentta[y-1][x+1] == "5":
                    kentta[y-1][x+1] = "6"
                elif kentta[y-1][x+1] == "6":
                    kentta[y-1][x+1] = "7"
                else:
                    kentta[y-1][x+1] = "8"
                

        if (x >= 0 and x <= muu["xleveys"]-1) and (y >= 1 and y <= muu["ykorkeus"]-1):
            if kentta[y-1][x] != "x":
                if kentta[y-1][x] == " ":
                    kentta[y-1][x] = "1"
                elif kentta[y-1][x] == "1":
                    kentta[y-1][x] = "2"
                elif kentta[y-1][x] == "2":
                    kentta[y-1][x] = "3"
                elif kentta[y-1][x] == "3":
                    kentta[y-1][x] = "4"
                elif kentta[y-1][x] == "4":
                    kentta[y-1][x] = "5"
                elif kentta[y-1][x] == "5":
                    kentta[y-1][x] = "6"
                elif kentta[y-1][x] == "6":
                    kentta[y-1][x] = "7"
                else:
                    kentta[y-1][x] = "8"

        
        if (x >=0 and x <= muu["xleveys"]-2) and (y >= 0 and y <= muu["ykorkeus"]-2):
           if kentta[y+1][x+1] != "x":
                if kentta[y+1][x+1] == " ":
                    kentta[y+1][x+1] = "1"
                elif kentta[y+1][x+1] == "1":
                    kentta[y+1][x+1] = "2"
                elif kentta[y+1][x+1] == "2":
                    kentta[y+1][x+1] = "3"
                elif kentta[y+1][x+1] == "3":
                    kentta[y+1][x+1] = "4"
                elif kentta[y+1][x+1] == "4":
                    kentta[y+1][x+1] = "5"
                elif kentta[y+1][x+1] == "5":
                    kentta[y+1][x+1] = "6"
                elif kentta[y+1][x+1] == "6":
                    kentta[y+1][x+1] = "7"
                else:
                    kentta[y+1][x+1] = "8"

            
        if (x >= 1 and x <= muu["xleveys"]-1) and (y >= 0 and y <= muu["ykorkeus"]-2):
            if kentta[y+1][x-1] != "x":
                if kentta[y+1][x-1] == " ":
                    kentta[y+1][x-1] = "1"
                elif kentta[y+1][x-1] == "1":
                    kentta[y+1][x-1] = "2"
                elif kentta[y+1][x-1] == "2":
                    kentta[y+1][x-1] = "3"
                elif kentta[y+1][x-1] == "3":
                    kentta[y+1][x-1] = "4"
                elif kentta[y+1][x-1] == "4":
                    kentta[y+1][x-1] = "5"
                elif kentta[y+1][x-1] == "5":
                    kentta[y+1][x-1] = "6"
                elif kentta[y+1][x-1] == "6":
                    kentta[y+1][x-1] = "7"
                else:
                    kentta[y+1][x-1] = "8"
                
            
        if (x >= 0 and x <= muu["xleveys"]-1) and (y >= 0 and y <= muu["ykorkeus"]-2):
            if kentta[y+1][x] != "x":
                if kentta[y+1][x] == " ":
                    kentta[y+1][x] = "1"
                elif kentta[y+1][x] == "1":
                    kentta[y+1][x] = "2"
                elif kentta[y+1][x] == "2":
                    kentta[y+1][x] = "3"
                elif kentta[y+1][x] == "3":
                    kentta[y+1][x] = "4"
                elif kentta[y+1][x] == "4":
                    kentta[y+1][x] = "5"
                elif kentta[y+1][x] == "5":
                    kentta[y+1][x] = "6"
                elif kentta[y+1][x] == "6":
                    kentta[y+1][x] = "7"
                else:
                    kentta[y+1][x] = "8"
                  
def piirra_kentta():
    """
    Piirtää pelikentän peliruudulle.
    """
    h.tyhjaa_ikkuna ()
    h.piirra_tausta ()
    h.aseta_hiiri_kasittelija(kasittele_hiiri)
    h.aloita_ruutujen_piirto ()
    for y, joo in enumerate(pkentta["kentta"]):
        for x, ruutu in enumerate(joo):
            h.lisaa_piirrettava_ruutu(ruutu, x*40 , y*40)
    h.piirra_ruudut ()

def kasittele_hiiri(x, y, painike, muokkaus):
    """
    Selvittää mitä hiirellä tehdään ja käyttää saamiaan arvoja pelin kulkuun.
    """
    if hiiri[painike] == "vasen":    
        if pkentta["kentta"][m.floor(y/40)][m.floor(x/40)] == " ":
            if tila["kentta"][m.floor(y/40)][m.floor(x/40)] == " ":
                tulvataytto(tila["kentta"], m.floor(x/40), m.floor(y/40))
                muu["vuorot"] += 1
            h.aseta_piirto_kasittelija(piirra_kentta)

        if tila["kentta"][m.floor(y/40)][m.floor(x/40)] == "x":
            muu["lopetus"] = "Häviö"
            h.lopeta()
            print("Hävisit! Voi himpskatti!")
    
        if tila["kentta"][m.floor(y/40)][m.floor(x/40)] in ["1", "2", "3", "4", "5", "6", "7", "8", "f"]:
            pkentta["kentta"][m.floor(y/40)][m.floor(x/40)] = tila["kentta"][m.floor(y/40)][m.floor(x/40)]
            muu["jaljella"] -= 1
            muu["vuorot"] += 1
            h.aseta_piirto_kasittelija(piirra_kentta)

        if muu["jaljella"] == 0:
            h.lopeta()
            muu["lopetus"] = "Voitto"
            print("")
            print("Onnea, Voitit!")

    elif hiiri[painike] == "oikea":
        if pkentta["kentta"][m.floor(y/40)][m.floor(x/40)] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            if pkentta["kentta"][m.floor(y/40)][m.floor(x/40)] == "f":
                pkentta["kentta"][m.floor(y/40)][m.floor(x/40)] = " "
            else:
                pkentta["kentta"][m.floor(y/40)][m.floor(x/40)] = "f"

def tulvataytto(kentura, xkoordinaatti, ykoordinaatti):
    """
    Painettaessa tyhjää ruutua, tämä funktio avaa kaikki sen vieressä olevat tyhjät ruudut ja niiden viereiset numeroruudut.
    """
    lista = [(xkoordinaatti, ykoordinaatti)]
    korkeus = muu["ykorkeus"]
    leveys = muu["xleveys"]
    if pkentta["kentta"][ykoordinaatti][xkoordinaatti] not in ["x", "1", "2", "3", "4", "5", "6", "7", "8", "f"]:
        while lista:
            x, y = lista.pop()            
            if pkentta["kentta"][y][x] == " ":
                muu["jaljella"] -= 1
                kentura[y][x] = "0"        
                pkentta["kentta"][y][x] = kentura[y][x]
                for i in range(y-1, y+2):
                    for k in range(x-1, x+2):
                        if i >= 0 and k >= 0:
                            if i <= korkeus-1 and k <= leveys-1:
                                if kentura[i][k] == " ":
                                    lista.append((k, i))
                                if kentura[i][k] in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                                    if pkentta["kentta"][i][k] != kentura[i][k]:
                                        muu["jaljella"] -= 1
                                    pkentta["kentta"][i][k] = kentura[i][k]

def tilasto(muoto):
    """
    Kutsumistavasta riippuen joko kirjaa uuden tuloksen tilastolistaan tai näyttää nykyisen tilastolistan.
    """
    if muoto == "kirjoitus":
        try:
            with open("tilasto.txt", "a") as kohde:
                sekunti = int(muu["kesto"]%60)
                minuutti = int(muu["kesto"]/60)
                aika = t.strftime("%d.%m.%Y %H:%M", muu["aika"])
                kohde.write("{}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(muu["gamer"], sekunti, minuutti, aika, muu["vuorot"], muu["xleveys"], muu["ykorkeus"], muu["miina"], muu["lopetus"]))
        except IOError:
                print("Tallennus epäonnistui, tiedostoa ei voitu avata")
    elif muoto == "katselu":
        try:
            with open("tilasto.txt", "r") as kohde:
                for rivi in kohde:
                    muokkaus = rivi.rstrip()
                    listaus = muokkaus.split(",")
                    print("{} pelasi {} vuoroa, peli alkoi {} ja kesti {} min {} sec.".format(listaus[0], listaus[4], listaus[3], listaus[2], listaus[1]))
                    print("Kenttä oli: {} x {} kokoinen".format(listaus[5], listaus[6]))
                    print("Miinojen lukumäärä: {}".format(listaus[7]))
                    print("Lopputulos: {}".format(listaus[8]))
                    print("")
        except IOError:
            print("Dataa ei ole olemassa.")

def valikko():
    """
    Avaa pelivalikon.
    """
    print("\nValitse yksi näistä vaihtoehdoista:")
    print("1: Uusi peli")
    print("2: Avaa tilastolista")
    print("3: Poistu pelistä" + "\n")
    
    while True:
        try:
            joo = int(input("Anna valintasi numero: "))
        except ValueError:
            print("Anna vain valinnan numero!")
        else:
            if joo > 0 and joo < 4:
                return joo

if __name__ == "__main__":
    main()