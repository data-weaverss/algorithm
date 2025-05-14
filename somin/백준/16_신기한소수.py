import sys
from itertools import product

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    
    return True

def solution(N):
    """N자리 수에서, 모든 자릿수가 소수인 수를 오름차순으로 출력"""
    # 첫 자리는 2, 3, 5, 7만 가능
    current_level = [2, 3, 5, 7]

    for _ in range(1, N):  # 이미 1자리 있으므로 N-1번만 반복
        next_level = []
        for num in current_level:
            for digit in [1, 3, 7, 9]:  # 짝수, 5 제외
                new_num = num * 10 + digit
                if is_prime(new_num):
                    next_level.append(new_num)
        current_level = next_level

    for num in current_level:
        print(num)
        

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    solution(N)