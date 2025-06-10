import sys

MOD = 10**9 + 7  # 결과 출력시 나누는 수
MAX = 2501       # 최대 쌍 수는 5000 // 2 = 2500이므로

# DP 배열 선언 및 초기값
catalan = [0] * MAX
catalan[0] = 1             

# DP로 카탈란 수 채우기
for n in range(1, MAX):
    for i in range(n):
        catalan[n] += catalan[i] * catalan[n - 1 - i]
        catalan[n] %= MOD

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    if n % 2 != 0:
        print(0)             # 홀수면 올바른 괄호 불가능
    else:
        print(catalan[n // 2])  # 짝수면 쌍 개수 = n // 2
