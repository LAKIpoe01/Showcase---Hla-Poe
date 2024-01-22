from turtle import *

def piirra_spiraali(vari, kaari, alkusade, kasvu, v_paksuus = 1):
    """piirtaa spiraalin"""
    color(vari)
    pensize(int(v_paksuus))
    for i in range(int(kaari)):
        alkusade += kasvu
        circle(alkusade , 90)
piirra_spiraali("black", 20, 10, 3)
piirra_spiraali("red", 10, 20, 4, 3)
piirra_spiraali("blue", 10, -20, -4, 3)
done()
