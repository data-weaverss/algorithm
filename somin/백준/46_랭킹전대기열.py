import sys

if __name__ == "__main__":
    P, M = map(int, sys.stdin.readline().split())  # 플레이어 수, 방 최대 인원 수
    rooms = []  # 각 방: [기준레벨, 플레이어 리스트]

    for _ in range(P):
        level, nickname = sys.stdin.readline().split()
        level = int(level)

        # 입장 가능한 방 탐색
        for room_level, players in rooms:
            if len(players) < M and abs(room_level - level) <= 10:
                players.append((level, nickname))
                break
        # 입장 가능한 방이 없으면 새 방 생성
        else:
            rooms.append([level, [(level, nickname)]])

    # 결과 출력
    for room_level, players in rooms:
        if len(players) == M:
            print("Started!")
        else:
            print("Waiting!")

        # 닉네임 사전순 정렬 후 출력
        for level, name in sorted(players, key=lambda x: x[1]):
            print(level, name)
