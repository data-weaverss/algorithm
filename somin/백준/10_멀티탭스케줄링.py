import sys
from collections import defaultdict, deque

def solution(n, k, order):
    """
    Parameters:
        n: 멀티탭 구멍의 개수
        k: 전자기기 사용 횟수
        order: 전자기기 사용 순서
    Returns:
        최소한의 플러그 교체 횟수
    """
    # 기기별 사용 순서
    order_dict = defaultdict(deque)
    for idx, device in enumerate(order):
        order_dict[device].append(idx)

    multitap = []
    switch_cnt = 0

    # 플러그 사용 순서 순회하면서 교체 횟수 계산
    for i in range(k): 
        curr = order[i] # 사용해야 할 기기
        order_dict[curr].popleft()

        if curr in multitap:
            continue
        if len(multitap) < n:
            multitap.append(curr)
            continue
        
        # 교체할 기기 선택
        farthest_idx = -1 # 가장 늦게 사용하는 순서
        to_remove = -1 # 교체할 기기 번호
        for device in multitap:
            if not order_dict[device]:  # 앞으로 사용되지 않음
                to_remove = device
                break

            next_use = order_dict[device][0]
            if next_use > farthest_idx:
                farthest_idx = next_use
                to_remove = device

        multitap.remove(to_remove)
        multitap.append(curr)
        switch_cnt += 1

    return switch_cnt

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    order = list(map(int, sys.stdin.readline().split()))
    
    print(solution(n, k, order))