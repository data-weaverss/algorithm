||문제|풀이|난이도|
|--|--|--|--|
|프로그래머스|[입국 심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238)|[👉](./01_입국심사.py)|⭐️⭐️⭐️|
|프로그래머스|[징검다리](https://school.programmers.co.kr/learn/courses/30/lessons/43236)|[👉](./02_징검다리.py)|⭐️⭐️⭐️⭐️|
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

<br><br>

# 01_입국심사

| 단계 | start | end | mid | 처리 가능한 총 인원 (total_people) | 조건 (total_people >= n) | 탐색 방향 | 최소 시간 (min_time) |
|------|-------|-----|-----|-----------------------------------|--------------------------|-----------|----------------------|
| 1    | 1     | 16  | 8   | (8 // 1) + (8 // 2) = 8 + 4 = 12  | ✅ (12 >= 8)              | 왼쪽으로 탐색 (end = mid - 1) | 8                    |
| 2    | 1     | 7   | 4   | (4 // 1) + (4 // 2) = 4 + 2 = 6   | ❌ (6 < 8)               | 오른쪽으로 탐색 (start = mid + 1) | 8                    |
| 3    | 5     | 7   | 6   | (6 // 1) + (6 // 2) = 6 + 3 = 9   | ✅ (9 >= 8)              | 왼쪽으로 탐색 (end = mid - 1) | 6                    |
| 4    | 5     | 5   | 5   | (5 // 1) + (5 // 2) = 5 + 2 = 7   | ❌ (7 < 8)               | 오른쪽으로 탐색 (start = mid + 1) | 최종: **6**          |


---

# 02_징검다리

> 💡 핵심 아이디어
> 최솟값 중 최댓값을 구하라는 건 **이분 탐색으로 최솟값을 조정"하면서 가능한지를 판단해야한다는 뜻

## 풀이흐름

```plain
1. rocks에 도착점(distance)을 추가한 뒤 오름차순 정렬

2. 이분 탐색 범위 설정
   left = 0
   right = distance

3. mid = (left + right) // 2
   → 최소 거리로 가정하고 확인 시작

4. rocks 순회하면서 현재 위치(current)와의 거리 체크
   → mid보다 짧으면 해당 rock 제거 (count += 1)

5. 제거한 바위 수가 n 이하이면 mid 거리 유지 가능 → answer = mid, left = mid + 1
   제거한 바위 수가 n 초과이면 mid 거리 유지 불가 → right = mid - 1
```

```plain
정렬된 바위 위치
[0] → [2] → [11] → [14] → [17] → [21] → [25]

1) mid = 12
- 거리 기준: 최소 간격 12 이상 유지해야 함
- 거리 계산:
    2 - 0   = 2     → 제거
    11 - 0  = 11    → 제거
    14 - 0  = 14    → 유지
    17 - 14 = 3     → 제거
    21 - 14 = 7     → 제거
    25 - 14 = 11    → 제거
→ 총 제거 바위 수 = 5 > n ❌
→ right = 11 로 줄임

2) mid = 5
- 거리 기준: 최소 간격 5 이상 유지
- 거리 계산:
    2 - 0   = 2     → 제거
    11 - 0 = 11     → 유지 (current = 11)
    14 - 11 = 3     → 제거
    17 - 11 = 6     → 유지 (current = 17)
    21 - 17 = 4     → 제거
    25 - 17 = 8     → 유지
→ 제거 수 = 3 > n ❌
→ right = 5

3) mid = 3
- 거리 기준: 3 이상이면 통과
- 거리 계산:
    2 - 0   = 2     → 제거
    11 - 0  = 11    → 유지 (current = 11)
    14 - 11 = 3     → 유지 (current = 14)
    17 - 14 = 3     → 유지 (current = 17)
    21 - 17 = 4     → 유지 (current = 21)
    25 - 21 = 4     → 유지
→ 제거 수 = 1 ≤ n ✅
→ answer = 3
→ left = 4

4) mid = 4
- 거리 기준: 4 이상
- 거리 계산:
    2 - 0   = 2     → 제거
    11 - 0  = 11    → 유지 (current = 11)
    14 - 11 = 3     → 제거
    17 - 11 = 6     → 유지 (current = 17)
    21 - 17 = 4     → 유지 (current = 21)
    25 - 21 = 4     → 유지
→ 제거 수 = 2 ≤ n ✅
→ answer = 4
→ left = 5
```