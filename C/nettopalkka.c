#include <stdio.h>

int main() {
    double tuntipalkka, tehdyt_tunnit, veroprosentti, bruttopalkka, vero, nettopalkka;

    printf("Anna tuntipalkka: ");
    scanf("%lf", &tuntipalkka);

    printf("Tehdyt tunnit: ");
    scanf("%lf", &tehdyt_tunnit);

    printf("Veroprosentti: ");
    scanf("%lf", &veroprosentti);

    bruttopalkka = tuntipalkka * tehdyt_tunnit;

    vero = (veroprosentti / 100.0) * bruttopalkka;

    nettopalkka = bruttopalkka - vero;

    printf("Nettopalkkasi on %.2lf euroa, josta veron osuus on %.2lf euroa\n", nettopalkka, vero);

    return 0;
}