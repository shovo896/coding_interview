#include <stdio.h>

int main(void) {
    int n = 5;

    for (int i = 1; i <= n; i++) {
        int spaces = n - i;

        while (spaces--) {
            printf(" ");
        }

        for (int j = i; j >= 1; j--) {
            printf("%d", j);
        }

        printf("\n");
    }

    return 0;
}
