from collections import defaultdict
def solution(n, results):
    """
    Parameters:
        - n (int): 선수의 수
        - results (List[int]): 경기 결과를 담은 2차원 배열
    Returns:
        - 정확하게 순위를 매길 수 있는 선수의 수 (int)
    """
    win = defaultdict(set)
    lose = defaultdict(set)
    for winner, loser in results:
        win[loser].add(winner)
        lose[winner].add(loser)

    # lose + win 개수 == n-1 이면 순위 확정
    for i in range(1, n+1):
        for winner in win[i]:
            lose[winner].update(lose[i])
        for loser in lose[i]:
            win[loser].update(win[i])
    answer = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1

    return answer

if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

    print(solution(n, results))