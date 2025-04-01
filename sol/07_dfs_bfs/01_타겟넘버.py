from collections import deque

# bfs
def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # (index, sum)

    while queue:
        (cur_idx, cur_sum) = queue.popleft()
        if cur_idx == len(numbers):
            if cur_sum == target:
                answer += 1
            continue
        queue.append((cur_idx + 1, cur_sum + numbers[cur_idx]))
        queue.append((cur_idx + 1, cur_sum - numbers[cur_idx]))
    return answer


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target)) #5