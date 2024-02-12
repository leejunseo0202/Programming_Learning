#define _CRT_SECURE_NO_WARNINGS
#define MIN(x,y) (x < y ? x : y)
#include <stdio.h>
#include <stdlib.h>

int main() {
	int house;
	int** weight;
	int** dp;

	scanf("%d", &house);
	weight = (int**)malloc(sizeof(int*) * house);
	dp	   = (int**)malloc(sizeof(int*) * house);
	for (int i = 0; i < house; i++) {
		weight[i] = (int*)malloc(sizeof(int) * 3);
		dp[i]	  = (int*)malloc(sizeof(int) * 3);
		scanf("%d %d %d", &weight[i][0], &weight[i][1], &weight[i][2]);
	}
	
	dp[0][0] = weight[0][0];
	dp[0][1] = weight[0][1];
	dp[0][2] = weight[0][2];

	for (int i = 1; i < house; i++) {
		dp[i][0] = MIN(dp[i - 1][1], dp[i - 1][2]) + weight[i][0];
		dp[i][1] = MIN(dp[i - 1][0], dp[i - 1][2]) + weight[i][1];
		dp[i][2] = MIN(dp[i - 1][0], dp[i - 1][1]) + weight[i][2];
	}

	int min = MIN(MIN(dp[house - 1][0], dp[house - 1][1]), MIN(dp[house - 1][1], dp[house - 1][2]));
	printf("%d\n", min);
}