import sys
from collections import Counter

"""
입력 단어 중에서 "비슷한 단어"의 개수를 세야 한다.
비슷한 단어:
기준 단어에서 → 한 글자를 추가, 삭제, 교체 중 한 가지에 해당한 경우

각 단어를 Counter()를 이용하여 알파벳 개수 딕셔너리를 만들고, 차이를 비교한다.
"""
N = int(sys.stdin.readline())
word = sys.stdin.readline().strip()
word_counter = Counter(word)

similar_cnt = 0
for _ in range(N - 1):
    input_word = sys.stdin.readline().strip()
    input_counter = Counter(input_word)

    diff = 0
    for ch in (set(word_counter) | set(input_counter)):
        diff += abs(word_counter[ch] - input_counter[ch])

    if diff == 0 or diff == 1:
        # 같은 단어이거나 추가 또는 삭제
        similar_cnt += 1
    elif diff == 2 and len(word) == len(input_word):
        # 한 단어만 교체한 경우
        similar_cnt += 1

print(similar_cnt)