from itertools import permutations
def is_prime(num):
    if num < 2: # 0, 1
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, num, 2): # 홀수만 검사
        if num % i == 0:
            return False

    return True

def solution(numbers):
    # 모든 경우의 수
    permut_cases = set() # 중복 방지를 위해 집합 사용
    for length in range(1, len(numbers)+1): # 1부터 자리수까지 모든 순열
        for perm in permutations(numbers, length):
            num = int("".join(perm))
            permut_cases.add(num)
            # {0, 1, 101, 10, 11, 110}

    # 소수 찾기
    cnt_prime = 0
    for num in permut_cases:
        if is_prime(num):
            cnt_prime += 1

    return cnt_prime

if __name__ == "__main__":
    numbers = "011"
    nums_list = list(numbers)
    sol = solution(numbers)
    print(sol)