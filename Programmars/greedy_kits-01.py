# python
# 2020-09-07
# [programmars] 프로그래머스 탐욕법(Greedy) kit - 1
# @Jihyun22

def solution(n, lost, reserve):
    # 초기화
    answer = 0
    student = [1 for i in range (n)]
    # lost 인 학생의 체육복 수를 -1, reserve인 학생의 체육복 수를 +1
    for i in range(len(student)):
        if i+1 in lost:
            student[i] -= 1
        if i+1 in reserve:
            student[i] += 1
    # 선행
    for i in range(len(student)-1):
        if student[i] < 1:
            if student[i+1] > 1:
                student[i] +=1
                student[i+1] -=1
    # 후행    
    for i in range(len(student)-1):
        if student[len(student)-i-1] < 1:
            if student[len(student)-i-2] > 1:
                student[len(student)-i-1] +=1
                student[len(student)-i-2] -=1
    # 수업을 들을 수 있는 학생 수
    for a in student:
        if a > 0: answer +=1
    # 출력
    return answer