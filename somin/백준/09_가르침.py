import sys
from itertools import combinations

def solution(n, k, words):
    """K개의 글자를 가르칠 때, n개의 단어 words 중 읽을 수 있는 단어 개수의 최댓값"""
    if k < 5: # 필수 알파벳 만족 못함
        return 0
    
    essential = {'a', 'n', 't', 'i', 'c'}
    new_words = [set(word[4:-4]) for word in words] # anta, tica 제거

    # 후보 알파벳의 k-5개 조합
    all_letters = [chr(i + ord('a')) for i in range(26)]
    candidates = [ch for ch in all_letters if ch not in essential]
    comb_list = list(combinations(candidates, k - 5))

    max_count = 0
    # 조합 하나씩 탐색
    for i in range(len(comb_list)):
        # 읽을 수 있는 단어 개수 계산
        learned = essential.union(comb_list[i])
        readable = 0
        for word in new_words:
            for ch in word:
                if ch not in learned:
                    break
            else:
                readable += 1
    
        max_count = max(max_count, readable)

    return max_count

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())

    words = []
    for _ in range(n):
        words.append(sys.stdin.readline().strip())
    
    print(solution(n, k, words))