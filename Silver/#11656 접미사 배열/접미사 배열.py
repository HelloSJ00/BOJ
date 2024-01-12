#접미사 배열

import sys
input = sys.stdin.readline

_string = input().rstrip()

result = []
for i in range(len(_string)):
    result.append(_string[i:])

result = sorted(result)
for i in range(len(result)):
    print(result[i])