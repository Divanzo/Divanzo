# import math

# lst=list(range(1,11))
# print(lst)
# mean=sum(lst)/len(lst)

# #통계
# print("통계:",mean)

# #분산
# vsum=0

# for x in lst:
#     vsum+=(x-mean)**2
# var=vsum/len(lst)

# print("분산:",var)

# #표준편차
# std=math.sqrt(var)
# print(f"표준편차: {std:.2f}")

# #최소공약수
# gcd=math.gcd(*lst)
# lcm=math.lcm(*lst)

# print("최소공약수:",gcd,end=" ")
# print("최소공배수:",lcm)

import curses
import time

maze = [list(map(int, input().split())) for _ in range(10)] # 구지 지도 저장소

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작 위치
start_x, start_y = 1, 1

# 방문 여부 및 부모 좌표 저장
visited = [[False] * 10 for _ in range(10)]
parent = [[None] * 10 for _ in range(10)]

# 리스트로 큐 구현
queue = []
queue.append((start_x, start_y))
visited[start_x][start_y] = True

found = False
end_x, end_y = -1, -1

while queue:
    x, y = queue[0]
    queue.pop(0)

    if maze[x][y] == 2:
        end_x, end_y = x, y
        found = True
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 10 and 0 <= ny < 10:
            if not visited[nx][ny] and maze[nx][ny] != 1:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))

# 경로 추적 및 9로 표시
if found==True:
    x, y = end_x, end_y
    while True:
        # 먹이 위치도 9로 바꾸기 (경로 표시를 위해)
        if maze[x][y] == 0 or maze[x][y] == 2:
            maze[x][y] = 9
        
        # 시작점 도달 시 종료
        if (x, y) == (start_x, start_y):
            print('도착')
            break
        
        x, y = parent[x][y]

# 결과 출력
print('===== 9로 표신된 경로 =====')
for row in maze:
    print(*row)

# 방향 설정: W, A, S, D
directions = {
    'w': (-1, 0),
    's': (1, 0),
    'a': (0, -1),
    'd': (0, 1)
}

# 시작 위치
x, y = 1, 1
maze[x][y] = 8

def draw_maze(stdscr):
    stdscr.clear()  # 매번 그리기 전 화면 초기화
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 1:
                ch = '#'
            elif val == 0:
                ch = ' '
            elif val == 2:
                ch = 'G'
            elif val == 8:
                ch = '8'
            elif val == 9:
                ch = '@'
            else:
                ch = str(val)
            stdscr.addstr(i, j * 2, ch)
    stdscr.refresh()  # 반드시 새로 출력 내용 반영

def main(stdscr):
    global x, y
    curses.curs_set(0)          # 커서 숨기기
    stdscr.nodelay(True)        # 입력 없을 때도 루프 계속
    stdscr.keypad(True)         # 방향키, 특수키 허용
    draw_maze(stdscr)

    while True:
        key = stdscr.getch()

        if key == -1:
            time.sleep(0.05)
            continue

        try:
            char = chr(key).lower()
        except ValueError:
            continue  # 특수키는 무시

        if char in directions:
            dx, dy = directions[char]
            nx, ny = x + dx, y + dy

            if 0 <= nx < 10 and 0 <= ny < 10:
                if maze[nx][ny] != 1:
                    maze[x][y] = 9  # 지나간 자리를 9로
                    x, y = nx, ny
                    if maze[x][y] == 2:
                        maze[x][y] = 8
                        draw_maze(stdscr)
                        stdscr.addstr(11, 0, "도착했습니다! 아무 키나 누르세요.")
                        stdscr.nodelay(False)
                        stdscr.getch()
                        break
                    maze[x][y] = 8
            draw_maze(stdscr)

        elif char == 'q':
            break

curses.wrapper(main)