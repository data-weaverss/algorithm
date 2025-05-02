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
    
    answer = 0
    necessary = set('antatica')
    required_letters = set()
    for word in words:
        filtered = set(word) - necessary
        if not filtered:
            words.remove(word)
        elif len(filtered) <= teach_cnt:
            required_letters.update(filtered)
    
    for chosen_words in combinations(required_letters, teach_cnt):
        count = 0
        for word in words:
            if len(set(word) - set(chosen_words) - necessary) == 0:
                count += 1
        answer = max(answer, count)
        
    return answer
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = list(map(int, input().split()))
    words = list(input().strip() for _ in range(N))
    print(solution(K, words))
    