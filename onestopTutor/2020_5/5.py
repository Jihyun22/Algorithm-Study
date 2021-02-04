# 문자열을 압축하는 방법
# 2진수 입력 가정 -> str 형식으로 받아오기
# 동일한 문자가 1~26회까지 입력될 수 있음
# 첫 문자가 0인 경우 숫자 생략하여 연속 입력 수 대응하여 알파벳으로 표시
# 단, 첫 문자가 1인 경우 표시할 것

import sys
import string
string.ascii_uppercase
# 알파벳 대문자 사용할 것

data = sys.stdin.readline().rstrip()
print(data)
