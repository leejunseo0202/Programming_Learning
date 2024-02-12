#define _CRT_SECURE_NO_WARNINGS
#define MAX(x,y) (x > y ? x : y)
#include <stdio.h>

int dp[501][501] = { 0 };

int main() {
	int n;

	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			scanf("%d", &dp[i][j]);
			dp[i][j] = MAX(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j];
		}
	}

	int max = 0;
	for (int j = 1; j <= n; j++)
		if (dp[n][j] > max)	max = dp[n][j];

	printf("%d\n", max);
}