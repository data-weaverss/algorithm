import sys
from collections import defaultdict
sys.setrecursionlimit(10**6) # RecursionError

def dfs(node, parent):
    """
    모든 사람에게 아이디어를 전파하는데 필요한 얼리 아답터의 최소 수
    - 조건: 모든 사용자(정점)는 직접 얼리어답터이거나, 이웃들이 모두 얼리어답터여야 한다.
    - 트리 구조
    """
    dp[node][0] = 0  # node가 얼리어답터가 아닌 경우
    dp[node][1] = 1  # node가 얼리어답터인 경우

    for child in tree[node]:
        if child == parent: # tree가 무방향이기 때문에
            continue
        dfs(child, node)
        dp[node][0] += dp[child][1]                     # 자식은 반드시 얼리어답터
        dp[node][1] += min(dp[child][0], dp[child][1])  # 자식이 얼리어답터든 아니든 상관없기 때문에 최소 개수 선택

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    tree = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        tree[u].append(v)
        tree[v].append(u)

    dp = [[0, 0] for _ in range(n + 1)]
    dfs(1, -1)
    print(min(dp[1][0], dp[1][1]))