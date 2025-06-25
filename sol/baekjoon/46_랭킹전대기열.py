import sys

""" 
    최종적으로 만들어진 방의 상태와 입장 플레이어들을 출력
    - 처음 입장한 플레이어의 레벨을 기준으로 -10부터 +10까지 입장 가능

    1 <= player_cnt <= 300, 1 <= room_capacity <= 300,
    1 <= level <= 500
""" 
def solution(player_cnt, room_capacity, levels, players):
    rooms = []
    
    for level, player in zip(levels, players):
        matched = False
        for room in rooms:
            if len(room) >= room_capacity:
                continue
            if abs(level - room[0][0]) > 10:
                continue
            else:
                room.append((level, player))
                matched = True
                break
        if not matched:
            rooms.append([(level, player)])
    
    for room in rooms:
        if len(room) != room_capacity:
            print("Waiting!")
        else:
            print("Started!")
        room.sort(key=lambda key: key[1])
        for l, n in room:
            print(f"{l} {n}")
        
    
if __name__ == "__main__":
    input = sys.stdin.readline
    p, m = list(map(int, input().split()))
    levels = []
    names = []
    
    for _ in range(p):
        i = input().split()
        levels.append(int(i[0]))
        names.append(i[1])
    
    solution(p, m, levels, names)