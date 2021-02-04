# 완전탐색
# 9개의 배열 입력받기
n = 9
numbers = list(map(int, input().split()))
answer = list()
result = sum(numbers)

for i in range(n-1):
    for j in range(i+1, n):
        if result - numbers[i] - numbers[j] == 100:
            numbers[i], numbers[j] = -1, -1
            break
print(len(answer))