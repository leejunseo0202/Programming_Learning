//array[i] = array[i-1]+array[i-2]+array[i-3] 을 이용하면 쉽게 풀 수 있음.
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int factorial(int num) {
	int result = 1;
	
	for (int i = 1; i <= num; i++)
		result *= i;

	return result;
}

int combination(int a, int b){
	int tmp = a;
	if (a < b) {
		a = b;
		b = tmp;
	}

	return factorial(a) / factorial(b) / factorial(a - b);
}

int main() {
	int n, num;					

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int count = 0;
		scanf("%d", &num);

		if (num > 0)		count++;				//use only 1
		if (num % 2 == 0)	count++;				//use only 2
		if (num % 3 == 0)	count++;				//use only 3
		
		for (int i = 1; i < num; i++)				//use 1 and 2
			if ((num - i) % 2 == 0)		count += combination((num - i) / 2 + i, i);		
		for (int i = 1; i < num; i++) 				//use 1 and 3
			if ((num - i) % 3 == 0)		count += combination((num - i) / 3 + i, i);
		for (int i = 2; i < num; i += 2) 			//use 2 and 3
			if ((num - i) % 3 == 0)		count += combination((num - i) / 3 + i / 2, i / 2);

		//use 1 and 2 and 3
		for (int one = 1; one <= num; one++) {
			for (int two = 2; one + two <= num; two += 2) {
				for (int three = 3; one + two + three <= num; three += 3) {
					if (one + two + three == num) 
						count += factorial(one + two / 2 + three / 3)
							/ factorial(one) / factorial(two / 2) / factorial(three / 3);
				}
			}		
		}
		printf("%d\n", count);
	}
}