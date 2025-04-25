import sys
from math import gcd   

def solution(M, N, x, y):
    """
    <x:y> 해가 될 때까지 몇 년이 흘러야 하는가?
    아이디어: 먼저 x를 만족시키고, M 주기마다 y까지 만족되는지 확인
    """

    # 최소 공배수 -> 최대 공약수로 나누기
    lcm = M * N // gcd(M, N) 

    k = x # 총 년수
    while k <= lcm:
        if (k - y) % N == 0:  # y 만족하는지 확인
        # if k % N == y:  -> 반례: y == N 일때 
            return k
        k += M # 다음 M 주기 후

    return -1  # limit을 넘도록 못 찾으면 해가 없음

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        M, N, x, y = map(int, sys.stdin.readline().split())
        print(solution(M, N, x, y))

'''
- gcd(a, b) : a와 b의 “최대 공약수” → 나누기(약분) 때 사용
- lcm(a, b) : a와 b의 “최소 공배수” → 맞춰 늘리기(동기화) 때 사용
- 두 값은 곱해서 항상 a × b가 된다.
'''