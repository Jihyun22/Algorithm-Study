# python
# 2020-09-07
# [programmars] 프로그래머스 탐욕법(Greedy) kit - 2
# @Jihyun22

def solution(number, k):
    answer = []
    for num in number:
        # answer[-1] : answer의 마지막 요소
        while answer and answer[-1] < num and k > 0:
            k -= 1
            answer.pop()
        answer.append(num)
    if k != 0:
        # answer에서 k개의 요소를 뒤에서부터 삭제
        answer = answer[:-k]
    return ''.join(answer)