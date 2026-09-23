"""
5장 DFS/BFS — 워밍업 빈칸 문제

00_concept.md를 먼저 읽고 오세요.

규칙
  - 각 함수 안의 `TODO` 자리를 지우고 직접 코드를 채웁니다.
  - 다 채웠으면 터미널에서 실행하세요:
        python3 practice/05/00_warmup.py
"""

from collections import deque

TODO = "아직 안 풀었음"


# ─────────────────────────────────────────────────────────────
# 1. 스택 시뮬레이션
#    ops는 ('push', 값) 또는 ('pop',) 같은 명령 리스트입니다.
#    순서대로 실행한 뒤, 최종적으로 스택에 남은 값들을 리스트로 돌려주세요.
#    stack_result([('push',1),('push',2),('pop',),('push',3)]) → [1, 3]
#    힌트: 파이썬 리스트 자체가 스택입니다. append로 넣고 pop()으로 뺍니다.
# ─────────────────────────────────────────────────────────────
def stack_result(ops):
    stack = []
    return TODO


# ─────────────────────────────────────────────────────────────
# 2. 큐 시뮬레이션
#    1번과 명령은 같지만 이번엔 큐(deque)로 처리합니다.
#    queue_result([('push',1),('push',2),('pop',),('push',3)]) → [2, 3]
#    힌트: deque()를 만들고 append로 넣고 popleft()로 뺍니다.
#          마지막엔 list(큐)로 바꿔서 반환하세요.
# ─────────────────────────────────────────────────────────────
def queue_result(ops):
    q = deque()
    return TODO


# ─────────────────────────────────────────────────────────────
# 3. 재귀 — 팩토리얼
#    factorial(0) → 1     (종료 조건)
#    factorial(4) → 24    (4 * 3 * 2 * 1)
#    힌트: if n == 0: return 1 을 먼저 쓰고,
#          그 아래에 return n * factorial(n - 1)
# ─────────────────────────────────────────────────────────────
def factorial(n):
    return TODO


# ─────────────────────────────────────────────────────────────
# 4. 재귀 — 거꾸로 세기
#    n부터 1까지 거꾸로 센 숫자들을 리스트로 돌려주세요.
#    count_down(3) → [3, 2, 1]
#    count_down(0) → []
#    힌트: 종료 조건 if n == 0: return []
#          그 아래에 return [n] + count_down(n - 1)
# ─────────────────────────────────────────────────────────────
def count_down(n):
    return TODO


# ─────────────────────────────────────────────────────────────
# 5. 문자열 여러 줄 → 2차원 정수 리스트
#    rows는 ["001", "110"] 처럼 숫자로만 이루어진 문자열 리스트입니다.
#    각 문자열을 한 글자씩 정수로 바꿔서 2차원 리스트로 만들어 주세요.
#    build_grid(["001", "110"]) → [[0, 0, 1], [1, 1, 0]]
#    힌트: list(map(int, row)) 를 각 row마다 적용합니다.
# ─────────────────────────────────────────────────────────────
def build_grid(rows):
    return TODO


# ─────────────────────────────────────────────────────────────
# 6. 상하좌우 이웃 중 '땅(0)'의 개수 세기
#    graph는 2차원 리스트, 0은 땅, 1은 바다입니다.
#    (x, y)의 상하좌우 네 칸 중, 판 범위 안이면서 값이 0인 칸의 개수를 세어 주세요.
#    graph = [[0, 1], [0, 0]]
#    count_land_neighbors(graph, 0, 0) → 1   (아래 칸 (1,0)=0 만 해당)
#    count_land_neighbors(graph, 0, 1) → 2   (아래 (1,1)=0, 왼쪽 (0,0)=0)
#    힌트: 4장 워밍업의 in_range와 방향 벡터를 그대로 합치면 됩니다.
#          moves = [(-1,0),(1,0),(0,-1),(0,1)]
# ─────────────────────────────────────────────────────────────
def count_land_neighbors(graph, x, y):
    n, m = len(graph), len(graph[0])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    return TODO


# ─────────────────────────────────────────────────────────────
# 7. DFS — 연결된 땅 덩어리 크기 구하기
#    graph는 2차원 리스트, 0은 땅, 1은 바다입니다.
#    (x, y)에서 시작해 상하좌우로 연결된 땅(0)의 개수를 세어 주세요.
#    (이번 장 첫 문제 '음료수 얼려 먹기'와 똑같은 규칙입니다.)
#
#    g = [[0, 0, 1, 1],
#         [1, 0, 1, 0],
#         [1, 0, 0, 0],
#         [0, 0, 1, 1]]
#    flood_fill_count(g, 0, 0) → 9
#    flood_fill_count(g, 3, 0) → 9   (같은 덩어리라 시작점이 달라도 같은 값)
#
#    힌트: 내부에 재귀 함수 dfs(x, y)를 만들어 씁니다.
#      - 범위를 벗어나면 0을 반환
#      - 이미 방문했거나 바다(1)면 0을 반환
#      - 아니면 방문 처리하고, 1 + 네 방향 재귀 호출의 합을 반환
#    visited 같은 방문 기록판을 함수 안에서 새로 만들어 두고 써야
#    무한 재귀에 빠지지 않습니다. (개념 노트 3번 참고)
# ─────────────────────────────────────────────────────────────
def flood_fill_count(graph, x, y):
    n, m = len(graph), len(graph[0])
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y):
        return TODO

    return dfs(x, y)


