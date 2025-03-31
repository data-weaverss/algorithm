||문제|풀이|난이도|
|--|--|--|--|
|프로그래머스|[타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165)|[👉](./01_타겟넘버.py)|⭐️⭐️|
|프로그래머스|[네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)|[👉](./02_네트워크.py)|⭐️⭐️⭐️|
|프로그래머스|[게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844)|[👉](./03_게임맵최단거리.py)|⭐️⭐️|

<br><br><br>
---
<br><br>

# 그래프의 순회

## DFS

```python
def dfs(cur_node):
    visited[cur_node] = True
    for neighbor_node in graph[cur_node]:
        if neighbor_node not in visited:
            dfs(neighbor_node)
```

A 방문
- Stack: B C
- Visited: {A}
```plain
    A*
   / \
  B   C
 / \   \
D   E   F
```  

C 방문
- Stack: B F
- Visited: {A, C}
```plain
    A
   / \
  B   C*
 / \   \
D   E   F
```  

F 방문
- Stack: B 
- Visited: {A, C, F}
```plain
    A
   / \
  B   C
 / \   \
D   E   F*
```  

B 방문
- Stack: D E 
- Visited: {A, C, F, B}
```plain
    A
   / \
  B*  C
 / \   \
D   E   F
```  


## BFS

```python
from collections import deque

def bfs(graph, start):
    visited = dict()
    visited[start] = True
    queue = deque([start])
    while queue:
        cur_node = queue.popleft()
        if neighbor_node not in visited:
            visited[neighbor_node] = True
            queue.append(neighbor_node)
    return visited
```

- Queue: A
- Visited: {A}
```plain
    A
   / \
  B   C
 / \   \
D   E   F
```  

A를 방문
- Queue: B, C
- Visited: {A, B, C}
```plain
    A*
   / \
  B   C
 / \   \
D   E   F
```  

B를 방문
- Queue: C, D, E
- Visited: {A, B, C, D, E}
```plain
    A
   / \
  B*  C
 / \   \
D   E   F
```  

C를 방문
- Queue: D, E, F
- Visited: {A, B, C, D, E, F}
```plain
    A
   / \
  B   C*
 / \   \
D   E   F
```  

---

## DFS와 BFS 비교
- 시간복잡도: O(V + E) 
    - 모든 정점을 탐색하고 정점에 연결된 모든 간선을 확인하기 때문
- DFS는 스택에서 pop할 때 visited 처리, BFS는 큐에 넣을 때 visited 처리
- DFS는 깊이 우선 탐색, BFS는 너비 우선 탐색
    - DFS는 탐색 순서와 실제 방문 순서가 다르고, BFS는 탐색 순서와 실제 방문 순서가 동일




[참고](https://www.inflearn.com/course/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%85%EB%AC%B8-%ED%8C%8C%EC%9D%B4%EC%8D%AC)

---

