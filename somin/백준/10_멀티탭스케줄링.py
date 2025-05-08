import sys
from collections import defaultdict, deque

def solution(n, k, order):
    """멀티탭 콘센트를 바꾸는 최소횟수"""
    # 용품별 사용 순서
    order_dict = defaultdict(deque)
    for idx, device in enumerate(order):
        order_dict[device].append(idx)

    multitap = []
    switch_cnt = 0

    for i in range(k): # 콘센트 사용 순섭 용품을 모두 순회
        curr = order[i] # 사용해야 할 용품
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