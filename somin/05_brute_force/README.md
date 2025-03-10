<!-- https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit -->
||문제|풀이|난이도|
|--|--|--|--|
|프로그래머스|[최소 직사각형](https://school.programmers.co.kr/learn/courses/30/lessons/86491)|[👉](./01_최소직사각형.py)|⭐️★★|
|프로그래머스|[모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840)|[👉](./02_모의고사.py)|⭐️★★|
|프로그래머스|[소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839)|[👉](./03_소수찾기.py)|⭐️⭐️★|
|프로그래머스|[카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842)|[👉](./04_카펫.py)|⭐️⭐️★|
|프로그래머스|[피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946)|[👉](./05_피로도.py)|⭐️⭐️★|
|프로그래머스|[전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971)|[👉](./06_전력망을둘로나누기.py)|⭐️⭐️★|
|프로그래머스|[모음사전](https://school.programmers.co.kr/learn/courses/30/lessons/84512)|[👉](./06_모음사전.py)|⭐️⭐️★|

## 📌 1. 개념 및 정의

### 🔹 완전 탐색란?

- 문제의 **모든 가능한 경우의 수**를 하나하나 검사하여 해를 찾는 방법입니다.
- 이 방법은 무식하게 한다는 의미로 'Brute Force'라고도 부르며, 직관적이여서 이해하기 쉽고 문제의 정확한 결과값을 얻어낼 수 있습니다. 
- 입력 크기가 작은 경우 적합하지만, 크기가 커질수록 비효율적일 수 있습니다.

---

## 🔍 2. 접근 방식

### 1️⃣ 단순 Brute-Force
- **반복문과 조건문을 이용해 모든 경우를 검사**하는 가장 기본적인 방법입니다.
- 예시: 4자리 비밀번호를 찾을 때 `0000~9999`까지 모든 조합을 시도

### 4️⃣ 순열(Permutation)
- **순서를 고려하여 여러 개의 원소를 나열**하는 방법입니다.
- Python의 `itertools.permutations()`을 활용하면 쉽게 구현할 수 있습니다.
```python
from itertools import permutations
arr = [1, 2, 3]
print(list(permutations(arr)))  # 모든 순열 출력
```

### 3️⃣ 재귀(Recursion)
- **자기 자신을 호출하여 경우의 수를 탐색**하는 방식입니다.
- DFS(깊이 우선 탐색)와 유사하며, 상태를 변화시키면서 모든 경로를 탐색합니다.
```python 
def dfs(path, visited):
    if len(path) == len(arr):
        print(path)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            dfs(path + [arr[i]], visited)
            visited[i] = False

arr = [1, 2, 3]
dfs([], [False] * len(arr))
```

### 4️⃣ BFS/DFS(너비/깊이 우선 탐색)
- 그래프 탐색에서 모든 경우를 찾기 위해 활용됩니다.
- **DFS**는 깊이 있는 탐색을 수행하며, **BFS**는 너비 우선 탐색을 수행합니다.
```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
bfs(1)  # 1 2 3 4 5 6
```

---

## 📊 3. 시간 및 공간 복잡도 분석

### 🔹 일반적인 시간 복잡도
- 경우의 수가 많아질수록 탐색 시간이 기하급수적으로 증가합니다.
- 순열: O(n!)
- 부분 집합 탐색: O(2^n)
- 반복문 기반 탐색: O(n^2) 또는 O(n^3)

### 🔹 주요 특징
- **입력 크기가 작다면 최적의 해법**이며, 구현이 직관적입니다.
- **입력 크기가 크면 백트래킹, DP, 분할 정복 등의 최적화가 필요**합니다.

---

## ✅ 4. 장점과 단점

### 🔹 장점
✔ 직관적이고 쉬운 구현 <br/>
✔ 항상 정확한 해를 보장 <br/>
✔ 모든 문제 유형에 적용 가능

### 🔹 단점
❌ **비효율적**: 시간 복잡도가 크고 실행 속도가 느림 <br/>
❌ **메모리 사용 증가**: 탐색 과정에서 많은 상태를 저장해야 하는 경우 메모리 사용량이 증가할 수 있습니다.

---

## 🔥 5. 활용 예시

### 🔹 문제 예시
✅ 부분 집합 합 문제 <br/>
✅ 순열 및 조합 문제 <br/>
✅ N-Queen 문제 (백트래킹과 결합) <br/>
✅ 최단 경로 문제 (BFS 활용) <br/>

### 🔹 코딩 테스트에서의 역할
- **문제의 크기가 작을 때** 기본적인 해결 방법으로 사용됩니다.
- **백트래킹, 동적 계획법 등의 최적화 기법과 함께 사용**하여 더 효율적인 알고리즘을 도출할 수 있습니다.

---

## 📖 6. 요약 및 핵심 정리

| 개념 | 설명 |
| --- | --- |
| **완전 탐색(Brute Force)** | 가능한 모든 해를 탐색하는 기법 |
| **주요 접근 방식** | Brute-Force, 비트마스크, 재귀, 순열, BFS/DFS |
| **시간 복잡도** | O(n!), O(2^n) 등 기하급수적으로 증가 |
| **활용 예시** | 부분 집합 문제, 순열, 조합, N-Queen, BFS/DFS 탐색 문제 |
| **장점** | 단순하고 직관적이며, 정확한 답을 보장 |
| **단점** | 경우의 수가 많아질수록 비효율적이며, 최적화 필요 |

완전 탐색은 **가장 기본적인 탐색 기법**으로, 문제의 규모를 고려하여 적절하게 활용해야 합니다. 입력 크기가 작을 때는 효과적인 방법이지만, 크기가 클 경우 최적화 기법과 함께 사용해야 합니다.

