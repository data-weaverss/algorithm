||문제|풀이|난이도|
|--|--|--|--|
|프로그래머스|[더 맵게](https://school.programmers.co.kr/learn/courses/30/parts/12117)|[👉](./01_더맵게.py)|⭐️⭐️★|
|프로그래머스|[디스크 컨트롤러](https://school.programmers.co.kr/learn/courses/30/lessons/42627)|[👉](./02_디스크컨트롤러.py)|⭐️⭐️⭐️|
|프로그래머스|[이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628)|[👉](./03_이중우선순위큐.py)|⭐️⭐️⭐️|

<br><br><br>
---
<br><br>

# 🔍 힙(Heap)

## 📌 목차
1. [Heap이란?](#1)
2. [파이썬에서의 Heap 구조](#2)
3. [파이썬에서 Heap 사용법](#3)
4. [Heap의 시간복잡도](#4)

## [📌 Heap이란?](#1)
Heap은 우선순위 큐(Priority Queue)를 구현하는 데 사용되는 자료구조

## [📌 파이썬에서의 Heap 구조](#2)
파이썬의 `heapq` 모듈은 **완전 이진 트리**를 리스트로 표현하는 방식으로 동작
명시적인 트리 구조가 아닌 **배열 기반의 이진 힙**을 사용하여 힙 연산을 수행
 
예제 힙 구조:
```
        1
      /   \
     3     5
    / \   / \
   7   9 6   8 
```
배열로 표현하면:
```python
heap_arr = [1, 3, 5, 7, 9, 6, 8]
```
이처럼 파이썬에서는 **리스트의 인덱스를 이용하여 이진 힙 구조를 유지**

> ⚠️ Min Heap의 특성
>- `heapq` 모듈을 사용하여 **min heap**을 만들었을 때, `heap_arr[0]`은 항상 최솟값을 보장
>- 하지만 그 이후의 원소 순서는 정렬된 상태가 아님. 즉, `heap_arr[1]`이 두 번째로 작은 값이라고 보장할 수 없음. 그 이유는 **heap은 왼쪽 자식 노드와 오른쪽 자식 노드의 크기를 비교하지 않기 때문**



## [📌 파이썬에서 Heap 사용법](#3)

### 📚 `heapq` 모듈 사용
```python
from heapq import heappush, heappop, heappush
```

### 📌 리스트를 힙으로 변환 - heapify
```python
from heapq import heapify

arr = [3, 1, 4, 1, 5, 9, 2]
heapify(arr)
print(arr)  # [1, 1, 2, 3, 5, 9, 4]
```

### 📌 최소 힙
```python
min_heap = []
heappush(min_heap, 3)
heappush(min_heap, 1)
heappush(min_heap, 4)
heappush(min_heap, 2)

print(heappop(min_heap))  # 1
print(heappop(min_heap))  # 2
```

### 📌 최대 힙
```python
# 최대 힙
max_heap = []
heappush(max_heap, -3)
heappush(max_heap, -1)
heappush(max_heap, -4)
heappush(max_heap, -2)

print(-heappop(max_heap))  # 4
print(-heappop(max_heap))  # 3
```

## [⏳ Heap의 시간복잡도](#4)

| 연산        | 평균 시간복잡도 | 설명 |
|------------|--------------|------|
| `heappush` | O(log N)    | 요소 추가 |
| `heappop`  | O(log N)    | 최댓값/최솟값 제거 |
| `heapify`  | O(N)        | 리스트를 힙으로 변환 |
