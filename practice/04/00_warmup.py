"""
4장 구현 — 워밍업 빈칸 문제

00_concept.md를 먼저 읽고 오세요.

규칙
  - 각 함수 안의 `TODO` 자리를 지우고 직접 코드를 채웁니다.
  - 다 채웠으면 터미널에서 실행하세요:
        python3 practice/04/00_warmup.py
"""

TODO = "아직 안 풀었음"


# ─────────────────────────────────────────────────────────────
# 1. 2차원 리스트 만들기
#    n행 m열이고 모든 칸이 0인 2차원 리스트를 돌려주세요.
#    make_board(2, 3) → [[0, 0, 0], [0, 0, 0]]
#    힌트: [[0] * m for _ in range(n)]
#          ※ [[0] * m] * n 은 함정입니다. 개념 노트 3번 참고.
# ─────────────────────────────────────────────────────────────
def make_board(n, m):
    return TODO


# ─────────────────────────────────────────────────────────────
# 2. 방향 벡터로 한 칸 이동
#    현재 위치 (x, y)에서 방향 문자 하나를 받아 이동한 좌표를 돌려주세요.
#    'U' 위(x-1) / 'D' 아래(x+1) / 'L' 왼쪽(y-1) / 'R' 오른쪽(y+1)
#    move(2, 2, 'U') → (1, 2)
#    move(2, 2, 'R') → (2, 3)
#    힌트: 아래 moves 딕셔너리를 그대로 쓰면 if문 없이 한 줄로 끝납니다.
#          moves['U'] 는 (-1, 0) 입니다.
# ─────────────────────────────────────────────────────────────
def move(x, y, d):
    moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    dx, dy = moves[d]
    return TODO


# ─────────────────────────────────────────────────────────────
# 3. 범위 체크
#    좌표 (x, y)가 n행 m열 판 안에 있으면 True, 벗어나면 False.
#    in_range(0, 0, 3, 3) → True
#    in_range(-1, 0, 3, 3) → False
#    in_range(1, 3, 3, 3) → False      (열 인덱스는 0~2까지)
#    힌트: 0 <= x < n  형태를 and 로 두 개 연결합니다.
# ─────────────────────────────────────────────────────────────
def in_range(x, y, n, m):
    return TODO


# ─────────────────────────────────────────────────────────────
# 4. 방향 회전
#    dx, dy 가 시계방향(북→동→남→서)으로 정렬돼 있을 때,
#    현재 방향 d에서 시계방향으로 한 번 돈 방향을 돌려주세요.
#    turn_right(0) → 1,  turn_right(3) → 0
#    힌트: % 4
# ─────────────────────────────────────────────────────────────
def turn_right(d):
    return TODO


# ─────────────────────────────────────────────────────────────
# 5. 반시계방향 회전
#    turn_left(0) → 3,  turn_left(2) → 1
#    힌트: 파이썬은 (0 - 1) % 4 를 3으로 계산해 줍니다.
# ─────────────────────────────────────────────────────────────
def turn_left(d):
    return TODO


# ─────────────────────────────────────────────────────────────
# 6. 숫자에 특정 숫자가 들어 있나 (완전 탐색 준비운동)
#    정수 num 안에 숫자 digit(0~9)이 하나라도 있으면 True.
#    has_digit(13, 3) → True
#    has_digit(25, 3) → False
#    has_digit(3, 3) → True
#    힌트: 숫자를 문자열로 바꾸고 in 을 씁니다. str(num), str(digit)
# ─────────────────────────────────────────────────────────────
def has_digit(num, digit):
    return TODO


# ─────────────────────────────────────────────────────────────
# 7. 체스판 좌표 변환
#    'a1' 같은 문자열을 (행, 열) 인덱스로 바꿔 주세요. 둘 다 0부터 시작합니다.
#    열 문자: a→0, b→1, ... h→7
#    행 숫자: '1'→0, '2'→1, ... '8'→7
#    to_index('a1') → (0, 0)
#    to_index('c2') → (1, 2)        행이 앞, 열이 뒤입니다
#    힌트: ord(s[0]) - ord('a') 로 열을, int(s[1]) - 1 로 행을 구합니다.
# ─────────────────────────────────────────────────────────────
def to_index(s):
    return TODO


# ─────────────────────────────────────────────────────────────
# 8. 완전 탐색 맛보기
#    0시 0분부터 (h)시 59분까지 중, 분(minute)이 5로 나누어떨어지는
#    시각이 몇 개인지 세어 주세요. h는 0 이상 23 이하.
#    count_times(0) → 12        (0시 0,5,10,...,55분 → 12개)
#    count_times(1) → 24        (0시 12개 + 1시 12개)
#    힌트: for hour in range(h + 1): 안에 for minute in range(60):
# ─────────────────────────────────────────────────────────────
def count_times(h):
    count = 0
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
    cases = [
        ("1. make_board(2, 3)", lambda: make_board(2, 3), [[0, 0, 0], [0, 0, 0]]),
        ("1. make_board(1, 1)", lambda: make_board(1, 1), [[0]]),
        ("2. move(2, 2, 'U')", lambda: move(2, 2, 'U'), (1, 2)),
        ("2. move(2, 2, 'R')", lambda: move(2, 2, 'R'), (2, 3)),
        ("2. move(0, 0, 'L')", lambda: move(0, 0, 'L'), (0, -1)),
        ("3. in_range(0, 0, 3, 3)", lambda: in_range(0, 0, 3, 3), True),
        ("3. in_range(-1, 0, 3, 3)", lambda: in_range(-1, 0, 3, 3), False),
        ("3. in_range(1, 3, 3, 3)", lambda: in_range(1, 3, 3, 3), False),
        ("3. in_range(2, 2, 3, 3)", lambda: in_range(2, 2, 3, 3), True),
        ("4. turn_right(0)", lambda: turn_right(0), 1),
        ("4. turn_right(3)", lambda: turn_right(3), 0),
        ("5. turn_left(0)", lambda: turn_left(0), 3),
        ("5. turn_left(2)", lambda: turn_left(2), 1),
        ("6. has_digit(13, 3)", lambda: has_digit(13, 3), True),
        ("6. has_digit(25, 3)", lambda: has_digit(25, 3), False),
        ("6. has_digit(3, 3)", lambda: has_digit(3, 3), True),
        ("7. to_index('a1')", lambda: to_index('a1'), (0, 0)),
        ("7. to_index('c2')", lambda: to_index('c2'), (1, 2)),
        ("7. to_index('h8')", lambda: to_index('h8'), (7, 7)),
        ("8. count_times(0)", lambda: count_times(0), 12),
        ("8. count_times(1)", lambda: count_times(1), 24),
        ("8. count_times(23)", lambda: count_times(23), 288),
    ]

    passed = 0
    print("\n4장 워밍업 채점\n" + "─" * 40)
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
        print("\n전부 통과! 이제 01_udlr.py 로 넘어가세요.\n")
    else:
        print()


if __name__ == "__main__":
    main()
