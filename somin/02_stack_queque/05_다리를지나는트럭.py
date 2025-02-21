# 모든 트럭이 다리를 건더는 최단시간 return
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length) # 다리 길이만큼 큐로 초기화
    truck_weights = deque(truck_weights) # 트럭 무게 큐로 초기화
    time = 0 # 소요 시간
    bridge_weight = 0  # 현재 다리 위의 트럭 무게 합
    
    while truck_weights: # 트럭이 다 건너갈 때까지
        time += 1
        truck = truck_weights.popleft()
        bridge_weight -= bridge.popleft()  # 다리를 건넌 트럭 무게 제거
        
        if bridge_weight <= weight - truck: # 합이 제한무게를 넘지 않는다면
            bridge.append(truck)
            bridge_weight += truck
        else: # 넘었다면 트럭을 다시 truck_weights 삽입,
            truck_weights.appendleft(truck)
            bridge.append(0)
    
    # 다리에 있는 트럭 모두 건너는 시간 추가
    time += bridge_length
    return time
            

if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    sol = solution(bridge_length, weight, truck_weights)
    print(sol) # 110