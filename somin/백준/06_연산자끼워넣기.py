import sys
from itertools import permutations

def solution(n, nums, op_counts):
    """
    Parameters:
        - n (int): 수의 개수 
        - nums (List[int]): 숫자 리스트
        - op_counts (List[int]): +, -, *, / n-1개의 연산자 개수
    Returns:
        만들 수 있는 결과의 최대, 최소값
    """
    max_result, min_result = -float('inf'), float('inf')
    operator_list = []
    symbols = ['+', '-', '*', '/']

    for cnt, symbol in zip(op_counts, symbols):
        operator_list.extend([symbol] * cnt)
    
    # 연산자 순서에 대한 순열
    for ops in set(permutations(operator_list, n-1)):
        result = nums[0]
        for i in range(1, n):
            if ops[i - 1] == '+':
                result += nums[i]
            elif ops[i - 1] == '-':
                result -= nums[i]
            elif ops[i - 1] == '*':
                result *= nums[i]
            elif ops[i - 1] == '/':
                if result < 0:
                    result = -(-result // nums[i])
                else:
                    result = result // nums[i]
        max_result = max(max_result, result)
        min_result = min(min_result, result)    

    print(max_result)
    print(min_result)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    op_counts = list(map(int, sys.stdin.readline().split()))
    
    solution(n, nums, op_counts)