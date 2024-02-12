#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int method[1001] = { 0, 1, 2 }, num;

	for (int i = 3; i <= 1000; i++)
		method[i] = (method[i - 1] + method[i - 2]) % 10007;
	
	scanf("%d", &num);
	printf("%d\n", method[num]);

}