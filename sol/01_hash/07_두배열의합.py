import sys
from collections import defaultdict


def solution(T, n, A, m, B):
    result = 0

    dict_A = defaultdict(int)  # A의 모든 부분합을 저장하는 딕셔너리
    dict_B = defaultdict(int)  # B의 모든 부분합을 저장하는 딕셔너리

    # n, m <= 1000 이므로 O(n^2)으로 해결 가능
    for i in range(n):
        sum_A = sum(A[i:])  # i번째 요소부터 끝까지의 합
        dict_A[sum_A] += 1

        for j in range(len(A) - 1, i, -1):
            sum_A -= A[j]  # 마지막 요소를 제거하면서 부분합 갱신
            dict_A[sum_A] += 1

    for i in range(m):
        sum_B = sum(B[i:])
        dict_B[sum_B] += 1

        for j in range(len(B) - 1, i, -1):
            sum_B -= B[j]
            dict_B[sum_B] += 1

    for key, value in dict_A.items():
        if (T - key) in dict_B:
            result += value * dict_B[T - key]

    return result


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input().rstrip())

    n = int(input().rstrip())
    A = list(map(int, input().split()))
    m = int(input().rstrip())
    B = list(map(int, input().split()))

    print(solution(T, n, A, m, B))
