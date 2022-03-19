#include <stdio.h>

int sum(int i, int n) {
    int k;
    int solution = 0;

    for (k = i; k <= n; k++) {
        solution += k;
    }
    
    return solution;
}

void psi(int x, int y) {
    int n;
    int p;
    int tmp;
    for (p = y; ; p--) {
        tmp = 0;
        for (n = 1; tmp < y; n++) {
            tmp = y - n * y + sum(1, n) * x;
        
            if (p + tmp == y) {
                printf("%d\n", p);
            }
            printf("%d\n", p);
        }
    }
}

int main() {
    psi(13, 1000);

    return 0;
}
