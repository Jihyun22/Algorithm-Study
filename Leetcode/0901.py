# python
# [LeetCode] week-1-september-1th
# Array Nesting
# @Jihyun22

# nums 배열 입력
nums = list(map(int, input().split(' ')))
# 방문 요소를 마킹하는 배열 visit
visit = [0 for _ in range(len(nums))]
answer = 0

for i, j in enumerate(nums): # nums 배열을 순서대로 탐색
    if visit[i] == 0: # 방문하지 않은 요소라면,
        start = j # 해당 요소에서 방문 시작
        count = 0 # 변수 초기화
        while j != nums[start]: # 무한 루프를 방지하기 위한 조건
            start = nums[start] # 시작 요소 변경
            count += 1 
            visit[start] = 1 # 해당 요소 방문 표시
            answer = max(answer, count) # count 의 최대값만을 answer 에 반영

print(answer +1) # s[k] 의 최소값은 1 이므로
