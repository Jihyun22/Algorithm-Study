# python3
# 2020-09-07
# [이것이코딩테스트다] ch03-그리디
# 2. 큰 수의 법칙
# @Jihyun22

n, m, k = map(int, input().split())
_list = list(map(int, input().split()))
answer = 0

_list.sort()
a = _list[n-1]
b = _list[n-2]
n = k*m/(k+1) + m % (k+1)

answer += a*n
answer += b*(m-n)

print(int(answer))
