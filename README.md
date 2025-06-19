
import curses
import time
import pyttsx3
import threading
import queue

# TTS 초기화 및 설정
engine = pyttsx3.init()
speech_queue = queue.Queue()
tts_busy = threading.Event()

# 음성 출력 스레드
def speech_worker():
    while True:
        text = speech_queue.get()
        if text is None:
            break
        if not tts_busy.is_set():
            tts_busy.set()
            try:
                engine.say(text)
                engine.runAndWait()
            except Exception as e:
                print("TTS 오류:", e)
            tts_busy.clear()
        speech_queue.task_done()

# 음성 출력 함수
def speak(text):
    if not tts_busy.is_set():
        speech_queue.put(text)

# 음성 스레드 시작
speech_thread = threading.Thread(target=speech_worker, daemon=True)
speech_thread.start()

# 미로 데이터
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 목적지 목록
location = {
    "홈푸드마트": (7, 8),
    "롯데리아": (8, 7),
    "프랭크버거": (4, 5),
    "대구소프트웨어마이스터고": (4, 9),
    "준범이집": (8, 9),
    "민들레 식당": (1, 8)
}

for row in maze:
    print(row)

# 시작지점 및 도착지점 입력
start_x, start_y = map(int, input("시작지점 (x y): ").split())
end_name = input("도착지점 이름 입력: ")

if end_name not in location:
    print("❌ 도착지점이 목록에 없습니다.")
    exit()

end_x, end_y = location[end_name]
maze[end_x][end_y] = 2

# BFS를 이용한 최단 경로 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*10 for _ in range(10)]
parent = [[None]*10 for _ in range(10)]

queue_bfs = [(start_x, start_y)]
visited[start_x][start_y] = True
found = False

while queue_bfs:
    x, y = queue_bfs.pop(0)

    if maze[x][y] == 2:
        end_x, end_y = x, y
        found = True
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny] and maze[nx][ny] != 1:
            visited[nx][ny] = True
            parent[nx][ny] = (x, y)
            queue_bfs.append((nx, ny))

if found:
    x, y = end_x, end_y
    while True:
        if maze[x][y] == 0:
            maze[x][y] = 9
        if (x, y) == (start_x, start_y):
            break
        x, y = parent[x][y]

x, y = start_x, start_y

maze[x][y] = 7
maze_backup = [row[:] for row in maze]
already_warned = False

def clear_wrong_path():
    global already_warned
    cleared = False

    for i in range(10):
        for j in range(10):
            if maze[i][j] in (8, 7) and (i, j) != (x, y) and (i, j) != (start_x, start_y) and maze_backup[i][j] != 9:
                maze[i][j] = 0
                cleared = True

    if cleared and not already_warned:
        speak("잘못된 경로입니다. 되돌아가세요.")
        already_warned = True

    if not cleared:
        already_warned = False

def draw_maze(stdscr):
    stdscr.clear()
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 1:
                ch = '⬜️'
            elif val == 0:
                ch = ' '
            elif val == 2:
                ch = '💙'
            elif val == 9:
                ch = '🔘'
            elif val == 8:
                ch = '🟩'
            elif val == 7:
                ch = '🧑'
            else:
                ch = str(val)
            stdscr.addstr(i, j * 2, ch)
    stdscr.refresh()

def main(stdscr):
    global x, y
    curses.curs_set(0)
    stdscr.nodelay(True)
    draw_maze(stdscr)

    directions = {
        'w': (-1, 0),
        's': (1, 0),
        'a': (0, -1),
        'd': (0, 1)
    }

    while True:
        key = stdscr.getch()
        if key == -1:
            time.sleep(0.05)
            continue

        try:
            char = chr(key).lower()
        except:
            continue

        if char in directions:
            dx, dy = directions[char]
            nx, ny = x + dx, y + dy

            if 0 <= nx < 10 and 0 <= ny < 10 and maze[nx][ny] != 1:
                maze[x][y] = 8
                x, y = nx, ny

                if maze[x][y] == 2:
                    maze[x][y] = 7
                    draw_maze(stdscr)
                    stdscr.addstr(11, 0, "🎉 도착했습니다! 프로그램을 종료합니다.")
                    speak("도착했습니다. 안내를 종료합니다.")
                    stdscr.nodelay(False)
                    stdscr.getch()
                    break

                maze[x][y] = 7
                clear_wrong_path()
                draw_maze(stdscr)

        elif char == 'q':
            break

curses.wrapper(main)
speech_queue.put(None)
speech_thread.join()

<!--
**Divanzo/Divanzo** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
