// 주어진 9개의 숫자 중 7개의 숫자의 합이 100이 되는 수를 찾아내기
// 같은 숫자가 반복되는 경우는 없으며 답은 항상 유일함

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int numbers[]) {
	int* answer = (int*)malloc(sizeof(int) * 9);
	int sum = 0, i, j;
	for (i = 0; i < 9; i++)
		sum += numbers[i];
	for (i = 0; i < 8; i++) {
		for (j = i + 1; j < 9; j++) {
			if (sum - numbers[i] - numbers[j] == 100) {
				numbers[i] = -1;
				numbers[j] = -1;
				break;
			}
		}
	}
	j = 0;
	for (i = 0; i < 9; i++) {
		if (numbers[i] != -1) {
			answer[j++] = numbers[i];
		}
	}
	return answer;
}
void sort(int* ar) {
	int i, j, temp;
	for (i = 0; i < 6; i++) {
		for (j = i + 1; j < 7; j++) {
			if (ar[i] > ar[j]) {
				temp = ar[i];
				ar[i] = ar[j];
				ar[j] = temp;
			}
		}
	}
}

int main(void) {
	int numbers[9];
	for (int i = 0; i < 9; i++) {
		scanf("%d", &numbers[i]);
	}
	int* r = solution(numbers);
	for (int i = 0; i < 7; i++) {
		printf("%d ", r[i]);
	}
}