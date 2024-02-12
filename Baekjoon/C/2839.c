#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int envelope_3 = 0, envelope_5 = 0, candy, value = 0, check_possibility = 0, leftover_candy = 0;

	scanf("%d", &candy);

	envelope_5 = candy / 5;
	leftover_candy = candy - envelope_5 * 5;

	if (leftover_candy == 0) {
		envelope_3 = 0;
		check_possibility = 1;
	}
	else if (leftover_candy % 3 == 0) {
		envelope_3 = 1;
		check_possibility = 1;
	}

	value = envelope_5;
	for (int i = 0; i < value; i++) {
		if (check_possibility)	break;

		envelope_5 -= 1;
		leftover_candy = candy - envelope_5 * 5;

		if (leftover_candy % 3 == 0) {
			envelope_3 = leftover_candy / 3;
			check_possibility = 1;
			break;
		}

	}
	
	if (!check_possibility)	printf("-1\n");
	else					printf("%d\n", envelope_3 + envelope_5);
}