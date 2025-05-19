import sys

def solution(s, numbers):
    """
    길이가 s인 '-'와 '|'를 이용해서 출력해야 한다. 
    각 숫자는 모두 s+2의 가로와 2s+3의 세로로 이루어 진다. 
    나머지는 공백으로 채워야 한다. 각 숫자의 사이에는 공백이 한 칸 있어야 한다
     -- a --
    |       |
    f       b
    |       |
     -- g --
    |       |
    e       c
    |       |
     -- d --
    """

    SEGMENTS = {
        '0': [1, 1, 1, 1, 1, 1, 0],
        '1': [0, 1, 1, 0, 0, 0, 0],
        '2': [1, 1, 0, 1, 1, 0, 1],
        '3': [1, 1, 1, 1, 0, 0, 1],
        '4': [0, 1, 1, 0, 0, 1, 1],
        '5': [1, 0, 1, 1, 0, 1, 1],
        '6': [1, 0, 1, 1, 1, 1, 1],
        '7': [1, 1, 1, 0, 0, 0, 0],
        '8': [1, 1, 1, 1, 1, 1, 1],
        '9': [1, 1, 1, 1, 0, 1, 1],
    }

    lines = [""] * (2 * s + 3)
    
    for idx, num in enumerate(numbers):
        seg = SEGMENTS[num]
        
        # a 줄
        lines[0] += " " + ("-" * s if seg[0] else " " * s) + " "
        # f, b 줄
        for i in range(1, s + 1):
            lines[i] += ("|" if seg[5] else " ") + " " * s + ("|" if seg[1] else " ")
        # g 줄
        lines[s + 1] += " " + ("-" * s if seg[6] else " " * s) + " "
        # e, c 줄
        for i in range(s + 2, 2 * s + 2):
            lines[i] += ("|" if seg[4] else " ") + " " * s + ("|" if seg[2] else " ")
        # d 줄
        lines[2 * s + 2] += " " + ("-" * s if seg[3] else " " * s) + " "

        # 숫자 간 간격
        for i in range(2 * s + 3):
            lines[i] += " "
    
    for line in lines:
        print(line)

if __name__ == "__main__":
    s, numbers = sys.stdin.readline().split()
    s = int(s)

    solution(s, numbers)