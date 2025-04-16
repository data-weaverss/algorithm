||문제|풀이|난이도|
|--|--|--|--|
|프로그래머스|[가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189)|[👉](./01_가장먼노드.py)|⭐️⭐️⭐️|
|프로그래머스|[순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191)|[👉](./02_순위.py)|⭐️⭐️⭐️|
|백준|[최소 스패닝 트리](https://www.acmicpc.net/problem/1197)|[👉](./03_최소스패닝트리.py)|💛💛💛💛|
|백준|[ACM Craft](https://www.acmicpc.net/problem/1005)|[👉](./04_ACMCraft.py)|💛💛💛|
|프로그래머스|[방의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/49190)|[👉](./03_방의개수.py)|⭐️⭐️⭐️⭐️⭐️|




<br><br><br>
---
<br><br>

# 그래프(graph)

**노드(Node)**와 간선(Edge)**로 구성된 자료구조

## 그래프의 구현 방법
### 1. 인접 행렬(Adjacency Matrix)
- 특징: 2차원 배열로 그래프를 표현
- 장점: 특징 노드 간의 간선 비용을 O(1) 시간에 조회 가능
- 단점: 메모리 사용량이 O(V^2)로 비효율적
    - 노드 수가 적을 때 많이 사용

```python  
# 인접 행렬 구현
INF = float('inf')  # 무한대 값 설정
graph = [
    [0, 7, INF, INF],
    [7, 0, 5, INF],
    [INF, 5, 0, 2],
    [INF, INF, 2, 0]
]
```

### 2. 인접 리스트(Adjacency List)
- 특징: 각 노드에 연결된 노드 정보를 딕셔너리 `{}`로 표현
    - key에는 정점들이 들어가며, value에는 list 형태로 연결 관계 표시
- 장점: 메모리 사용량이 O(E)로 효율적

```python
# 인접 리스트 구현
graph = [[] for _ in range(4)]
graph[0].append((1, 7))  # 노드 0에서 노드 1로 가는 비용이 7
graph[1].append((0, 7))
graph[1].append((2, 5))
graph[2].append((1, 5))
graph[2].append((3, 2))
graph[3].append((2, 2))
```

## 주요 알고리즘

|알고리즘|설명|
|----|----|
|다익스트라|한 지점 -> 모든 지점 최단 거리(양의 간선)|
|플로이드-워셜|모든 지점 -> 모든 지점 최단 거리|
|크루스칼|최소 신장트리(MST), 간선 정렬 + Union-Find|
|위상 정렬|방향 그래프에서 순서 정하기(진입 차수)|
|벨만포드|음의 간선 허용, 최단 거리 + 사이클 탐지|


### 1️⃣ 다익스트라

** 최단 거리 테이블을 조금씩 갱신하며 완성해내가는 그리디 알고리즘**

- 한 지점에서 다른 지점으로 가는 최단 거리를 구하는 알고리즘
- 음의 간선이 없을 때 사용 가능

```python
import heapq

def dijkstra(start, graph, n):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for nxt, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
    return distance
```

#### 시각화

```plain
        (2)
     1 ----- 2
     |     / |
   (5)  (1)  (3)
     | /     |
     3 ----- 4
       (2)
```
- 노드: 1~4
- 간선: (1-2, 2), (1-3, 5), (2-3, 1), (2-4, 3), (3-4, 2)

🟢 초기 상태
- distance: [inf, 0, inf, inf, inf]
- pq: [(0, 1)]

▶ 1단계: 1번 노드 방문
- 인접한 간선들:
    - (1→2, 2) → 거리 2 → 업데이트!
    - (1→3, 5) → 거리 5 → 업데이트!
- distance: [inf, 0, 2, 5, inf]
- pq: [(2, 2), (5, 3)]


▶ 2단계: 2번 노드 방문(거리 2)
- 인접한 간선들:
    - (2→3, 1) → 현재 거리 = 2+1 = 3 → 기존 5보다 작다! 업데이트!
    - (2→4, 3) → 2+3 = 5 → 업데이트!
- distance: [inf, 0, 2, 3, 5]
- pq: [(3, 3), (5, 3), (5, 4)]

▶ 3단계: 3번 노드 방문(거리 3)
- 인접한 간선들:
    - (3→4, 2) → 3+2 = 5 → 기존 5와 같음 → 업데이트 X
- distance: [inf, 0, 2, 3, 5]
- pq: [(5, 3), (5, 4)]

▶ 4단계: 3번 노드 재방문 -> 이미 짧은 거리로 방문했으므로 무시
- pq: [(5, 4)]

▶ 5단계: 4번 노드 방문(거리 5) -> 인접 노드 없음 -> 끝

---

### 2️⃣ 플로이드-워셜(Floyd-Warshall)

모든 노드 쌍 사이의 최단 거리를 구하는 알고리즘 
- 다익스트라는 1개 정점 기준, 플로이드는 전체 정점 쌍 기준
- 음의 간선은 허용되지만, 음의 사이클은 안됨
- 노드 수가 작을 때 사용(n <= 100 정도)
- O(N^3) 시간 복잡도

```python
def floyd_warshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
```

```plain
입력 간선:
1 → 2 (4)
1 → 3 (2)
2 → 3 (5)
3 → 4 (7)
2 → 4 (1)

목표: 모든 정점 간 최단 거리

[초기]
    1   2   3   4
1 [ 0   4   2  ∞ ]
2 [ ∞  0   5   1 ]
3 [ ∞  ∞  0   7 ]
4 [ ∞  ∞  ∞   0 ]

k=2일 때, 1→2→4 = 4+1 = 5 → 1→4 거리 갱신
```

---

### 3️⃣ 크루스칼

모든 노드를 연결하면서 간선의 비용이 가장 작도록 하는 MST 알고리즘
- 간선을 비용 기준으로 정렬 후, 사이클이 생기지 않도록 선택
- 사이클 판별은 유니온 파인드를 활용함

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def kruskal(n, edges):
    parent = [i for i in range(n + 1)]
    edges.sort()
    total = 0

    for cost, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total += cost

    return total
```

```plain
입력 간선 (비용):
1 - 2 (1)
2 - 3 (2)
1 - 3 (3)

간선 정렬:
(1, 1-2), (2, 2-3), (3, 1-3)

→ 1-2 선택 → 2-3 선택 → 1-3은 사이클 생기므로 제외
```

---

### 4️⃣ 위상 정렬(Topological Sort)

순서가 정해진 작업을 수행할 때 사용되는 알고리즘
- 방향 그래프에서만 가능
- 진입 차수가 0인 노드부터 순차적으로 처리

```python
from collections import deque

def topology_sort(n, graph, indegree):
    result = []
    queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])

    while queue:
        now = queue.popleft()
        result.append(now)
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return result
```

```plain
과목 관계:
1 → 2
1 → 3
3 → 4

가능한 수강 순서:
1 → 2 → 3 → 4
or
1 → 3 → 2 → 4

진입 차수:
1: 0
2: 1
3: 1
4: 2

→ 진입차수 0인 노드부터 꺼내며 처리
```

---

### 5️⃣ 벨만-포드 (Bellman-Ford)

음의 간선을 포함한 그래프에서 최단 거리 계산
- 다익스트라는 음의 간선 X -> 이럴 땐 벨만-포드 사용
- 음수 사이클이 존재하는지도 확인할 수 있음

```python
def bellman_ford(n, edges, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    for i in range(n - 1):
        for u, v, cost in edges:
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost

    # 음수 사이클 확인
    for u, v, cost in edges:
        if dist[u] + cost < dist[v]:
            return None  # 음수 사이클 있음

    return dist
```

```plain
간선:
1 → 2 (4)
2 → 3 (-5)
3 → 1 (1)

→ 음수 사이클 존재 (1 → 2 → 3 → 1 순환하며 계속 감소)

→ 벨만포드는 N-1번 반복 후 N번째에 값이 바뀌면 음수 사이클로 판단
```