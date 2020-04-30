#include <stdio.h>

const char* F = "Fizz";
const char* B = "Buzz";

void fizzbuzz(int s, int f) {
    for (int i = s; i <= f; ++i) {
	if (i % 15 == 0) {
	    printf("%s", F);
	    printf("%s", B);
	} else if (i % 3 == 0) {
	    printf("%s", F);
	} else if (i % 5 == 0) {
	    printf("%s", B);
	} else {
	    printf("%d", i);
	}
	printf("\n");
    }
}

int main(int argc, char** argv) {
    if (argc < 3) {
	printf("Usage: a.out [start] [finish]\n");
    } else {
	int s, f;
	sscanf(argv[1], "%d", &s);
	sscanf(argv[2], "%d", &f);
	fizzbuzz(s, f);
    }
    return 0;
}
