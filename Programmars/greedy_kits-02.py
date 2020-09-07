# python
# 2020-09-07
# [programmars] 프로그래머스 탐욕법(Greedy) kit - 2
# @Jihyun22

def solution(number, k):
    answer = []
    # 문자열 리스트를 정수 리스트로 변환
    num = list(number)
    index = 0
    # len(answer) = len(num) - k
    for i in range(len(num)-k):
        if k+i == len(num):
            return ''.join(answer)+''.join(num[index:])
        # index ~ k+i+1까지 max값 탐색
        tmp = num[index:k+i+1]
        x = max(tmp)
        index = tmp.index(x) + index + 1
        answer += str(x)
    return ''.join(answer)