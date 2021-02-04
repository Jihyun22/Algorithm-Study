# 완전탐색
# 9개의 배열 입력받기
n = 9
numbers = list(map(int, input().split()))
answer = [0 for _ in range(7)]
result = sum(numbers)

for i in range(n-1):
    for j in range(i+1, n):
        if result - numbers[i] - numbers[j] == 100:
            numbers[i], numbers[j] = -1, -1
            break
j = 0
for i in range(n):
    if numbers[i] != -1:
        answer[j] = numbers[i]
        j += 1

print(' '.join(map(str, answer)))
