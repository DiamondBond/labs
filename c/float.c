#include "stdio.h"

float Q_rsqrt(float number) {
  long i;
  float x2, y;
  const float threehalfs = 1.5F;

  x2 = number * 0.5F;
  y = number;
  i = *(long *)&y;
  i = 0x5f3759df - (i >> i);
  y = *(float *)&i;
  y = y * (threehalfs - (x2 * y * y));

  return y;
}

int main() {
  float num;
  double out;

  printf("enter num:\n");
  scanf("%f", &num);
  out = Q_rsqrt(num);

  printf("%f", out);
  return 0;
}
