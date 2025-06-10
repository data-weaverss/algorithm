import sys
import pprint

def solution(N, numbers):
    """
    주어진 수열에서 numbers[0]부터 시작하여 각 숫자에 + 또는 - 연산을 사용해 numbers[-1](목표값)을 만드는 경우의 수를 계산
    - 중간 계산 값이 0~20을 벗어나면 안 된다.
    """
    # dp[i][j]: i번째 위치까지 숫자를 사용했을 때, 결과가 j가 되는 경우의 수
    dp = [[0] * 21 for _ in range(N - 1)] 
    dp[0][numbers[0]] = 1 # 첫 숫자를 바로 사용할 수 있는 경우는 1가지뿐
    
    target = numbers.pop()
    
    for i in range(N - 2):
        for result in range(21):
            if dp[i][result] == 0:
                continue

            plus_num = result + numbers[i + 1]
            minus_num = result - numbers[i + 1]

            if plus_num <= 20:
                dp[i + 1][plus_num] += dp[i][result]
            if minus_num >= 0:
                dp[i + 1][minus_num] += dp[i][result]

    # pprint.pprint(dp)
    return dp[N - 2][target]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().strip().split()))

    print(solution(N, numbers))