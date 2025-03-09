def is_prime(number):
    """주어진 숫자가 소수인지 판별"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):  # 제곱근까지만 확인
        if number % i == 0:
            return False
    return True


def generate_combinations(index, cur_number, digits, visited, results):
    results.add(int(cur_number))  # 현재까지 만든 숫자 저장
    visited[index] = True # 현재 숫자를 방문 처리
    
    # 모든 숫자를 탐색하면서 조합 생성
    for idx, digit in enumerate(digits):
        if not visited[idx]:
            generate_combinations(idx, cur_number + digit, digits, visited, results)
    
    visited[index] = False # 재귀 호출 후 현재 숫자를 방문 해제

def solution(numbers):
    """
    - numbers: 숫자 문자열
    - return: 한자리 숫자로 만들 수 있는 소수의 개수
    """
    # 숫자 문자열을 리스트로 변환
    digits = list(numbers)
    results = set() # 생성된 숫자를 저장할 set(중복 제거)
    
    # 각 숫자를 시작점으로 하여 가능한 모든 숫자 조합 생성
    for idx, digit in enumerate(digits):
        visited = [False] * len(numbers) # 방문 여부 리스트 초기화
        generate_combinations(idx, digit, digits, visited, results)
    
    # 소수 개수 반환
    return sum(is_prime(num) for num in results)

if __name__ == "__main__":
    numbers = "0113"
    print(solution(numbers))



"""
참고
from itertools import permutations

for length in range(1, len(numbers) + 1):
    for perm in permutations(numbers, length):
        unique_numbers.add(int("".join(perm)))  # 문자열을 정수로 변환하여 저장
"""
