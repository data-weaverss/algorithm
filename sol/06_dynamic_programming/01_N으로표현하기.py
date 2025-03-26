from collections import defaultdict

"""
- case1: 5
- case2: 55, 5 + 5, 5 - 5, 5 * 5, 5 / 5
- case3: 555, 55 + 5, 55 - 5, 55 * 5, 55 / 5 -> case1 + case2, case1 - case2

"""


def solution(N, number):
    """
    Returns:
        - N과 사칙연산만 사용해서 number를 표현할 수 있는 방법 중 N 사용횟수의 최솟값
    """
    comb = defaultdict(list)
    
    for i in range(1, 9):
        comb[i].append(int(str(N)*i))
        for j in range(1, i):
            for n in comb[j]:
                for k in comb[i-j]:
                    comb[i].append(n+k)
                    comb[i].append(n-k)
                    comb[i].append(n*k)
                    if k != 0:
                        comb[i].append(n//k)
        if number in comb[i]:
            return i
        
    return -1


if __name__ == "__main__":
    N = 2
    number = 2
    print(solution(N, number)) 