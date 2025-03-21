<!-- https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit -->
## 💡 탐욕 알고리즘 (Greedy Algorithm) 문제 목록

| 출처 | 문제 | 풀이 | 난이도 |
|--|--|--|--|
| 프로그래머스 | [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862) | [👉 코드 보기](./01_체육복.py) | ⭐️★★ |
| 프로그래머스 | [조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860) | [👉 코드 보기](./02_조이스틱.py) | ⭐️⭐️★ |
| 프로그래머스 | [큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883) | [👉 코드 보기](./03_큰수만들기.py) | ⭐️⭐️★ |
| 프로그래머스 | [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) | [👉 코드 보기](./04_구명보트.py) | ⭐️⭐️★ |
| 프로그래머스 | [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) | [👉 코드 보기](./05_섬연결하기.py) | ⭐️⭐️⭐️ |
| 프로그래머스 | [단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884) | [👉 코드 보기](./06_단속카메라.py) | ⭐️⭐️⭐️ |

---

## 📌 1. 탐욕 알고리즘이란?

**탐욕(Greedy) 알고리즘**은 최적해를 구하는 데 사용되는 근사적인 방법으로, **각 단계에서 가장 최적이라고 판단되는 선택을 하며 최종적인 해답에 도달하는 방식**이다.

### ✅ 특징
- **전략:** 현재 선택이 이후 선택에 영향을 미치지 않는 경우 탐욕적 선택을 수행할 수 있다.
- **단점:** 항상 최적해를 보장하지 않으며, 문제의 성질에 따라 실패할 수도 있다.
- **적용 가능 조건:**  
  1. **탐욕적 선택 조건(Greedy Choice Property)**  
     → 이전 선택이 이후 선택에 영향을 미치지 않아야 한다.  
  2. **최적 부분 구조 조건(Optimal Substructure)**  
     → 전체 문제의 최적해가 부분 문제의 최적해로 구성될 수 있어야 한다.

---

## 🔍 2. 문제 해결 접근 방식

탐욕 알고리즘을 적용할 때는 다음 절차를 따른다.

1️⃣ **선택 절차 (Selection Procedure)**  
   → 현재 상태에서 가장 최적의 해답을 선택한다.  

2️⃣ **적절성 검사 (Feasibility Check)**  
   → 선택된 해가 문제의 조건을 만족하는지 확인한다.  

3️⃣ **해답 검사 (Solution Check)**  
   → 원래 문제가 해결되었는지 검사하며, 해결되지 않았다면 다시 **선택 절차**로 돌아가 반복 수행한다.  

---
