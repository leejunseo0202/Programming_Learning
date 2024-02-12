#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n, num;
	long long int triangle[101] = { 0, 1, 1, 1 };

	for (int i = 4; i <= 100; i++)
		triangle[i] = triangle[i - 3] + triangle[i - 2];

	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &num);
		printf("%lld\n", triangle[num]);
	}
}