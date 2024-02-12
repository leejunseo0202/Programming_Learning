#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int house[15][15] = { 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14 };
	int test_case, floor, number;

	for (floor = 1; floor < 15; floor++) {
		for (number = 1; number < 15; number++) {
			int member = 0;
			for (int i = 1; i <= number; i++)	
				member += house[floor-1][i];

			house[floor][number] = member;
		}
	}

	scanf("%d", &test_case);
	for (int i = 0; i < test_case; i++) {
		scanf("%d", &floor);
		scanf("%d", &number);

		printf("%d\n", house[floor][number]);
	}
}