import sys

def solution(N):
    """
    1부터 N까지의 수를 이어서 썼을 때, 이 수의 자릿수
    """
    n_digit = len(str(N))
    count = 0
    
    # example: 108
    # 1-9 : 9개  -> 9 * (10 ** (자릿수 - 1)) = 9 * 1
    # 10-99: 90개 -> 9 * (10 ** (2 - 1)) = 9 * 10
    for digit in range(1, n_digit - 1): 
        count += (digit) * (9 * (10 ** (digit - 1)))
    
    # 100 ~ 108: 9개 -> 9개 x 자릿수
    count += n_digit * (N - (10 ** (n_digit - 1)) + 1)
    
    print(count)
        
        
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input()) 
        
    solution(N)