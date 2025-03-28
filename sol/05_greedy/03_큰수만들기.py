"""
- 4177252841, target_len = 6
    - 41772 에서 max_digit = 7, max_idx = 2
- 7252841, target_len = 5
    - 725 에서 max_digit = 7, max_idx = 0
- 252841, target_len = 4
    - 252 에서 max_digit = 5, max_idx = 1
- 2841, target_len = 3
    - 28 에서 max_digit = 8, max_idx = 1
- 41, target_len = 2
"""

""" chatgpt가 추천해준 방법
- 4177252841

	1.	Stack을 사용하여 숫자를 하나씩 추가한다.
	2.	현재 숫자가 Stack의 마지막 숫자보다 크면 Stack에서 제거(단, k가 남아있는 경우만 제거).
	3.	모든 숫자를 확인한 후, Stack에 남은 숫자에서 k개를 더 제거해야 하면, 뒤에서 삭제.

1. [4]        (4 추가)
2. [4, 1]     (1 추가)
3. [4, 1, 7]  (7 추가 → 이전 값(1)이 작으므로 제거)
4. [7]     (7 유지)
5. [7, 7]  (7 추가)
6. [7, 7, 2] (2 추가)
7. [7, 7, 5] (5 추가 → 2 제거)
8. [7, 7, 5, 2] (2 추가)
9. [7, 7, 5, 8] (8 추가 → 5 제거, 2 제거)
10. [7, 7, 8]  (8 유지)
11. [7, 7, 8, 4] (4 추가)
12. [7, 7, 8, 4, 1] (1 추가)

"""

def solution(number, k):
    """
    Args
        number: 숫자 문자열
        k: 제거할 숫자의 개수
    Return
        numbers에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
    """
    target_len = len(number) - k  # 최종적으로 만들어야 할 숫자의 길이
    answer = ''
    
    while target_len > 1:
        sub_number = number[:-target_len+1]
        
        max_digit = '0'
        max_idx = 0
        for i in range(len(sub_number)):
            if sub_number[i] > max_digit:
                max_digit = sub_number[i]
                max_idx = i
            if max_digit == '9':
                max_idx = i
                break
    
        
        answer += max_digit
        number = number[max_idx + 1:]
        target_len -= 1
        
    return answer + max(number)


if __name__ == "__main__":
    number = "4177252841"
    k = 4
    print(solution(number, k))


