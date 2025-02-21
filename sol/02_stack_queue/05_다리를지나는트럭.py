from collections import deque


def solution(bridge_length, weight, truck_weights):
    """
    최대 bridge_length대 올라갈 수 있음
    weight 이하까지의 무게를 견딜 수 있음
    """

    bridge = deque([0] * bridge_length)  # 다리를 표현하는 큐
    seconds = 0  # 경과 시간
    current_weight = 0  # 현재 다리 위 트런 무게 합

    for truck_weight in truck_weights:

        while True:
            current_weight -= bridge.popleft()
            seconds += 1

            if (
                current_weight + truck_weight <= weight
            ):  # 다음 트럭이 올라갈 수 있는 경우
                bridge.append(truck_weight)
                current_weight += truck_weight
                break
            else:  # 무게 초과라면 빈 공간(0) 추가
                bridge.append(0)

    # 마지막 트럭이 다리를 지나는 시간 추가
    # |도착지|---|---|현재 위치|
    #       <---다리 ------->
    # 다리에 오른 순간부터 다리의 길이만큼(3) 더 가야함
    return seconds + bridge_length


if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    print(solution(bridge_length, weight, truck_weights))
