def solution(arr):
    """
    서로 다른 연산순서의 계산 결과 중 최댓값을 return
    input:
        arr: 숫자와, 더하기 기호("+"), 뺄셈 기호("-")가 들어있는 배열
    핵심 아이디어:
        최댓값을 구하기 위해서는 덧셈 뒤에 나오는 수는 가장 커져야 하고, 뺄셈 뒤에 나오는 수는 가장 작아져야 함.
        작은 범위부터 min, max값을 구하면서 전체적인 최댓값을 찾는다.
    예시)    
    gap = 2 (숫자 3개)
    max_val[(0,2)] = 3
    min_val[(0,2)] = 1

    max_val[(1,3)] = 5
    min_val[(1,3)] = 1

    max_val[(2,4)] = 4
    min_val[(2,4)] = -1

    """
    numbers = [int(x) for x in arr[::2]] # 숫자
    operators = [x for x in arr[1::2]] # 연산자
    
    max_val = {} # 범위(key)에서 만들 수 있는 최댓값
    min_val = {} # 범위(key)에서 만들 수 있는 최솟값

    n = len(numbers)
    for i in range(n):
        max_val[(i, i)] = min_val[(i, i)] = numbers[i]

    for gap in range(1, n): # 범위가 1부터 n-1까지
        for start in range(n - gap): # ㅈ
            end = start + gap

            # 괄호를 어디에 하는지 탐색
            max_candidates, min_candidates = [], [] 
            for k in range(start + 1, end + 1): # start=0, end=2 > 5 - 3 + 1
                op = operators[k - 1]
                if op == '-':
                    # 최댓값 = 왼쪽 최대 - 오른쪽 최소
                    max_candidates.append(max_val[(start, k - 1)] - min_val[(k, end)])
                    # 최솟값 = 왼쪽 최소 - 오른쪽 최대
                    min_candidates.append(min_val[(start, k - 1)] - max_val[(k, end)])
                else:
                    # 최댓값 = 왼쪽 최대 + 오른쪽 최대
                    max_candidates.append(max_val[(start, k - 1)] + max_val[(k, end)])
                    # 최솟값 = 왼쪽 최소 + 오른쪽 최소
                    min_candidates.append(min_val[(start, k - 1)] + min_val[(k, end)])

            # 최대/최솟값 업데이트
            max_val[(start, end)] = max(max_candidates)
            min_val[(start, end)] = min(min_candidates)

    return max_val[(0, n - 1)] # 처음부터 끝까지의 최댓값 반환



if __name__ == "__main__":
    arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]	
    print(solution(arr))  