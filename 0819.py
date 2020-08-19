# python
# [LeetCode] week-3-august-18th
# Goat Latin
# @Jihyun22

# 문장을 입력받아 공백을 기준으로 list에 저장
S = list(map(str, input().split(' ')))

for i in range(0, len(S)):
    # 맨 앞 문자가 자음이면
    if S[i][0].lower() not in ['a', 'e', 'i', 'o', 'u']:
        # 앞 문자를 뒤로 add
        S[i] = S[i][1:] + S[i][0]
    # "ma" add
    # 'a'를 공백 수+1 만큼 add
    S[i] += "ma" + "a"*(i+1)

print(' '.join(S).strip(" "))


