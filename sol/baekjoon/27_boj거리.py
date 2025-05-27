import sys
from collections import defaultdict

def solution(block_num, block):
    """
    B, O, J 순서로 블록을 밟으면서 점프
    한 번 k칸 만큼 점프를 하는데 필요한 에너지의 양은 k * k
    스타트가 링크를 만나는데 필요한 에너지 양의 최솟값을 반환
    만날 수 없는 경우에는 -1
    
    1 <= block_num <= 9
    
    총 시간 복잡도: O(50 x 1,001) = O(50,050)
    핵심 아이디어: 현재 단계의 가능한 볼륨을 이전 단계의 결과에만 의존
    """  
    
    record = defaultdict(list) 
    record['B'] = [(0, 0)] # idx, jump_cnt 
    order = {'B':'J', 'O':'B', 'J':'O'}  
    
    for idx in range(1, block_num - 1):
        prev = order[block[idx]] 
        if prev not in record: continue 
        for prev_idx, jump_cnt in record[prev]:
            jump_cnt += (idx - prev_idx) ** 2
            record[block[idx]].append((idx, jump_cnt))
            
    prev = order[block[block_num-1]]
    if prev not in record: return -1
    min_jump = float('inf')
    for prev_idx, jump_cnt in record[prev]:
        jump_cnt += (block_num-1 - prev_idx) ** 2
        min_jump = min(jump_cnt, min_jump)  
    return min_jump
                
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    block = input().rstrip("\n")
    
    print(solution(N, block))
