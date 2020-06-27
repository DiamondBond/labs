#include <math.h>
#include <stdio.h>

#define PI 3.14159265358979323846

int pi() {
	int r[2800 + 1];
	int i, k;
	int b, d;
	int c = 0;

	for (i = 0; i < 2800; i++) {
		r[i] = 2000;
	}

	for (k = 2800; k > 0; k -= 14) {
		d = 0;

		i = k;
		for (;;) {
			d += r[i] * 10000;
			b = 2 * i - 1;

			r[i] = d % b;
			d /= b;
			i--;
			if (i == 0) break;
			d *= i;
		}
		printf("%.4d", c + d / 10000);
		c = d % 10000;
	}
	return 0;
}

int main(void){
    float ax, ay, az, bx, by, bz, azu, ele, ka, ke;

    printf("? ");
    scanf("%f %f %f %f %f %f", &ax, &ay, &az, &bx, &by, &bz);

    ka = atan2(bx - ax, by - ay);
    printf("Azimuth K = %f\n", ka);

    if (ka < 0){
	printf("Adding 2Pi to K...\n");
	ka = ka + (2 * PI);
    }

    azu = ka * (180 / PI);
    printf("Azimuth = %f\n\n", azu);

    ke = sqrt(((bx - ax) * (bx - ax)) + ((by - ay) * (by - ay)));
    printf("Elevation K = %f\n", ke);

    ele = atan((bz - az) / ke) * 180 / PI;
    printf("Elevation = %f\n", ele);

    return 0;
}
