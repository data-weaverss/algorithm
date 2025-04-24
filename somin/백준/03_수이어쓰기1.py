import sys

def solution(n):
    """
    1부터 n까지 이어서 쓴 숫자의 전체 자릿수를 반환한다.
    ex) n = 12  -> "123456789101112"  (총 15자리)  => 15
    """
    total = 0          # 누적 자릿수
    length = 1         # 현재 자릿수(1자리, 2자리, …)
    start = 1          # 이번 루프에서의 최솟값: 1, 10, 100, …

    while start * 10 <= n:
        # [start, start*10 - 1] : 모두 length 자리수이며 개수는 9 * start
        total += length * (9 * start)
        length += 1
        start *= 10     # 다음 자릿수 구간으로 이동

    # 마지막 구간: [start, n]
    total += length * (n - start + 1)
    return total

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solution(n))