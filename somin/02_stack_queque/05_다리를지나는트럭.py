# 모든 트럭이 다리를 건더는 최단시간 return
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length) # 다리 길이만큼 큐로 초기화
    truck_weights = deque(truck_weights) # 트럭 무게 큐로 초기화
    time = 0 # 다리를 건너는 시간 저장
    # 남아있는 트럭이 없을 때까지
    while truck_weights:
        time += 1
        truck = truck_weights.popleft()
        bridge.popleft() # 다리를 모두 건넌 트럭 또는 0 popleft
        if sum(bridge)+truck <= weight: # 합이 제한무게를 넘지 않는다면
            bridge.append(truck)
        else: # 넘었다면 트럭을 다시 truck_weights 삽입,
            truck_weights.appendleft(truck)
            bridge.append(0)
    
    # 다리에 있는 트럭 모두 건너는 시간 추가
    time += len(bridge)
    return time
            

if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    sol = solution(bridge_length, weight, truck_weights)
    print(sol) # 110