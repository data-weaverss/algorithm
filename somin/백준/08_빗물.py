import sys

def solution(h, w, blocks):
    result = 0

    for i in range(1, w - 1):  # 양 끝은 물이 고일 수 없음
        left_max = max(blocks[:i])
        right_max = max(blocks[i+1:])
        water = min(left_max, right_max) - blocks[i]
        if water > 0:
            result += water

    return result


if __name__ == "__main__":
    h, w = map(int, input().split())
    blocks = list(map(int, input().split()))
    print(solution(h, w, blocks))
