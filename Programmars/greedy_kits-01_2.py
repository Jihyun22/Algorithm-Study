# python
# 2020-09-07
# [programmars] 프로그래머스 탐욕법(Greedy) kit - 1
# @Jihyun22

def solution(n, lost, reserve):
    answer = 0
    # lost에만 있는 학생 번호
    lost_list = [l for l in lost if l not in reserve ]
    # reserve에만 있는 학생 번호
    reserve_list = [r for r in reserve if r not in lost ]
    # < reserve list > 탐색
    for r in reserve_list:
        # < lost list > 업데이트
        if r - 1 in lost_list:      lost_list.remove(r - 1)
        elif r + 1 in lost_list:    lost_list.remove(r + 1)
    # 체육 수업을 들을 수 있는 학생의 최댓값
    answer = n - len(lost_list)
    return answer