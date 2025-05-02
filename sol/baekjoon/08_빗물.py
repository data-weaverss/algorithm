import sys

def solution(height, width, blocks_height):
    """
    height: 세계의 높이
    width: 세계의 폭
    blocks_height: 각 세계 한 열에 쌓여있는 블록의 높이
    """  
    
    map = [[0] * width for _ in range(height)]
    
    for col, block_h in enumerate(blocks_height):
        for row in range(height - block_h, height):
            map[row][col] = 1
    
    total = 0
    
    for row in range(height-1, -1, -1):
        prev = -1
        for col in range(width):
            if map[row][col] == 1:
                if prev != -1:
                    total += col - prev - 1
                prev = col
    
    return total
        
        
if __name__ == "__main__":
    input = sys.stdin.readline
    H, W = list(map(int, input().split()))
    blocks_height = list(map(int, input().split()))
    print(solution(H, W, blocks_height))