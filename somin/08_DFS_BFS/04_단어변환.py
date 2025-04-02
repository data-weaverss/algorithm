from collections import deque

def solution(begin, target, words):

    if target not in words:
        return 0
    
    q = deque([(begin, 0)])  # (현재 단어, 변환 단계 수)
    visited = set([begin])   # 시작 단어 방문 처리

    while q:
        curr_word, step = q.popleft()
        
        if curr_word == target:
            return step

        # 현재 단어와 한 글자만 다른 단어 찾기
        for word in words:
            diff_cnt = 0
            for c, w in zip(curr_word, word):
                if c != w:
                    diff_cnt += 1
                if diff_cnt > 1:
                    break

            # 알파벳이 1개만 다르고, 방문하지 않은 단어일 때,
            if diff_cnt == 1 and word not in visited:
                q.append((word, step + 1))
                visited.add(word)
            
    return 0


if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    
    print(solution(begin, target, words)) # 4