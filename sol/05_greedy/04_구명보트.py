from collections import deque

def solution(people, limit):
    """
    - 구명보트: 한 번에 최대 2명씩밖에 탈 수 없음. 무게 제한도 있음
    Args:
        - people: 사람들의 몸무게를 담은 배열
        - limit: 구명보트의 최대 무게 제한
    Return:
        - 필요한 구명보트의 최소 개수    
    """
    people.sort() # 오름차순 정렬
    people_q = deque(people)
    answer = 0 
    
    while people_q:
        heavy = people_q.pop()
        answer += 1
        if people_q and heavy + people_q[0] <= limit:
            people_q.popleft()    
            
    return answer


if __name__ == "__main__":
    people = [70, 50, 80, 50]
    limit = 100
    print(solution(people, limit)) # 3
    