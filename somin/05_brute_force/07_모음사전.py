def solution(word):
    """return: 사전에서 몇 번째 단어인지"""
    vowels = ['A', 'E', 'I', 'O', 'U']
    multipliers = [781, 156, 31, 6, 1]  # 각 자리에서의 가중치

    answer = 0
    for i, w in enumerate(word):
        answer += vowels.index(w) * multipliers[i] + 1  # 인덱스 기반 계산
    
    return answer

if __name__ == "__main__":
    word = "I"
    sol = solution(word)
    print(sol)  # 1563