def breakingSquare(plane, start_col, end_col, start_row, end_row):
    global blue, white

    # 종료 조건: 하나의 셀만 남았을 때
    if start_col == end_col and start_row == end_row:
        if plane[start_row][start_col] == 1:
            blue += 1
            return 'blue'
        else:
            white += 1
            return 'white'

    mid_col = (start_col + end_col) // 2
    mid_row = (start_row + end_row) // 2

    # 분할 정복
    colors = [
        breakingSquare(plane, start_col, mid_col, start_row, mid_row),
        breakingSquare(plane, mid_col + 1, end_col, start_row, mid_row),
        breakingSquare(plane, start_col, mid_col, mid_row + 1, end_row),
        breakingSquare(plane, mid_col + 1, end_col, mid_row + 1, end_row)
    ]

    # 모든 영역이 동일한 색인지 확인
    if all(color == 'blue' for color in colors):
        blue -= 3  # 중복 카운팅 제거
        return 'blue'
    elif all(color == 'white' for color in colors):
        white -= 3  # 중복 카운팅 제거
        return 'white'
    else:
        # 혼합된 경우, 이미 카운팅되었으므로 추가 처리 불필요
        return 'mixed'

import sys
input = sys.stdin.readline
N = int(input())

    # 입력 데이터 (예시)
monun = []
for i in range(N):
    monun.append(list(map(int,input().split())))

# 결과 변수 초기화
blue = 0
white = 0

# 함수 실행
breakingSquare(monun, 0, N-1, 0, N-1)

# 결과 출력
print(white)
print(blue)
