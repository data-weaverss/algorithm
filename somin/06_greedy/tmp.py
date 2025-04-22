def make_alphabet():
    """
    알파벳 조작 횟수 딕셔너리 생성 (A에서 목표 문자까지 최소 이동)
    return:
        {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}
    """
    alphabet = {}
    k = 0
    for i in range(26):
        a = chr(ord('A') + i)
        if i < 13:
            alphabet[a] = i
        else:
            alphabet[a] = 13 - k
            k += 1

    return alphabet

def solution(name):
    alphabet = make_alphabet()
    # 상하 이동(알파벳 변경) 횟수 합산
    total_cnt = sum(alphabet[char] for char in name) 
    length = len(name)  # 문자열 길이

    print(total_cnt)
   
    # 좌우 이동
    # 1. A의 최대길이 구하기
    all_a_index = [i for i in range(length) if name[i] == 'A']
    # [1, 2, 3, 5, 6, 8, 9, 10, 12]

    # 모든 문자가 A일 경우
    if len(all_a_index) == len(name):
        return total_cnt
    # A가 전혀 없는 경우
    if len(all_a_index) == 0:
        return total_cnt + length - 1

    # 1. 연속된 A 그룹 찾기
    grouped_a = []
    temp_group = []

    prev = -2 # 연속성 확인을 위한 초기값
    for i in all_a_index:
        if i != prev + 1:
            # 연속되지 않는 경우, 새 그룹 시작
            grouped_a.append(temp_group)
            temp_group = [] 
        temp_group.append(i)
        prev = i
    grouped_a.append(temp_group)  # 마지막 그룹 추가
    # [[], [1, 2, 3], [5, 6], [8, 9, 10]]

    # 맥스 그룹만 찾기
    max_cnt = len(max(grouped_a, key=len))
    grouped_a = [g for g in grouped_a if len(g) == max_cnt] # 최대 갯수의 A index만 추출
    # 가장 앞부분 A 그룹과 뒷부분 A 그룹 선택
    first_a_group = grouped_a[0]
    last_a_group = grouped_a[-1]
    print('frist:', first_a_group)
    print('last:', last_a_group)
    # 첫 번째 A 그룹 이전 거리와 마지막 A 그룹 이후 거리 계산
    first_a = first_a_group[0] - 1  # 첫 번째 A 그룹의 시작 전 위치
    last_a = length - last_a_group[-1] - 1  # 마지막 A 그룹의 끝 이후 위치
    if first_a < 0: first_a = 0

    # 더 짧은 거리 쪽을 먼저 이동
    total_cnt += min(
     first_a * 2 + (length - first_a_group[-1] - 1),
     last_a * 2 + (last_a_group[0] - 1)
     )
  
    return total_cnt

if __name__ == "__main__":
    # test_cases = ["AAAABAAA"]
    test_cases = ["AAAABAAA", "ABAAABBBAA", "BBAAAABB", "BAAAAAAB", "AAAA", "JAAANAAEAAAN"]
    for name in test_cases:
        print(f"name = {name}, result = {solution(name)}")