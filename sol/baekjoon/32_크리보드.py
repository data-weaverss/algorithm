import sys

def solution(push_cnt):
    """
    크리보드 버튼을 총 push_cnt 번 눌러서 화면에 출력된 A 개수의 최댓값
    
    1 <= push_cnt <= 100
    
    총 시간 복잡도: O(10^4)
    핵심 아이디어: 단순 A 입력 vs 복사 - 붙여넣기 중 더 큰 값을 선택
    """  
    dp = [i for i in range(push_cnt + 1)]
    
    for i in range(1, push_cnt + 1):
        if i <= 2:
            continue
        # 전체 선택 -> 복사 -> 붙여넣기(+3인 숫자부터 배수를 지정 가능)
        for j in range(i + 3, push_cnt + 1):
            dp[j] = max(dp[j], dp[i] * (j - i - 3 + 2))

    return dp[push_cnt]

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())

    print(solution(N))
