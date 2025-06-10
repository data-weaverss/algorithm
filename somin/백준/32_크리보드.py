import sys

def solution(n):
    # dp[i]: i번 키를 눌렀을 때 화면에 출력할 수 있는 최대 A 개수
    # 초기값 설정: i번 모두 'A'를 직접 눌러서 출력하는 경우
    dp = [i for i in range(n + 1)]

    # i: 복사할 시점을 결정 (최소 Ctrl+A, Ctrl+C, Ctrl+V 세 번 필요 → i는 최소 3부터)
    for i in range(3, n - 2):
        # j: 복사 이후 붙여넣기를 몇 번 할 것인지 결정
        for j in range(i + 3, n + 1):
            # dp[i]를 (j - i - 1)번 붙여넣기 했을 때 최대값 갱신
            dp[j] = max(dp[j], dp[i] * (j - i - 1))
    
    return dp[n]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solution(n))