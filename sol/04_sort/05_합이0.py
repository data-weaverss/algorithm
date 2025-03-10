import sys
from collections import defaultdict

def count_valid_triplets(negatives, positives, negative_count, positive_count):
    answer = 0
    
    def count_pairs(arr, counter):
        nonlocal answer
        for l in range(len(arr) - 1):
            for r in range(l+1, len(arr)):
                total = arr[l] + arr[r]
                if -total in counter:
                    answer += counter[-total]
    
    # 음수 2 + 양수 1의 조합
    count_pairs(negatives, positive_count)
    # 음수 1 + 양수 2의 조합
    count_pairs(positives, negative_count)
    
    return answer

def solution(N, coding_levels):
    """
    - coding_level의 합이 0이 되는 팀을 얼마나 많이 만들 수 있는지
    - 3명으로 구성된 팀만 참가
    - 3476ms 시간으로 통과
    """
    
    answer = 0
    negatives, positives = [], [] # 음수인 코딩 실력, 양수인 코딩 실력
    positive_count = defaultdict(int)
    negative_count = defaultdict(int)
    
    # 입력된 코딩 실력을 양수와 음수로 분리하여 저장
    for level in coding_levels:
        if level >= 0 :
            positives.append(level)
            positive_count[level] += 1
        else:
            negatives.append(level)
            negative_count[level] += 1
    
    # 음수 2개 + 양수 1개 또는 양수 2개 + 음수 1개 조합 확인
    answer += count_valid_triplets(negatives, positives, negative_count, positive_count)
            
    # 0으로만 이루어진 조합 계산(0이 3개 이상일 경우 조합 개수 추가)
    zero_cnt = positive_count[0]
    if zero_cnt >= 3:
        answer += zero_cnt * (zero_cnt-1) * (zero_cnt-2) // 6
    
    return answer
    


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    coding_levels = list(map(int, input().split()))

    print(solution(N, coding_levels))
