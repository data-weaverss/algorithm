import sys

def solution(S, P):
    """P가 S의 부분 문자열이면 1, 아니면 0을 출력한다."""
    if P in S:
        return 1
    return 0

if __name__ == "__main__":
    S = sys.stdin.readline().strip()
    P = sys.stdin.readline().strip()

    print(solution(S, P))