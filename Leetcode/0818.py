# python
# [LeetCode] week-3-august-18th
# Numbers With Same Consecutive Differences
# @Jihyun22

# N과 K가 공백 기준으로 입력되는 경우
N, K = list(map(int, input().split(" ")))


def sol(N, K):
    # 0부터 9까지의 result에 저장
    result = range(10)
    # 자리수 만큼 반복
    # N=1이면 result = range(10) 반환
    for i in range(N - 1):
        result = {  # 자리수 고려
                    a * 10 + b
                    # result에 저장된 수 만큼 a연산 반복
                    for a in result
                    # a, b의 절대 차는 K
                    for b in [a % 10 + K, a % 10 - K]
                    # a에는 0이 올 수 없으며, b는 0~9 까지의 자연수
                    if a and 0 <= b < 10}
    return list(result)


print(sol(N, K))
