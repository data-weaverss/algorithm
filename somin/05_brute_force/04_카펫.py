def solution(brown, yellow):
    vertical = 3 # 초기화
    while True:  # 최소 크기 3부터 가능한 세로 길이 탐색
        horizon = ((brown + 4) // 2) - vertical  # 테두리 블록 수를 이용하여 가로 길이 계산
        # brown = (horizon + vertical) * 2 - 4 
        
        # 가로 길이가 세로보다 작아지면 종료
        if vertical > horizon:
            break
        
        # 전체 타일 개수와 일치하는지 확인
        if vertical * horizon == brown + yellow:
            return [horizon, vertical]  # [가로, 세로] 순서로 반환

        vertical += 1        

    return []

if __name__ == "__main__":
    brown = 10
    yellow = 2
    sol = solution(brown, yellow)
    print(sol)