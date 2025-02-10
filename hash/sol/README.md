||문제|풀이|난이도|
|--|--|--|--|
|프로그래머스|[폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3)|[👉](./ponketmon.py)|⭐️★★|



<br><br><br>
---
# 🔍 해시 알고리즘 (Hash Algorithm)

데이터를 **효율적으로 검색(빠른 검색)** 하기 위한 자료구조인 **해시 테이블(Hash Table)** 을 기반으로 하며, 키-값 쌍(Key-Value Pair)을 저장하는 방식입니다.

- **해시 함수(Hash Function)** $h$에 키(key)를 입력하여 해시 값 $h(key)$을 생성합니다.
- 해시 값을 **인덱스**로 변환하여 데이터를 저장하거나 검색합니다.

---

## 📌 목차
1. [해시 테이블의 구조](#1)
2. [해시 함수 (Hash Function)](#2)
3. [충돌 해결 방법 (Collision Resolution)](#3)
   - 체이닝 (Chaining)
   - 개방 주소법 (Open Addressing)
4. [해시 테이블의 시간 복잡도](#4)
5. [해시 테이블의 공간 효율성](#5)
6. [파이썬의 `dict`는 미리 얼마나 공간을 할당할까?](#6)
7. [파이썬의 dict 문법](#7)

---

## [🔑 해시 테이블의 구조](#1)

해시 테이블은 **키(Key)를 해시 함수에 입력해 해시 값(Hash Value)**을 생성하고, 이 해시 값을 **배열의 인덱스**로 사용하여 데이터를 저장합니다.

|       Key         |       Hash Function       |       Index       |       Value       |
|-------------------|---------------------------|-------------------|-------------------|
|       "apple"     |       hash("apple")       |       1           |       "fruit"     |
|       "banana"    |       hash("banana")      |       2           |       "fruit"     |
|       "carrot"    |       hash("carrot")      |       3           |       "vegetable" |

---

## 🎯 [좋은 해시 함수 (Hash Function)](#2)

좋은 해시 함수는 다음과 같은 특성을 가집니다.

1. **빠른 계산 속도**: 해시 값 계산이 빠르게 이루어져야 합니다.
2. **균등한 분포**: 해시 값이 균등하게 분포되어 **충돌을 최소화**해야 합니다.
3. **결정적(Deterministic)**: 동일한 입력에 대해 항상 동일한 해시 값을 반환해야 합니다.

---

## [⚠ 충돌 해결 방법 (Collision Resolution)](#3)

해시 테이블에서 **두 개 이상의 키가 동일한 해시 값을 가질 때 발생하는 문제**를 **충돌(Collision)** 이라고 합니다.  
이를 해결하기 위한 대표적인 방법은 다음과 같습니다.

### 1️⃣ **체이닝 (Chaining)**
- 동일한 해시 값을 가지는 키를 <b>연결 리스트(Linked List) 또는 트리(Tree)</b>로 저장하는 방식입니다.
- 장점: 공간을 미리 많이 할당할 필요 없음.
- 단점: 충돌이 많아지면 검색 속도가 **O(n)** 으로 증가할 수 있음.

#### 🔹 체이닝 예시

```plaintext
Index 0: [ ("apple", "fruit") ]
Index 1: [ ("banana", "fruit"), ("carrot", "vegetable") ]
```

✅ **"carrot" 찾기 과정**
1. `hash("carrot")`를 계산하여 **인덱스 1**을 얻습니다.
2. 인덱스 1의 연결 리스트를 탐색합니다.
3. "banana"와 비교 → 일치하지 않음.
4. "carrot"과 비교 → **일치함을 확인하고 "vegetable" 반환**.

---

### 2️⃣ **개방 주소법 (Open Addressing)**
- 충돌이 발생하면 **다른 빈 인덱스를 찾아 저장**하는 방식입니다.
- 장점: 추가적인 연결 리스트 사용 없이 **메모리 절약 가능**.
- 단점: 충돌이 많아질수록 새로운 저장 공간을 찾는 과정이 느려질 수 있음.

#### 🔹 오픈 어드레싱 예시

```plaintext
Index 0: ("apple", "fruit")
Index 1: ("banana", "fruit")
Index 2: ("carrot", "vegetable")
```

> 파이썬의 `dict`는 **개방 주소법**을 사용합니다.(이차 탐사 사용)

✅ **"carrot" 찾기 과정**
1. `hash("carrot")`를 계산하여 **인덱스 2**를 얻습니다.
2. 인덱스 2의 키와 "carrot"을 비교 → **일치함을 확인하고 "vegetable" 반환**.

---


## [📌 해시 테이블의 시간 복잡도](#4)

||Hash Table|Linked List|Array|
|--|----------|-----------|-----|
|access|$O(1)$|$O(n)$|$O(1)$|
|insert|$O(1)$|$O(1)$|$O(n)$|
|append||$O(1)$|$O(n)$|
|delete|$O(1)$|$O(n)$|$O(n)$|

> 충돌로 인한 최악의 경우 $O(n)$
<br>

> 파이썬의 리스트(list)는 동적 배열이기 때문에, 공간이 부족하면 더 큰 크기의 배열을 생성하고 기존 원소를 복사하는 과정이 필요합니다.(append 시간 복잡도: $O(n)$)


---

## [💡 해시테이블의 공간 효율성](#5)

### 1️⃣ 미리 공간을 확보해야 한다 (Preallocated Space)
- 해시테이블은 데이터를 저장하기 전에 **미리 일정 크기의 배열(버킷, 슬롯)을 할당**해야 합니다.
- 데이터가 적게 저장되면 **사용되지 않는 빈 슬롯이 많아져 메모리 낭비**가 발생할 수 있습니다.
- 예를 들어, **로드 팩터(Load Factor) α = 저장된 원소 개수 / 버킷 크기** 가 낮으면 공간이 낭비됩니다.

### 2️⃣ 충돌(Collision)로 인한 추가적인 공간 사용
  - **체이닝(Chaining)**: 같은 인덱스에 여러 개의 데이터를 저장하기 위해 **연결 리스트나 트리를 추가로 사용** → **추가적인 포인터 공간 필요**.
  - **개방 주소법(Open Addressing)**: 충돌이 발생하면 **해시테이블 내 다른 빈 공간을 찾아 저장** → **버킷 크기를 더 크게 설정해야 함**.

### 3️⃣ 리사이징(Resizing)으로 인한 공간 낭비
- 해시테이블의 **로드 팩터가 일정 수준(보통 0.7~0.9)을 넘으면**, **테이블 크기를 2배로 확장(리사이징)** 합니다.
- 리사이징 후에는 **기존 크기의 절반 정도만 데이터가 채워져 있는 경우가 많아 메모리 낭비가 발생**합니다.

### 4️⃣ 사용되지 않는 슬롯이 많아질 가능성
- 개방 주소법을 사용하는 경우, 충돌이 많아지면 특정 키를 저장할 공간을 찾기 어려워집니다.
- 이를 해결하기 위해 **로드 팩터를 낮게 유지하려면 테이블 크기를 더 크게 설정해야 하며, 이는 공간 낭비를 초래**합니다.

---

## [🔍 파이썬의 `dict`는 미리 얼마나 공간을 할당할까?](#6)

파이썬의 해시테이블(`dict`)은 내부적으로 **해시 충돌을 해결하기 위해 미리 일정 크기의 슬롯을 할당**합니다. 

- 파이썬 `dict`의 기본적인 슬롯 개수(버킷 크기)는 **초기에 8개**로 시작합니다.
- 요소가 추가되면서 **로드 팩터가 2/3(약 0.67)을 초과하면 리사이징**이 발생하며, **2배 크기로 확장**됩니다.
- 즉, **넉넉한 슬롯을 미리 확보하여 해시 충돌을 줄이고 성능을 향상시키지만, 그만큼 공간 효율성은 떨어집니다.**

### 🛠️ 파이썬 딕셔너리의 기본 슬롯 크기 변화
| 원소 개수 | 버킷 크기 (슬롯 개수) |
|-----------|----------------|
| 0         | 8              |
| 5         | 8              |
| 6         | 16             |
| 11        | 16             |
| 12        | 32             |
| 22        | 32             |
| 23        | 64             |

- 예를 들어, **5개의 데이터를 저장할 때도 8개의 슬롯이 할당**되며, **12개를 저장할 때는 32개의 슬롯을 사용**하는 등 **실제 데이터보다 더 많은 공간을 차지**하게 됩니다.

---

## [📌 파이썬의 dict 문법](#7)

### ✅ 1. 딕셔너리 생성 방법

#### 1️⃣ 기본적인 `dict` 생성
```python
# 빈 딕셔너리 생성
my_dict = {}

# 키-값을 포함한 딕셔너리 생성
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

print(my_dict)  
# 출력: {'apple': 1, 'banana': 2, 'cherry': 3}
```

#### 2️⃣ `dict()` 생성자 사용
```python
my_dict = dict(apple=1, banana=2, cherry=3)  # 키를 변수처럼 사용 가능
print(my_dict)
# 출력: {'apple': 1, 'banana': 2, 'cherry': 3}

my_dict = dict([("apple", 1), ("banana", 2), ("cherry", 3)])  # 리스트 안의 튜플
print(my_dict)
# 출력: {'apple': 1, 'banana': 2, 'cherry': 3}
```

#### 3️⃣ `zip()`을 이용한 딕셔너리 생성
```python
keys = ["apple", "banana", "cherry"]
values = [1, 2, 3]

my_dict = dict(zip(keys, values))
print(my_dict)
# 출력: {'apple': 1, 'banana': 2, 'cherry': 3}
```

---

### ✅ 2. `dict` 요소 접근 및 수정

#### 1️⃣ 값 조회 (`dict[key]`)
```python
my_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(my_dict["apple"])  
# 출력: 1
```
⚠️ **주의:** 존재하지 않는 키를 조회하면 `KeyError` 발생!

#### 2️⃣ 안전한 조회 (`.get()`)
```python
print(my_dict.get("banana"))  
# 출력: 2

print(my_dict.get("grape"))  # 없는 키 조회 시 None 반환
# 출력: None

print(my_dict.get("grape", "Not Found"))  # 기본값 설정 가능
# 출력: Not Found
```

#### 3️⃣ 값 변경 및 추가
```python
my_dict["apple"] = 10
my_dict["grape"] = 5
print(my_dict)  
# 출력: {'apple': 10, 'banana': 2, 'cherry': 3, 'grape': 5}
```

---

### ✅ 3. `dict` 요소 삭제

#### 1️⃣ `del` 키워드 사용
```python
del my_dict["banana"]
print(my_dict)
# 출력: {'apple': 10, 'cherry': 3, 'grape': 5}
```

#### 2️⃣ `.pop()` 사용 (삭제 후 값 반환)
```python
value = my_dict.pop("apple")
print(value)  # 출력: 10
print(my_dict)  
# 출력: {'cherry': 3, 'grape': 5}
```

#### 3️⃣ `.popitem()` 사용 (마지막 요소 삭제)
```python
last_item = my_dict.popitem()
print(last_item)  # 출력: ('grape', 5)
print(my_dict)  
# 출력: {'cherry': 3}
```

---

### ✅ 4. `dict` 반복문 활용

#### 1️⃣ `for key in dict` → 키 순회
```python
for key in my_dict:
    print(key)
```

#### 2️⃣ `.items()` → 키-값 쌍 가져오기
```python
for key, value in my_dict.items():
    print(key, value)
```

---

### ✅ 5. `dict` 관련 메서드 정리

| 메서드 | 설명 |
|--------|------|
| `.get(key, default)` | 키가 존재하면 값 반환, 없으면 `default` 반환 |
| `.keys()` | 모든 키 반환 |
| `.values()` | 모든 값 반환 |
| `.items()` | `(key, value)` 튜플 반환 |
| `.update(other_dict)` | 다른 `dict` 병합 |
| `.pop(key, default)` | 키 삭제 후 값 반환 |
| `.popitem()` | 마지막 삽입된 요소 삭제 후 반환 |
| `.clear()` | 모든 요소 삭제 |

---

### ✅ 6. `dict`의 정렬

#### 1️⃣ 키를 기준으로 정렬
```python
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)
```

#### 2️⃣ 값을 기준으로 정렬
```python
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)
```

---

### ✅ 7. Python 3.7+에서 `dict`의 순서 유지

Python 3.7+부터 `dict`는 **삽입 순서를 유지**합니다.
```python
my_dict = {"b": 2, "a": 1, "c": 3}
print(my_dict)
# 출력: {'b': 2, 'a': 1, 'c': 3}  (입력 순서 유지)
```

---

---

### ✅ 8. `in` 연산자 사용 (딕셔너리 vs 리스트)

#### 1️⃣ `in` 연산자를 사용한 키 존재 여부 확인 (`dict`)
```python
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

print("apple" in my_dict)  # 출력: True
print("grape" in my_dict)  # 출력: False
```
- `dict`에서 `in` 연산자는 **키(key)가 존재하는지**를 확인하는 데 사용됩니다.
- **시간 복잡도: O(1) (해시 테이블 기반으로 빠름)**

#### 2️⃣ `in` 연산자를 사용한 요소 존재 여부 확인 (`list`)
```python
my_list = ["apple", "banana", "cherry"]

print("apple" in my_list)  # 출력: True
print("grape" in my_list)  # 출력: False
```
- `list`에서 `in` 연산자는 **해당 값이 리스트에 존재하는지**를 확인합니다.
- **시간 복잡도: O(n) (리스트는 선형 탐색을 수행하므로 느림)**

#### 🔍 `dict` vs `list`에서 `in` 연산자 성능 비교
| 자료구조 | `in` 연산자 시간 복잡도 | 설명 |
|----------|-----------------|------------------|
| `dict`   | O(1)             | 해시 테이블 기반, 빠름 |
| `list`   | O(n)             | 리스트를 처음부터 끝까지 탐색 |



<br><br><br>
---

## Reference
- [인프런 - 코딩테스트(ALL_IN_ONE)](https://www.inflearn.com/course/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%85%EB%AC%B8-%ED%8C%8C%EC%9D%B4%EC%8D%AC)