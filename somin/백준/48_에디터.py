import sys

left = list(sys.stdin.readline().strip())  # 커서 왼쪽 문자들
right = []                    # 커서 오른쪽 문자들

M = int(sys.stdin.readline())
for _ in range(M):
    cmd = sys.stdin.readline().strip()
    if cmd == 'L':
        if left:
            right.append(left.pop())
    elif cmd == 'D':
        if right:
            left.append(right.pop())
    elif cmd == 'B':
        if left:
            left.pop()
    else:  # 'P x'
        _, x = cmd.split()
        left.append(x)

print(''.join(left + right[::-1]))
