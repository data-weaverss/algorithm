import sys
from itertools import combinations

def solution(teach_cnt, words):
    """
    teach_cnt: 가르칠 알파벳의 개수
    words: anta ** tica 인 남극언어
    """  
    teach_cnt -= 5
    
    if teach_cnt < 0:
        return 0
    
    # O(NL) 
    answer = 0
    necessary = set('antatica')
    required_letters = set()
    for word in words:
        filtered = set(word) - necessary
        if not filtered:
            continue
        elif len(filtered) <= teach_cnt:
            required_letters.update(filtered)
    
    # 21개 중 K-5개 선택, C(21, K-5) 최댓값: C(21, 11) = 352716
    for chosen_words in combinations(required_letters, teach_cnt):
        count = 0
        for word in words: # N: 50
            # 15 + K-5 + 5
            if len(set(word) - set(chosen_words) - necessary) == 0:
                count += 1
        answer = max(answer, count)
    # 352,716 × 50 × 15 = 264,537,000
    return answer
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = list(map(int, input().split()))
    words = list(input().strip() for _ in range(N))
    print(solution(K, words))