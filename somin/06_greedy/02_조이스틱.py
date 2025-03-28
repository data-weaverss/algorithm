def solution(name):
    # 알파벳 조작 횟수 초기화 (A에서 목표 문자까지 이동 횟수)
    alphabet = {}
    k = 0
    for i in range(26):
        a = chr(ord('A') + i)
        if i < 13:
            alphabet[a] = i
        else:
            alphabet[a] = 13 - k
            k += 1
    # {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 
    # 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}

    cnt = 0  # 총 조작 횟수
    p = 0  # 현재 위치 포인터
    length = len(name)  # 문자열 길이

    # 상하 이동 (알파벳 변경)
    for char in name:
        cnt += alphabet[char]

    # "JAAANAAEAAAN"
    # 좌우 이동 최적화
    min_move = length - 1  # 단순히 한쪽 방향으로 쭉 이동하는 경우(최대 이동 횟수)
    # J → A → A → A → N → A → A → E → A → A → A → N = 11번

    for i in range(length):
        next = i + 1  # 다음 문자 위치
        while next < length and name[next] == 'A':  # 연속된 'A' 찾기
            next += 1

        # 오른쪽으로 i까지 갔다가 되돌아와서 반대쪽으로 가는 경우
        option1 = 2 * i + (length - next)
        # 0 → 1 → 2 → 3 → (되돌아오기) → 4 → ... → 11

        # 왼쪽으로 먼저 갔다가 다시 오른쪽으로 가는 경우
        option2 = i + 2 * (length - next)

        # 최소 이동 횟수 갱신
        min_move = min(min_move, option1, option2)

    cnt += min_move  # 최적의 좌우 이동 추가
    return cnt

if __name__ == "__main__":
    name = "JAN" # "JAAANAAEAAAN"
    sol = solution(name)
    print(sol)  # 23