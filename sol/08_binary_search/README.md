||문제|풀이|난이도|
|--|--|--|--|
|프로그래머스|[입국 심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238)|[👉](./01_입국심사.py)|⭐️⭐️⭐️|
<br><br><br>
---
<br><br>

# 이분탐색(binary search)

**정렬된 데이터**에서 특정 값을 효율적으로 찾기 위한 알고리즘 <br>
탐색 범위를 절반씩 줄여나가기 때문에 시간 복잡도가 O(logN)으로 매우 빠르다.

## 기본 개념
- 정렬된 배열에서만 사용할 수 있다.
- 탐색 범위를 좁혀가며 원하는 값을 찾는다.
- 반복문 또는 재귀를 활용하여 구현한다. 

## 이분 탐색의 동작 과정
1. 시작점(`start`)과 끝점(`end`) 설정
2. 중간점(`mid`)를 계산 
    - mid = (start + end) // 2
3. 중간점의 값과 목푯값을 비교
    - 목푯값이 중간점보다 작으면 end = mid - 1
    - 목푯값이 중간점보다 크면 start = mid + 1
    - 목푯값을 찾으면 탐색 종료
4. 위 과정을 반복하거나 재귀적으로 수행

## 이분 탐색 코드 템플릿

### 1️⃣ 반복문 방식

```python
def binary_search(array, target):
    start = 0 
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        # 목푯값이 중간값과 같다면 반환
        if array[mid] == target:
            return mid
        # 목푯값이 중간값보다 작다면 왼쪽으로 이동
        elif array[mid] > target:
            end = mid - 1
        # 목푯값이 중간값보다 크다면 오른쪽으로 이동
        else:
            start = mid + 1
```


### 2️⃣ 재귀 방식

```python
def binary_search_recursive(array, target, start, end):
    # 탐색 범위가 비어있다면 종료
    if start > end:
        return -1
    
    mid = (start + end) // 2

    # 목푯값이 중간값과 같다면 반환
    if array[mid] == target:
        return mid
    # 목푯값이 중간값보다 작다면 왼쪽으로 재귀 호출
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    # 목푯값이 중간값보다 크다면 오른쪽으로 재귀 호출
    else:
        return binary_search_recursive(array, target, mid + 1, end)
```

## Python의 `bisect` 모듈

Python 표준 라이브러리에는 이분 탐색을 쉽게 구현할 수 있는 `bisect` 모듈이 포함되어 있음

- `bisect_left(array, x)` : 리스트에서 x가 삽입될 가장 왼쪽 위치를 반환
- `bisect_right(array, x)` : 리스트에서 x가 삽입될 가장 오른쪽 위치를 반환

```python
from bisect import bisect_left, bisect_right

# 데이터와 타겟 값 설정
array = [1, 3, 5, 7, 9]
x = 5

# bisect_left: x가 삽입될 가장 왼쪽 위치 반환
left_index = bisect_left(array, x)

# bisect_right: x가 삽입될 가장 오른쪽 위치 반환
right_index = bisect_right(array, x)

print(f"Left Index: {left_index}, Right Index: {right_index}") # 2, 3
```


---

# 01_입국심사

| 단계 | start | end | mid | 처리 가능한 총 인원 (total_people) | 조건 (total_people >= n) | 탐색 방향 | 최소 시간 (min_time) |
|------|-------|-----|-----|-----------------------------------|--------------------------|-----------|----------------------|
| 1    | 1     | 16  | 8   | (8 // 1) + (8 // 2) = 8 + 4 = 12  | ✅ (12 >= 8)              | 왼쪽으로 탐색 (end = mid - 1) | 8                    |
| 2    | 1     | 7   | 4   | (4 // 1) + (4 // 2) = 4 + 2 = 6   | ❌ (6 < 8)               | 오른쪽으로 탐색 (start = mid + 1) | 8                    |
| 3    | 5     | 7   | 6   | (6 // 1) + (6 // 2) = 6 + 3 = 9   | ✅ (9 >= 8)              | 왼쪽으로 탐색 (end = mid - 1) | 6                    |
| 4    | 5     | 5   | 5   | (5 // 1) + (5 // 2) = 5 + 2 = 7   | ❌ (7 < 8)               | 오른쪽으로 탐색 (start = mid + 1) | 최종: **6**          |
