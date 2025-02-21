# 가격이 떨어지지 않은 기간은 몇 초인지를 return
def solution(prices):
    n = len(prices)
    prices_not_fall = [0] * n

    for i in range(n): # 'i초 시점의 주가'의 떨어지지 않은 기간 계산
        for j in range(i+1, n): # 'i초 시점의 주가' 다음부터의 주가
            prices_not_fall[i] += 1 # 다음 시점으로 넘어갈 때마다 1초씩 추가
            if prices[j] < prices[i]: # 가격 하락했을 때 stop
                break
  
if __name__ == "__main__":
    prices = [4, 3, 1, 1, 0]
    sol = solution(prices)
    print(sol) # 출력: [4, 3, 1, 1, 0]