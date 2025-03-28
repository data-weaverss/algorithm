def solution(name):
    last_non_a_index = 0  # 마지막으로 'A'가 아닌 문자의 위치
    vertical_moves = 0  # 알파벳 변경 횟수
    min_horizontal_moves = float('inf') # 자리 이동 횟수

    # 문자열 순회
    for cur_position in range(len(name)):
        if name[cur_position] != 'A':  # 현재 문자가 'A'가 아닌 경우 처리
            vertical_moves += calculate_char_moves(name[cur_position])  

            if cur_position == 0:  # 첫 번째 문자는 이동 계산을 건너뜀
                continue

            from_last_to_cur = 2*last_non_a_index + len(name) - cur_position
            from_cur_to_last = 2*(len(name) - cur_position) + last_non_a_index

            min_horizontal_moves = min(min_horizontal_moves, min(
                from_last_to_cur, from_cur_to_last
            ))
            last_non_a_index = cur_position  # 마지막으로 'A'가 아닌 문자의 위치 업데이트

    # 최종적으로 직진으로 왔을 때 이동 횟수와 지금까지 구한 최소 이동 횟수 중 작은 값을 선택
    min_horizontal_moves = min(last_non_a_index, min_horizontal_moves)
    return vertical_moves + min_horizontal_moves

# 문자 변경 횟수 계산
def calculate_char_moves(target_word):
    return min(26 - (ord(target_word) - ord('A')), ord(target_word) - ord('A'))

if __name__ == "__main__":
    name = "ABBAAABAAAABB"
    print(solution(name))
