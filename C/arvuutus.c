#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

int main() {
    int arvattavaLuku, arvaus;
    char jatketaanko;
    
    srand(time(NULL));
    
    do {
        arvattavaLuku = rand() % 100 + 1;
        
        printf("Arvaa luku (1-100): ");

        while (scanf("%d", &arvaus) != 1) {
            printf("Virheellinen syöte. Syötä luku (1-100): ");
            while (getchar() != '\n');
            scanf("%d", &arvaus);
        }
        
        while (arvaus != arvattavaLuku) {
            if (arvaus < arvattavaLuku) {
                printf("Liian pieni luku, yrita uudelleen.\n\n");
            } else {
                printf("Liian suuri luku, yrita uudelleen.\n\n");
            }
            
            printf("Arvaa luku (1-100): ");

            while (scanf("%d", &arvaus) != 1) {
                printf("Virheellinen syöte. Syötä luku (1-100): ");
                while (getchar() != '\n');
                scanf("%d", &arvaus);
            }
        }
        
        printf("OIKEIN!\n");
        printf("Haluatko yrittaa uudelleen (vastaa k, jos haluat jatkaa ja e jos et halua jatkaa pelia)?\n");
        scanf(" %c", &jatketaanko);
        
        while (tolower(jatketaanko) != 'k' && tolower(jatketaanko) != 'e') {
            printf("Virheellinen syöte. Haluatko yrittää uudelleen? (k/e): ");
            scanf(" %c", &jatketaanko);
        }
        
    } while (tolower(jatketaanko) == 'k');
    
    return 0;
}