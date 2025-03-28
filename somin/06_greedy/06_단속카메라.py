def check_overlap(car1, car2):
    if car1[1] >= car2[0]: # 겹치는 구간이 있을 때
        return [max(car1[0], car2[0]), min(car1[1], car2[1])]
    else: # 겹치지 않을 때
        return None

def solution(routes):
    """
    input:
        routes: 차량의 이동 경로 [진입 지점, 진출 지점]
    return: 
        모든 차량이 한 번은 단속용 카메라를 만나도록 하는 카메라 최소 설치 개수
    """
    routes.sort() # 진입 기준으로 오름차순 정렬
    # [[-20, -15], [-18, -13], [-14, -5], [-5, -3], [0, 100], [2, 10], [20, 101], [80, 95]]
    cctv_cnt = 0
    i = 0
    n = len(routes)

    while i < n:
        overlap = routes[i]
        i += 1

        while i < n: # 다음 차량 경로와 겸치는 구간 좁혀가기
            new_overlap = check_overlap(overlap, routes[i])
            if new_overlap is None: 
                break  # 겹치지 않으면 현재 cctv 위치 확정
            overlap = new_overlap
            i += 1
        
        cctv_cnt += 1 # cctv 설치

    return cctv_cnt

if __name__ == "__main__":
    routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3], [0, 100], [2, 10], [20, 101], [80, 95]]
    print(solution(routes))