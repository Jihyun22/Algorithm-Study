# python3
# [LeetCode] week-3-august-16th
# @Jihyun22
# input -> 괄호 제거, ','기준으로 int값 분할하여 stock이름의 list 생성

stock = list(map(int, input().strip('[]').split(',')))


def maxProfit(stock):
    day = len(stock)
    # 입력값이 2개 미만이면 0 return
    if day < 2:
        return 0
    # 양 끝값에서 중앙으로 탐색
    left, right = stock[0], stock[day-1]
    # 최대 트렌젝션은 2번 일어나므로 각각 이익 저장할 배열 선언
    tmp1, tmp2 = [0]*day, [0]*day
    for i in range(1, day):
        # 왼쪽 -> 오른쪽 순으로 S_min 연산
        tmp1[i] = max(tmp1[i-1], stock[i]-left)
        left = min(left, stock[i])
        # 오른쪽 -> 왼쪽 순으로 S_max 연산
        j = day-1-i
        tmp2[j] = max(tmp2[j+1], right-stock[j])
        right = max(right, stock[j])
        # 이익은 음수가 될 수 없으므로 초기값은 0
        result = 0
    # 각각의 tmp에서 i번째 수의 합은 이익의 경우의 수
    for i in range(day):
        # 이익의 최대값 연산
        result = max(result, tmp1[i]+tmp2[i])
    return result


print(maxProfit(stock))
