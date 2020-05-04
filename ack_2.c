#include <stdio.h>
 
int ack(int m, int n){
        if (!m) return n + 1;
        if (!n) return ack(m - 1, 1);
        return ack(m - 1, ack(m, n - 1));
}
 
int main(){
        int m, n;
        for (m = 0; m <= 4; m++)
                for (n = 0; n < 6 - m; n++)
                        printf("A(%d, %d) = %d\n", m, n, ack(m, n));
        return 0;
}