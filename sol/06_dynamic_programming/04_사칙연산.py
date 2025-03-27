def solution(arr):
    """
    Args
    - arr: 문자열 형태의 숫자와 더하기 기호, 뺄셈 기호가 들어있는 배열 
    Returns
    - 서로 다른 연산순서의 계산 결과 중 최댓값
    """
    arr_int = []
    sign = 1
    for num in arr:
        if num == "+":
            sign = 1
        elif num == "-":
            sign = -1
        else:
            num = int(num)
            arr_int.append(num * sign)
    
    dp = [[0] * len(arr_int) for _ in range(len(arr_int))]
    for i in range(len(arr_int)):
        dp[i][i] = arr_int[i]
                
    # bottom up
    for i in range(len(arr_int) - 2, -1, -1):
        for j in range(i + 1, len(arr_int)):
            candidates = []
            for k in range(i, j):
                if dp[i][k] < 0 and i != 0:
                    candidates.append(-1*(-dp[i][k] + dp[k+1][j]))
                else:
                    candidates.append(dp[i][k] + dp[k+1][j])
            dp[i][j] = max(candidates)
            print(dp)
    return dp[0][-1]

if __name__ == "__main__":
    arr = ["10", "-5", "+", "7", "+", "9", "-", "20", "-", "30", "+", "10"]
    print(solution(arr)) # 1
    