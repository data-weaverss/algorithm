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
    always_valid = 0
    word_strip = []
    for word in words:
        filtered = set(word) - necessary
        if not filtered:
            always_valid += 1
            continue
        elif len(filtered) <= teach_cnt:
            required_letters.update(filtered)
            word_strip.append(filtered)
    
    if len(required_letters) <= teach_cnt:
        return always_valid + len(word_strip)
    
    # 21개 중 K-5개 선택, C(21, K-5) 최댓값: C(21, 11) = 352716
    for chosen_words in combinations(required_letters, teach_cnt):
        count = 0
        # 21 + 5
        learned = set(chosen_words) | necessary
        for word in word_strip: # N: 50
            # 7
            for c in word:
                if c not in learned:
                    break
            else:
                count += 1
                    
        answer = max(answer, count)
    # 352,716 × 50 × 7 = 123450600
    return always_valid + answer
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = list(map(int, input().split()))
    words = list(input().strip() for _ in range(N))
    print(solution(K, words))