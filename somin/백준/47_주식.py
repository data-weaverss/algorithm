import sys

"""
하루에 한 주식을 사거나, 원하는 만큼 팔거나, 아무것도 하지 않을 수 있다.
미래의 주가를 미리 알고 있을 때, 가능한 최대 이익을 구하라.

주가를 뒤에서부터 보면서 현재까지의 '최고가'를 갱신해가며 계산한다.
현재 주가가 '최고가'보다 낮으면, 지금 사서 나중에 팔면 이익이므로 그 차익을 누적한다.
"""
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))  # 주가 리스트

    max_price = 0
    profit = 0

    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            # 현재가가 최고가보다 낮으면 차익 누적
            profit += max_price - price
            
    print(profit)
