||문제|풀이|난이도|
|--|--|--|--|
|프로그래머스|[타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165)|[👉](./01_타겟넘버.py)|⭐️⭐️|
|프로그래머스|[네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)|[👉](./02_네트워크.py)|⭐️⭐️⭐️|
|프로그래머스|[게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844)|[👉](./03_게임맵최단거리.py)|⭐️⭐️|
|프로그래머스|[단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163)|[👉](./04_단어변환.py)|⭐️⭐️⭐️|
|프로그래머스|[아이템 줍기](https://school.programmers.co.kr/learn/courses/30/lessons/87694)|[👉](./05_아이템줍기.py)|⭐️⭐️⭐️|
|프로그래머스|[여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164)|[👉](./06_여행경로.py)|⭐️⭐️⭐️|
|프로그래머스|[퍼즐 조각 채우기](https://school.programmers.co.kr/learn/courses/30/lessons/84021)|[👉](./07_퍼즐조각채우기.py)|⭐️⭐️⭐️|

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

# 05_아이템 줍기

![alt text](./image/05_아이템줍기.jpeg)

---

# 06_퍼즐 조각 채우기
## 배열 회전하기

배열을 왼쪽으로 회전
```plain

1 1 0     0 1    1 1 0     0 1                 
0 1 1 ⬅️  1 1 ⬅️ 0 1 1 ⬅️  1 1  
          1 0              1 0                 
map_3    map_2   map_1     map 
```

```python
map = [[0, 1], [1, 1], [1, 1]]
print(map) # [[0, 1], [1, 1], [1, 0]]
map_1 = [list(x) for x in zip(*map)][::-1]
print(map_1) # [[1, 1, 0], [0, 1, 1]]
map_2 = [list(x) for x in zip(*map_1)][::-1]
print(map_2) # [[0, 1], [1, 1], [1, 0]]
map_3 = [list(x) for x in zip(*map_2)][::-1]
print(map_3) # [[1, 1, 0], [0, 1, 1]]
```

## 처음 푼 방식 -> 수정 방식
![alt text](./image/07_퍼즐조각채우기.jpeg)

코드 25번째 줄에서 
```python
origin_puzzle = [row[col1:col2+1] for row in map[row1:row2+1]]
```

퍼즐을 표현하려면 퍼즐이 아닌곳에 0을 채워넣어 직사각형으로 만들어야함. 직사각형으로 추출하면서 같은 퍼즐이 아닌 1(map[2][2])도 같이 직사각형에 넣는바람에 최종적으로 같은 값이 아니다 라는 결과를 내게 됨.

->
DFS로 찾은 같은 퍼즐(same parent) 외 패딩 값들은 모두 0으로 설정해줘야함.

```python
puzzle = [[0] * (col2 - col1 + 1) for _ in range(row2 - row1 + 1)]
for row, col in routes:
    puzzle[row - row1][col - col1] = 1
    map[row][col] = 0
return puzzle
```