import sys
from collections import defaultdict

def solution(block_num, block):
    """
    B, O, J 순서로 블록을 밟으면서 점프
    한 번 k칸 만큼 점프를 하는데 필요한 에너지의 양은 k * k
    스타트가 링크를 만나는데 필요한 에너지 양의 최솟값을 반환
    만날 수 없는 경우에는 -1
    
    1 <= block_num <= 1,000
    
    총 시간 복잡도: O(10^6 log10^3)
    핵심 아이디어: 현재 단계의 가능한 점프 수를 이전 단계의 결과에 의존
    """  
    # dp: 각 블록 종류별로 (인덱스, 누적 점프 에너지) 튜플을 저장하는 딕셔너리
    # 예) dp['B'] = [(0, 0)] : 0번 인덱스에 B가 있고, 점프 에너지는 0
    dp = defaultdict(list) 
    dp['B'] = [(0, 0)] # idx, jump_cnt 
    
    # prev_map: 현재 밟을 블록에서 이전에 밟아야 할 블록을 지정
    # 'B'는 'J'에서, 'O'는 'B'에서, 'J'는 'O'에서만 올 수 있음
    prev_map = {'B':'J', 'O':'B', 'J':'O'}  
    
    for idx in range(1, block_num):
        # 현재 블록에 오기 위해 필요한 이전 블록 타입
        prev_char = prev_map[block[idx]] 
        
        # 이전 블록 타입이 dp에 없으면(즉, 올 수 있는 경로가 없으면) 스킵
        if prev_char not in dp: continue 
        
        # 이전 블록의 모든 위치에서 현재 위치로 점프하는 경우를 모두 계산
        candidate_jumps = []
        for prev_idx, jump_cnt in dp[prev_char]:
            jump_cnt += (idx - prev_idx) ** 2
            candidate_jumps.append((idx, jump_cnt))
            
        # 누적 에너지가 가장 작은 경로만 선택 (최적 경로만 남김)
        candidate_jumps.sort(key = lambda key: key[1])
        dp[block[idx]].append(candidate_jumps[0])
        
        if idx == block_num - 1:
            return candidate_jumps[0][1]
        
    return -1
                
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    block = input().rstrip("\n")
    
    print(solution(N, block))
