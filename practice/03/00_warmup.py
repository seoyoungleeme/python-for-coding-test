"""
3장 그리디 — 워밍업 빈칸 문제

00_concept.md를 먼저 읽고 오세요.

규칙
  - 각 함수 안의 `TODO` 자리를 지우고 직접 코드를 채웁니다.
  - 다 채웠으면 터미널에서 실행하세요:
        python3 practice/03/00_warmup.py
  - 통과한 문제는 OK, 틀린 문제는 기대값과 내 답이 같이 출력됩니다.
"""

TODO = "아직 안 풀었음"


# ─────────────────────────────────────────────────────────────
# 1. 입력 파싱
#    "5 8 3" 같은 문자열을 받아 정수 3개를 담은 튜플 (5, 8, 3)로 돌려주세요.
#    힌트: text.split() 은 ["5", "8", "3"] 을 만듭니다. 여기에 map(int, ...) 를 씌우고
#          tuple(...) 로 감싸면 됩니다.
# ─────────────────────────────────────────────────────────────
def parse_three(text):
    return tuple(map(int, text.split()))


# ─────────────────────────────────────────────────────────────
# 2. 가장 큰 수와 두 번째로 큰 수
#    정수 리스트를 받아 (가장 큰 수, 두 번째로 큰 수) 를 돌려주세요.
#    중복은 서로 다른 값으로 취급합니다. [3, 4, 3, 4, 3] → (4, 4)
#    힌트: 정렬한 뒤 뒤에서 두 개를 꺼냅니다. data[-1], data[-2]
# ─────────────────────────────────────────────────────────────
def top_two(data):
    data.sort()
    return data[-1], data[-2]

# ─────────────────────────────────────────────────────────────
# 3. 몫과 나머지
#    사탕 total개를 한 사람에게 per개씩 나눠줄 때
#    (나눠줄 수 있는 사람 수, 남는 사탕 수) 를 돌려주세요.
#    candy_split(17, 5) → (3, 2)
#    힌트: // 와 %
# ─────────────────────────────────────────────────────────────
def candy_split(total, per):
    return total//per, total%per


# ─────────────────────────────────────────────────────────────
# 4. 거스름돈 그리디
#    500, 100, 50, 10원 동전이 무한히 있을 때
#    money원을 거슬러 주는 데 필요한 최소 동전 개수를 돌려주세요.
#    money는 항상 10의 배수입니다. coin_count(1260) → 6
#    힌트: 큰 동전부터 차례로 for 문을 돌면서
#          "이 동전을 몇 개 쓸 수 있는지"를 // 로 세고,
#          남은 돈은 % 로 갱신합니다.
# ─────────────────────────────────────────────────────────────
def coin_count(money):
    coins = [500, 100, 50, 10]
    count = 0
    for coin in coins:
        count += money // coin
        money = money % coin
    return count


# ─────────────────────────────────────────────────────────────
# 5. 그리디가 틀리는 경우
#    동전이 500, 400, 100원일 때 800원을 거슬러 준다고 합시다.
#    아래 두 값을 직접 숫자로 채우세요. (코드 말고 숫자만)
#      greedy_answer : 큰 동전부터 욕심껏 고르는 방식이 내놓는 동전 개수
#      best_answer   : 실제 최소 동전 개수
# ─────────────────────────────────────────────────────────────
greedy_answer = 4
best_answer = 2


# ─────────────────────────────────────────────────────────────
# 6. 반복문 감각
#    n이 1이 될 때까지, n을 1씩 빼는 연산을 몇 번 해야 하는지 돌려주세요.
#    steps_to_one(5) → 4
#    힌트: while n > 1: 안에서 n을 줄이고 횟수를 셉니다.
# ─────────────────────────────────────────────────────────────
def steps_to_one(n):
    count = 0
    while n > 1:
        n -= 1
        count += 1
    return count


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
        ("1. parse_three('5 8 3')", lambda: parse_three("5 8 3"), (5, 8, 3)),
        ("1. parse_three('10 2 7')", lambda: parse_three("10 2 7"), (10, 2, 7)),
        ("2. top_two([2,4,5,4,6])", lambda: top_two([2, 4, 5, 4, 6]), (6, 5)),
        ("2. top_two([3,4,3,4,3])", lambda: top_two([3, 4, 3, 4, 3]), (4, 4)),
        ("3. candy_split(17, 5)", lambda: candy_split(17, 5), (3, 2)),
        ("3. candy_split(8, 3)", lambda: candy_split(8, 3), (2, 2)),
        ("4. coin_count(1260)", lambda: coin_count(1260), 6),
        ("4. coin_count(4720)", lambda: coin_count(4720), 13),
        ("5. greedy_answer", lambda: greedy_answer, 4),
        ("5. best_answer", lambda: best_answer, 2),
        ("6. steps_to_one(5)", lambda: steps_to_one(5), 4),
        ("6. steps_to_one(1)", lambda: steps_to_one(1), 0),
    ]

    passed = 0
    print("\n3장 워밍업 채점\n" + "─" * 40)
    for name, fn, want in cases:
        try:
            got = fn()
            ok, msg = _check(name, got, want)
        except Exception as e:
            ok, msg = False, f"  에러 {name}: {type(e).__name__}: {e}"
        print(msg)
        passed += ok

    print("─" * 40)
    print(f"{passed} / {len(cases)} 통과")
    if passed == len(cases):
        print("\n전부 통과! 이제 02_big_number.py 로 넘어가세요.\n")
    else:
        print()


if __name__ == "__main__":
    main()
