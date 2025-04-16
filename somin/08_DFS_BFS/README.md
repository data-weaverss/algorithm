<!-- https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit -->
## 💡 DFS/BFS 문제 목록

| 출처 | 문제 | 풀이 | 난이도 |
|--|--|--|--|
| 프로그래머스 | [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) | [👉 코드 보기](./01_타겟넘버.py) | ⭐️⭐️★ |
| 프로그래머스 | [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) | [👉 코드 보기](./02_네트워크.py) | ⭐️⭐️⭐️ |
| 프로그래머스 | [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) | [👉 코드 보기](./03_게임맵최단거리.py) | ⭐️⭐️★ |
| 프로그래머스 | [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163) | [👉 코드 보기](./04_단어변환.py) | ⭐️⭐️⭐️ |
| 프로그래머스 | [아이템 줍기](https://school.programmers.co.kr/learn/courses/30/lessons/87694) | [👉 코드 보기](./05_아이템줍기.py) | ⭐️⭐️⭐️ |
| 프로그래머스 | [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164) | [👉 코드 보기](./06_여행경로.py) | ⭐️⭐️⭐️ |
| 프로그래머스 | [퍼즐 조각 채우기](https://school.programmers.co.kr/learn/courses/30/lessons/84021) | [👉 코드 보기](./07_퍼즐조각채우기.py) | ⭐️⭐️⭐️ |

---

## 📌 1. 깊이 우선 탐색 (DFS, Depth-Fisrt Search)이란?

트리(Tree)나 그래프(Graph) 구조에서 한 방향으로 끝까지 깊게 들어갔다가, 더 이상 갈  곳이 없으면 다시 되돌아와 다른 방향을 탐색하는 방식입니다. </br>
즉, 분기(Branch)를 완전히 탐색하고 나서 다음 분기로 이동합니다. 

> 구현 방법: **스택(Stack)** 또은 **재귀함수**

### 주요 특징
- 백트래킹 문제, 조합/순열 문제에 자주 사용
- 경로 탐색, 가능한 모든 경우 탐색에 효과적


## 동작 방식 및 시각화

1. 현재 노드를 방문 처리
2. 방문하지 않은 각 인접 노드로 이동 (재귀 호출 or 스택 추가)
3. 더이상 이동할 노드가 없으면 이전 노드로 되돌아감
4. 모든 노드를 방문할 때까지 반복

![alt text](img/Depth-First-Search.gif)


---

## DFS 구현 예시

### 재귀 DFS
```python 
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# 예시 그래프 (인접 리스트)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}
visited = [False] * 6
dfs(graph, 1, visited)
```

### 스택을 이용한 반복 DFS:

```python
def iterative_dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))  # 방문 순서 조정
```

---

## 📌 2. 너비 우선 탐색 (BFS, Breadth-Fisrt Search)이란?

그래프나 트리에서 가까운 노드부터 차례대로 탐색하는 알고리즘입니다.</br>
시작 노드에서 인접한 모든 노드를 탐색한 후, 그 다음 레벨의 노드를 탐색합니다.

> 구현 방법: **큐(Queue)**


## BFS 동작 방식 및 시각화
1. 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 인접 노드를 모두 큐에 삽입
3. 큐가 빌 때까지 반복

![alt text](img/Breadth-First-Search.gif)

---

## BFS 구현 방식

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

```

---
## 🧠 3. 핵심 요약 비교

| 항목 | DFS (깊이 우선 탐색) | BFS (너비 우선 탐색) |
|------|--------------------|---------------------|
| 방식 | 한 분기 끝까지 탐색 후 백트래킹 | 가까운 노드부터 레벨 순서대로 탐색 |
| 자료구조 | 스택 or 재귀 | 큐 |
| 주요 용도 | 백트래킹, 모든 경로 탐색 | 최단 거리 탐색 |
| 구현 난이도 | 간단 (재귀 활용) | 큐 자료구조 필요 |
| 시간복잡도 | 인접 리스트: `O(V + E)` </br> 인접행렬: `O(V²)`  | 인접 리스트: `O(V + E)` </br>인접행렬: `O(V²)` |
| 단점 | 해가 깊은 곳에 있을 때 비효율 | 메모리 사용량 많아질 수 있음 |