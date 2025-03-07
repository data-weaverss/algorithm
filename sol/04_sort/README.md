||문제|풀이|난이도|
|--|--|--|--|
|프로그래머스|[K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748)|[👉](./01_K번째수.py)|⭐️★|
|프로그래머스|[가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746)|[👉](./02_가장큰수.py)|⭐️⭐️★|
|프로그래머스|[H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747)|[👉](./03_H-Index.py)|⭐️⭐️★|
|백준|[덩치](https://www.acmicpc.net/problem/7568)|[👉](./04_덩치.py)|🩶|
|프로그래머스|[합이 0](https://www.acmicpc.net/problem/3151)|[👉](./05_합이0.py)|💛|




<br><br><br>
---
<br><br>

# 🔍 정렬(Sorting)

## 📌 파이썬의 기본 정렬 함수

Python에서는 기본적으로 `sorted()` 함수와 `list.sort()` 메서드를 제공한다.

### 🔹 `sorted()` 함수 (새로운 리스트 반환)
```python
arr = [3, 1, 4, 1, 5, 9, 2]
sorted_arr = sorted(arr)
print(sorted_arr)  # [1, 1, 2, 3, 4, 5, 9]

# 내림차순 정렬
desc_arr = sorted(arr, reverse=True)
print(desc_arr)  # [9, 5, 4, 3, 2, 1, 1]
```

✅ sorted()는 원본 리스트를 변경하지 않고 새로운 정렬된 리스트를 반환<br>
✅ 리스트의 원본을 유지하고, 정렬된 리스트를 새로운 변수로 받고 싶을 때<br>

### 🔹 list.sort() 메서드 (리스트 원본을 직접 변경)
```python
arr = [3, 1, 4, 1, 5, 9, 2]
arr.sort()  # 원본 리스트가 정렬됨
print(arr)  # [1, 1, 2, 3, 4, 5, 9]
```

### key를 활용한 정렬

```python
words = ["banana", "apple", "cherry"]
words.sort(key=len)  # 문자열 길이를 기준으로 정렬
print(words)  # ['apple', 'banana', 'cherry']
```

```python
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
people.sort(key=lambda x: x[1])  # 나이를 기준으로 정렬
print(people)  # [('Bob', 20), ('Alice', 25), ('Charlie', 30)]
```

✅ 리스트 자체를 정렬해야할 때(메모리 절약)<br>
✅ 불필요한 리스트 복사를 피해서 성능을 최적화하고 싶을 때


# 📌 정렬 알고리즘 종류 및 구현

| 정렬 알고리즘 | 시간복잡도 (평균) | 특징 |
|--------------|-----------------|------|
| **버블 정렬 (Bubble Sort)** | O(N²) | 인접한 원소를 비교하며 교환 |
| **선택 정렬 (Selection Sort)** | O(N²) | 최솟값을 찾아 앞으로 이동 |
| **삽입 정렬 (Insertion Sort)** | O(N²) | 앞에서부터 정렬된 부분을 확장 |
| **병합 정렬 (Merge Sort)** | O(N log N) | 분할 후 정렬하여 병합 |
| **퀵 정렬 (Quick Sort)** | O(N log N) | 피벗을 기준으로 정렬 |
| **힙 정렬 (Heap Sort)** | O(N log N) | 힙을 이용한 정렬 |
