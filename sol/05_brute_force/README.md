||문제|풀이|난이도|
|--|--|--|--|
|프로그래머스|[최소직사각형](https://school.programmers.co.kr/learn/courses/30/lessons/86491)|[👉](./01_최소직사각형.py)|⭐️★★|
|프로그래머스|[모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840)|[👉](./02_모의고사.py)|⭐️★★|
|프로그래머스|[소수찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839)|[👉](./03_소수찾기.py)|⭐️⭐️★|
|프로그래머스|[카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842)|[👉](./04_카펫.py)|⭐️⭐️★|

<br><br><br>
---
<br><br>

# 🔍 완전 탐색(Brute Force)

> 목차
> - [📌 완전 탐색이란?](#1)
> - [📌 주요 유형](#2)
>   - [1️⃣ 순열(Permutation)](#2-1)
>   - [2️⃣ 조합(Combination)](#2-2)
>   - [3️⃣ 중복 순열(Product)](#2-3)
>   - [4️⃣부분 집합(Subset)](#2-4)


## [📌 완전 탐색이란?](#1)
- 가능한 모든 경우의 수를 전부 탐색하여 정답을 찾는 방법
- 경우의 수가 많아질수록 시간 복잡도가 급격히 증가하여 비효율적이라는 단점이 있다. 

## [📌 주요 유형](#2)

### [1️⃣ 순열(Permutation)](#2-1)
- 서로 다른 n개의 원소 중 r개를 **순서 있게** 나열하는 방법

```python
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 2))  # 2개를 뽑아 순서 있게 나열
print(result)  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

```

### [2️⃣ 조합(Combination)](#2-2)
- 서로 다른 n개의 원소 중 r개를 **순서 없게** 나열하는 방법

```python
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))  # 2개를 뽑아 순서 없이 나열
print(result)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

### [3️⃣ 중복 순열(Product)](#2-3)
- n개의 원소에서 r개를 중복을 허용하여 나열하는 방법


```python
from itertools import product

data = ['A', 'B']
result = list(product(data, repeat=2))  # 중복을 허용하여 2개 선택
print(result)  # [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]

```

### [4️⃣ 부분 집합(Subset)](#2-4)
- 집합의 모든 부분 집합을 구하는 방법

```python
data = ['A', 'B']
n = len(data)

# 모든 부분 집합 생성
for i in range(1 << n):  # 1 << n은 2^n을 의미
    subset = []
    for j in range(n):
        if i & (1 << j):  # i의 j번째 비트가 켜져 있는지 확인
            subset.append(data[j])
    print(subset)
# 출력: [], ['A'], ['B'], ['A', 'B']
```

- 비트 마스킹을 이용하여 부분 집합을 구한다
- 집합의 크기가 n일 때, 부분 집합의 개수는 2^n개이다.(각 원소를 포함하거나 포함하지 않는 경우 2^n)


| 표현 | 이진수 결과 | 정수 값 |
|---|---|---|
| 1 << 0 | 0001 | 2^0 = 1 |
| 1 << 1 | 0010 | 2^1 = 2 |
| 1 << n | 1000...0000 | 2^n |

- 예시 코드 플로우

| i (Decimal) | i (Binary) | j=0 ('A') | j=1 ('B') | Subset       |
|-------------|------------|-----------|-----------|--------------|
| 0           | 00         | X         | X         | []           |
| 1           | 01         | O         | X         | ['A']        |
| 2           | 10         | X         | O         | ['B']        |
| 3           | 11         | O         | O         | ['A', 'B']   |

<br>

> 예를 들어, 리스트 `data = 'A', 'B'`에서 <br>
> `00` (이진수): 공집합 () <br>
> `01` (이진수): `'A'` <br>
> `10` (이진수): `'B'`<br>
> `11` (이진수): `'A', 'B'`
