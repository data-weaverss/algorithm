from collections import deque


def solution(prices):
    stack = []  # (idx, price) 저장
    answer = [0] * len(prices)

    # 가격 리스트를 (인덱스, 가격) 형태로 변환 후 뒤집기
    indexed_prices = [(time, price) for time, price in enumerate(prices)][::-1]

    for cur_time, cur_price in indexed_prices:
        # 현재 가격보다 크거나 같은 가격을 가진 요소가 스택에 있다면 제거
        # 2 -> stack [3, 1], 앞으로 3을 만나기전에 2를 만나게 되므로 3은 제거해도 됨
        while stack and stack[-1][1] >= cur_price:
            stack.pop()

        if stack:  # 스택이 비어있지 않다면 나보다 작은 가격을 가진 요소가 있다는 뜻
            answer[cur_time] = stack[-1][0] - cur_time
        else:  # 가격이 끝까지 떨어지지 않은 경우
            answer[cur_time] = len(answer) - 1 - cur_time

        # 현재 가격 정보 추가
        stack.append((cur_time, cur_price))

    return answer


if __name__ == "__main__":
    prices = [1, 2, 4, 3, 2, 3, 1]
    print(solution(prices))
