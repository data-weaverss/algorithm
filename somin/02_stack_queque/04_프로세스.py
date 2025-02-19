# location 번째 프로세스가 몇 번째로 실행되는지 return 
from collections import deque

def solution(priorities, location):
    q = deque()
    # 큐 초기화 (index, priority) 리스트로 저장
    for idx, priority in enumerate(priorities):
        q.append([idx, priority])

    exe_order = 0 # 프로세스 실행 순서
    while q:
        idx, priority = q.popleft()    
        # 나머지 큐의 우선순위 중 가장 높은 우선순위를 찾는다  
        if q and priority < max(q, key=lambda x: x[1])[1]:
            q.append([idx, priority])
        else:
            exe_order += 1 
            # 알고 싶은 프로세스 인덱스 location과 
            # 실행된 프로세스의 idx와 일치하면 현재 실행순서 출력
            if idx == location:
                return exe_order
            

if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    sol = solution(priorities, location)
    print(sol)