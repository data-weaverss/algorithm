import sys
from heapq import heappop, heappush

""" 
    1. 주식을 하나 산다
    2. 원하는 만큼 가지고 있는 주식을 판다.
    3. 아무것도 안한다. 
    최대 이익을 나타내는 정수 하나를 출력
    
    1 <= day <= 10^6, 1 <= stock <= 10^4
    
    핵심아이디어: 그리디 -> 더 높은 주가가 나타날 때 과거의 주식을 모두 파는 것
    과거의 주식을 판 개수만큼, 오늘 산 주식을 다시 삼
    
    7 3 5 4 3 4
""" 
def solution(day, stocks):
    pq = [] # (가격, 개수)를 저장하는 최소 힙 → 낮은 가격부터 빠르게 꺼냄
    answer = 0 # 총 이익
    
    for stock in stocks:
        cnt = 1  # 오늘 산 주식 1개 포함
        
        # 현재 가격보다 낮은 주식을 모두 팔아 이익 실현
        while pq and pq[0][0] < stock:
            prev_stock, prev_cnt = heappop(pq)
            # 이익 = (현재가 - 과거가) * 보유 개수
            answer += (stock - prev_stock) * prev_cnt
            cnt += prev_cnt # 지금 가격으로 다시 묶어 보유할 개수 증가
        
        # 현재 가격과 총 수량을 힙에 다시 저장
        heappush(pq, (stock, cnt))
    
    print(answer)
    
if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    N_list = []
    stocks_list = []
    
    for _ in range(T):
        N_list.append(int(input()))
        stocks_list.append(map(int, input().split()))
    
    for N, stocks in zip(N_list, stocks_list):
        solution(N, stocks)