# ─────────────────────────────────────────────────────────────
# 8. BFS — 최단 거리 구하기
#    graph는 2차원 리스트, 1은 이동 가능한 칸, 0은 벽입니다.
#    (이번 장 두 번째 문제 '미로 탈출'과 똑같은 규칙 — 0/1 의미가
#     7번과 반대라는 점에 주의하세요.)
#    (0, 0)에서 출발해 (n-1, m-1)까지 가는 최短 거리(시작 칸을 1로 세는 칸 수)를
#    구해 주세요. (0,0)과 (n-1,m-1)은 항상 이동 가능한 칸입니다.
#
#    g = [[1, 0, 1],
#         [1, 1, 1],
#         [0, 1, 1]]
#    bfs_shortest(g) → 5
#
#    힌트: 개념 노트 4번의 bfs 함수를 그대로 가져와 씁니다.
#      - dist 표를 만들어 dist[0][0] = 1 로 시작
#      - 큐에서 하나씩 꺼내 네 방향을 확인
#      - 갈 수 있는 새 칸이면 dist[nx][ny] = dist[x][y] + 1 로 기록하고 큐에 추가
#      - 다 끝나면 dist[n-1][m-1] 반환
# ─────────────────────────────────────────────────────────────
def bfs_shortest(graph):
    n, m = len(graph), len(graph[0])
    return TODO


# ═════════════════════════════════════════════════════════════
# 아래는 채점 코드입니다. 수정하지 마세요.
# ═════════════════════════════════════════════════════════════
def _check(name, got, want):
    if got == TODO:
        return False, f"  …  {name}: 아직 안 풀었음"
    if got == want:
        return True, f"  OK   {name}"
    return False, f"  틀림 {name}\n         기대: {want}\n         내 답: {got}"


def main():
    g6 = [[0, 1], [0, 0]]
    g7 = [
        [0, 0, 1, 1],
        [1, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 1],
    ]
    g8 = [
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1],
    ]
    g8b = [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
    ]

    cases = [
        ("1. stack_result(push1,push2,pop,push3)",
         lambda: stack_result([('push', 1), ('push', 2), ('pop',), ('push', 3)]), [1, 3]),
        ("1. stack_result(push5,push6,push7,pop)",
         lambda: stack_result([('push', 5), ('push', 6), ('push', 7), ('pop',)]), [5, 6]),
        ("2. queue_result(push1,push2,pop,push3)",
         lambda: queue_result([('push', 1), ('push', 2), ('pop',), ('push', 3)]), [2, 3]),
        ("2. queue_result(push5,push6,push7,pop)",
         lambda: queue_result([('push', 5), ('push', 6), ('push', 7), ('pop',)]), [6, 7]),
        ("3. factorial(0)", lambda: factorial(0), 1),
        ("3. factorial(4)", lambda: factorial(4), 24),
        ("4. count_down(3)", lambda: count_down(3), [3, 2, 1]),
        ("4. count_down(0)", lambda: count_down(0), []),
        ("5. build_grid(['001','110'])", lambda: build_grid(["001", "110"]), [[0, 0, 1], [1, 1, 0]]),
        ("5. build_grid(['0'])", lambda: build_grid(["0"]), [[0]]),
        ("6. count_land_neighbors g6 (0,0)", lambda: count_land_neighbors(g6, 0, 0), 1),
        ("6. count_land_neighbors g6 (0,1)", lambda: count_land_neighbors(g6, 0, 1), 2),
        ("7. flood_fill_count g7 (0,0)", lambda: flood_fill_count(g7, 0, 0), 9),
        ("7. flood_fill_count g7 (3,0)", lambda: flood_fill_count(g7, 3, 0), 9),
        ("8. bfs_shortest g8", lambda: bfs_shortest(g8), 5),
        ("8. bfs_shortest g8b", lambda: bfs_shortest(g8b), 6),
    ]

    passed = 0
    print("\n5장 워밍업 채점\n" + "─" * 40)
    for name, fn, want in cases:
        try:
            ok, msg = _check(name, fn(), want)
        except Exception as e:
            ok, msg = False, f"  에러 {name}: {type(e).__name__}: {e}"
        print(msg)
        passed += ok

    print("─" * 40)
    print(f"{passed} / {len(cases)} 통과")
    if passed == len(cases):
        print("\n전부 통과! 이제 10_ice_cream.py 로 넘어가세요.\n")
    else:
        print()


if __name__ == "__main__":
    main()
