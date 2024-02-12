#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int testcase;
	scanf("%d", &testcase);

	int num, divide1, divide2, tmp;
	for (int i = 0; i < testcase; i++) {
		unsigned long long int result = 1;

		scanf("%d %d", &divide1, &num);
		
		divide2 = num - divide1;
		if (divide1 < divide2) {
			tmp = divide1;
			divide1 = divide2;
			divide2 = tmp;
		}

		for (int j = divide1 + 1; j <= num; j++)	result *= j;
		for (int j = 1; j <= divide2; j++)			result /= j;

		printf("%lld\n", result);
	}
}