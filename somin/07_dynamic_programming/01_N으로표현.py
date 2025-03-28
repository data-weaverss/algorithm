"""
N과 사칙연산만 사용해서 표현할 수 있는 방법 중 N 사용횟수의 최솟값을 return
"""
def solution(N, number):
    """
    N과 사칙연산만 사용해서 number를 표현할 수 있는 방법 중 N 사용횟수의 최솟값 return
    input:
        N: 사용 숫자
        number: 만들어야 되는 숫자
    """
    if N == number:
        return 1

    dp = [set() for _ in range(9)]  # dp[i]: N을 i번 사용해서 만들 수 있는 수들의 집합

    for i in range(1, 9): # i=2
        # 숫자 이어붙이기
        dp[i].add(int(str(N) * i)) # dp[1]: (5)
                                   # dp[2]: (55)
        # 두 집합으로 나누어 사칙연산
        for j in range(1, i):
            for op1 in dp[j]: # dp[1]
                for op2 in dp[i-j]: # dp[1]
                    dp[i].add(op1 + op2)
                    if op1 - op2 > 0:
                        dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        
        if number in dp[i]:
            return i
    
    return -1

if __name__ == "__main__":
    N = 5
    number = 12
    sol = solution(N, number)
    print(sol)  # 1563