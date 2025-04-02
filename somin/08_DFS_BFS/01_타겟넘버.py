from collections import deque

def solution(numbers, target):
    """
    input:
        - numbers: 숫자가 담긴 배열
        - target: 타겟 넘버
    return:
        타겟 넘버를 만드는 경우의 수
    """
    q = deque([0])
    for num in numbers:
        for _ in range(len(q)):
            current = q.popleft()
            q.append(current + num)
            q.append(current - num)
    
    return q.count(target)

if __name__ == "__main__":
    numbers = [4, 1, 2, 1]
    target = 4
    print(solution(numbers, target))  