# python
# [LeetCode] week-3-august-17th
# Distribute Candies to People
# @Jihyun22

# 사탕 수와 사람 수가 각각 공백을 기준으로 입력되는 경우
c, p = list(map(int, input().split(" ")))
result = [0] * p

# candy_sum이 처음으로 10**9 이상일 때 i는 43
n = int(43/p)
candy = 1
candy_sum = 0
tmp = [[0] * p for _ in range(n+1)]
for i in range(n+1):
    for j in range(p):
        if candy_sum + candy > c:
            tmp[i][j] = c - candy_sum
            candy = -1
            result[j] += tmp[i][j]
            break
        tmp[i][j] = candy
        candy_sum += candy
        candy += 1
        result[j] += tmp[i][j]
    # 이중 for 문 종료
    if candy < 0:
        break

print(result)
