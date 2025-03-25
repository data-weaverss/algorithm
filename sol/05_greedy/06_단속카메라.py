def solution(routes):
    """
    - 고속도로를 이용하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라 설치
    Args:
        - routes: [차량의 진입, 이탈 지점] 리스트
    Return:
        - 카메라의 최소 개수
    """
    routes.sort(key=lambda x: x[1])  # 이탈점을 기준으로 정렬
    cctv = routes[0][1]  # 이탈점이 가장 빠른 차량에 cctv 설치
    answer = 1
    
    for enter, exit in routes:
        if enter <= cctv <= exit: # 설치된 cctv를 지나가는 차량
            continue
        
        cctv = exit # 지금 설정된 cctv를 지나가지 않는 차량
        answer += 1 # cctv를 그 차량의 이탈점으로 새로 설치
    return answer


if __name__ == "__main__":
    routes = [[-20,-15], [-14,-5], [-18, -16], [-5,-3]]
    print(solution(routes)) 
    