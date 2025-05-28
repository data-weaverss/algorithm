import sys

def solution(N: int, street: str) -> int:
    """
    0 → N-1 까지 BOJ 순서로 이동할 때의 최소 에너지를 구하시오.
    - 에너지 양: k칸 이동 시 에너지 = k*k
    - 마지막 보도블록에 도착할 수 없을 시 -1 출력
    """
    dp = [float('inf')] * N
    dp[0] = 0
    next_block = {'B':'O',
                  'O':'J',
                  'J':'B'}

    for i in range(N-1):
        if dp[i] == float('inf'):
            continue
        for j in range(i+1, N):
            if street[j] != next_block[street[i]]:
                continue
            energy = dp[i] + (j - i) ** 2
            if energy < dp[j]:
                dp[j] = energy

    return dp[N-1] if dp[N-1] != float('inf') else -1

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    street = sys.stdin.readline().strip()

    print(solution(N, street))
