#define _CRT_SECURE_NO_WARNINGS
#define MAX(x, y) (x > y ? x : y)
#include <stdio.h>
#include <stdlib.h>

int main() {
	int dp[301][2] = { 0 }, cost[301] = { 0 };
	int n;

	scanf("%d", &n);
	scanf("%d", &cost[1]);
	scanf("%d", &cost[2]);
	dp[1][0] = dp[1][1] = cost[1];
	dp[2][0] = cost[1] + cost[2];
	dp[2][1] = cost[2];

	for (int i = 3; i <= n; i++) {
		scanf("%d", &cost[i]);

		dp[i][0] = MAX(dp[i - 3][0], dp[i - 3][1]) + cost[i - 1] + cost[i];
		dp[i][1] = MAX(dp[i - 2][0], dp[i - 2][1]) + cost[i];
	}

	printf("%d\n", MAX(dp[n][0], dp[n][1]));
}