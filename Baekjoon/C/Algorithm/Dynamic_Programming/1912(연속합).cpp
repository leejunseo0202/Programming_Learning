#define _CRT_SECURE_NO_WARNINGS
#define MAX(x,y) (x > y ? x : y)
#include <stdio.h>

int main() {
	int n, dp[100000] = { 0 };

	scanf("%d", &n);
	scanf("%d", &dp[0]);
	
	int max = dp[0];
	for (int i = 1; i < n; i++) {
		scanf("%d", &dp[i]);

		dp[i] = MAX(dp[i - 1] + dp[i], dp[i]);
		if (dp[i] > max)	max = dp[i];
	}
	printf("%d\n", max);
}