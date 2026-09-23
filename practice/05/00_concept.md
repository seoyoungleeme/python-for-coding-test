# 5장 DFS/BFS — 개념 노트

## 1. 왜 필요한가

4장에서 격자를 한 칸씩 돌아다니는 법을 배웠다. 5장은 거기서 한 걸음 더 나간다:
**"연결된 칸들을 전부 찾아라"**, **"가장 가까운 길을 찾아라"** — 이 두 가지 질문에
답하는 도구가 DFS와 BFS다.

핵심 자료구조는 **그래프**다. 노드(정점)들이 있고, 노드끼리 간선(edge)으로 연결돼
있다. 격자 문제에서는 **칸 하나가 노드**, **상하좌우로 붙어 있으면 간선**이라고
생각하면 된다.

## 2. 스택과 큐 — 둘의 차이가 DFS/BFS의 차이다

DFS와 BFS는 알고리즘 자체보다 **"다음에 어디를 방문할지 어떻게 관리하는가"**가
다르다. 그 관리 방법이 스택이냐 큐냐로 갈린다.

### 스택 (Stack) — 나중에 넣은 걸 먼저 꺼낸다 (LIFO)

```python
stack = []
stack.append(1)      # [1]
stack.append(2)      # [1, 2]
stack.append(3)      # [1, 2, 3]
stack.pop()           # 3  ← 가장 최근에 넣은 것부터 나온다
```

파이썬은 리스트가 스택 역할을 그대로 한다. `append`로 넣고 `pop()`으로 꺼내면 끝.

### 큐 (Queue) — 먼저 넣은 걸 먼저 꺼낸다 (FIFO)

```python
from collections import deque
queue = deque()
queue.append(1)        # [1]
queue.append(2)        # [1, 2]
queue.append(3)        # [1, 2, 3]
queue.popleft()         # 1  ← 가장 먼저 넣은 것부터 나온다
```

**왜 `list.pop(0)`이 아니라 `deque`인가:** 리스트 맨 앞을 꺼내는 건 뒤에 있는 원소를
전부 한 칸씩 당겨야 해서 느리다(N이 크면 매우 느려짐). `deque`는 양쪽 끝 모두
빠르게 넣고 뺄 수 있도록 설계된 자료구조다. **BFS에서는 항상 `deque`를 쓴다.**

## 3. DFS (깊이 우선 탐색) — 갈 수 있는 데까지 가본다

"한 방향으로 끝까지 가보고, 막히면 되돌아와서 다른 방향을 시도한다." 미로에서 한
손을 벽에 대고 계속 따라가는 것과 비슷하다.

파이썬에서는 **재귀 함수**로 짜는 게 가장 자연스럽다 — 함수가 자기 자신을 부르는
것 자체가 "이 칸에서 갈 수 있는 다음 칸으로 파고드는" 동작과 맞아떨어진다.

```python
def dfs(x, y):
    # 범위를 벗어나면 멈춘다
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    # 이미 방문했거나 갈 수 없는 칸이면 멈춘다
    if visited[x][y] or graph[x][y] == 1:
        return

    visited[x][y] = True     # 방문 처리 (매우 중요 — 없으면 무한 재귀)

    # 네 방향으로 계속 파고들기
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
```

**방문 처리를 빼먹으면 무한 재귀에 빠진다.** (0,0)에서 (0,1)로 갔다가 다시 (0,0)으로
되돌아오는 걸 막아주는 게 `visited` 체크이기 때문이다. 4장에서 무한루프를 겪어봤으니
왜 위험한지는 이미 몸으로 알고 있을 것이다.

## 4. BFS (너비 우선 탐색) — 가까운 곳부터 순서대로 퍼진다

"현재 위치에서 한 칸 거리에 있는 곳을 모두 확인하고, 그다음 두 칸 거리, 그다음
세 칸..." 물에 돌을 던졌을 때 파문이 동심원으로 퍼지는 것과 같다.

**재귀가 아니라 큐로 짠다.**

```python
from collections import deque

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()          # 가장 먼저 들어온 칸부터 처리
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True   # 큐에 넣을 때 바로 방문 처리
                queue.append((nx, ny))
```

**BFS는 "최단 거리"를 구할 때 쓴다.** 모든 간선의 길이가 1(한 칸 이동)로 같을 때,
먼저 도달한 경로가 항상 가장 짧은 경로이기 때문이다. DFS로도 도달은 하지만,
어느 경로로 먼저 도착할지 보장이 없어서 최단 거리를 구하는 데는 안 맞는다.

## 5. 언제 DFS, 언제 BFS

| 질문 | 방법 |
|---|---|
| "연결된 덩어리가 몇 개인가?" / "이 두 칸이 연결돼 있나?" | DFS (또는 BFS, 결과는 같음) |
| "최단 거리는 몇인가?" | **반드시 BFS** |

이번 장 두 문제가 정확히 이 구분을 보여준다:

- **음료수 얼려 먹기**: "연결된 덩어리 개수" → DFS
- **미로 탈출**: "최단 거리" → BFS

## 6. 이 장에서 쓰는 파이썬 문법

### 재귀 함수

```python
def countdown(n):
    if n == 0:              # 종료 조건 (없으면 무한 재귀)
        print("발사!")
        return
    print(n)
    countdown(n - 1)         # 자기 자신을 다시 부름
```

**종료 조건을 반드시 먼저 쓴다.** 4장의 `while` 무한루프와 마찬가지로, 재귀도
멈추는 조건이 없으면 끝없이 자기 자신을 부르다가 터진다
(`RecursionError: maximum recursion depth exceeded`).

### 문자열을 한 글자씩 숫자로 바꿔 2차원 리스트 만들기

이 장의 입력은 `"00110"`처럼 붙어 있는 숫자 문자열이다. 4장에서 다룬 네 가지
조합 중 이번엔 이 형태를 쓴다:

```python
row = list(map(int, input()))   # "00110" → [0, 0, 1, 1, 0]

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
```

### deque

```python
from collections import deque

q = deque()          # 빈 큐
q = deque([1, 2, 3])  # 리스트로 초기화
q.append(4)           # 오른쪽에 추가
q.popleft()           # 왼쪽에서 꺼내기 (이게 리스트와 다른 점)
```

## 7. 다음 단계

`00_warmup.py`를 채워 보자.

```
python3 practice/05/00_warmup.py
```

전부 통과하면 첫 문제(`10_ice_cream.py`)로 넘어간다.
