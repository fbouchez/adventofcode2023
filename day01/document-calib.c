#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define BUFLEN 1024

bool part2 = false;
/* bool part2 = true; */


char* chiffres[10] = {
    "zeroINTROUVABLE",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
};


// renvoie un int > 0 si c'est un chiffre
// sinon renvoie -1
int estunchiffre(char *ptr)
{
    if (isdigit(*ptr)) {
        return *ptr - '0';
    }

    if (!part2) {
        return -1;
    }

    for (int digit=0; digit<10; digit++) {
        int len = strlen(chiffres[digit]);
        if (!strncmp(ptr, chiffres[digit], len)) {
            return digit;
        }
    }

    return -1;
}


int analyse_ligne(char *line)
{
    char *c = line;
    int prem = -1;
    int dern = -1;

    while (*c) {
        int digit = estunchiffre(c);
        if (digit >= 0) {
            if (prem == -1) {
                prem = digit;
                dern = digit;
                printf("trouvé premier: %d\n", prem);
            } else {
                dern = digit;
                printf("trouvé dernier?: %d\n", dern);
            }
        }
        c++;
    }

    return prem*10 + dern;
}


void calibration(void)
{
    char buffer[BUFLEN];
    int somme = 0;

    while (!feof(stdin)) {
        char *ret = fgets(buffer, BUFLEN-1, stdin);

        if (!ret) {break;}

        printf("Ligne: %s", buffer);

        int num = analyse_ligne(buffer);

        printf("Numéro extrait: %d\n\n", num);

        somme += num;
    }

    printf("Valeur totale de la calibration: %d\n", somme);
}


int main(void)
{
    calibration();
    exit(0);
}
