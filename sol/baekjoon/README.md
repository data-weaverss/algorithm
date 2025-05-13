|문제|풀이|난이도|푼 방식|
|--|--|--|----|
|[사탕 게임](https://www.acmicpc.net/problem/3085)|[👉](./01_사탕게임.py)|🩶🩶|완전 탐색|
|[리모컨](https://www.acmicpc.net/problem/1107)|[👉](./02_리모컨.py)|💛💛💛💛|완전 탐색, 중복 순열|
|[수 이어 쓰기 1](https://www.acmicpc.net/problem/1748)|[👉](./03_수이어쓰기1.py)|🩶🩶🩶🩶|수학, 구현|
|[카잉 달력](https://www.acmicpc.net/problem/6064)|[👉](./04_카잉달력.py)|🩶|수학|
|[테트로미노](https://www.acmicpc.net/problem/14500)|[👉](./05_테트로미노.py)|💛💛💛💛|구현|
|[연산자 끼워넣기](https://www.acmicpc.net/problem/14888)|[👉](./06_연산자_끼워넣기.py)|🩶|재귀, 완전 탐색|
|[괄호의 값](https://www.acmicpc.net/problem/2504)|[👉](./07_괄호의값.py)|💛💛💛💛💛|스택|
|[빗물](https://www.acmicpc.net/problem/14719)|[👉](./08_빗물.py)|💛💛💛💛💛|구현|
|[가르침](https://www.acmicpc.net/problem/1062)|[👉](./09_가르침.py)|💛💛💛💛|완전 탐색, 비트마스크|
|[멀티탭 스케줄링](https://www.acmicpc.net/problem/1700)|[👉](./10_멀티탭스케줄링.py)|💛|그리디|
|[부분합](https://www.acmicpc.net/problem/1806)|[👉](./11_부분합.py)|💛💛💛💛|큐|
|[최소비용 구하기](https://www.acmicpc.net/problem/1916)|[👉](./12_최소비용구하기-다익스트라.py)|💛💛💛💛💛|다익스트라, 벨만포드|
|[부분 문자열](https://www.acmicpc.net/problem/16916)|[👉](./13_부분문자열.py)|🤎|문자열 in|
|[줄 세우기](https://www.acmicpc.net/problem/2252)|[👉](./14_줄세우기.py)|💛💛💛|위상정렬|
|[iSharp](https://www.acmicpc.net/problem/3568)|[👉](./15_isharp.py)|🩶🩶🩶|스택, 구현|

<br><br><br>

--- 

# 가르침 문제 - 비트 마스크
- 집합을 효율적으로 다룰 수 있음(특히 부분집합 확인 문제)
- set의 in 연산, add, remove는 O(1)이지만, 차집합, 합집합, 교집합은 두 set 크기에 비례하는 O(len) 시간이 걸림

```python
mask = sum(1 << (ord(c) - ord('a')) for c in combo)
```
-> 알파벳 문자를 비트 마스크로 변환하는 코드
각 문자를 2진수 비트 위치로 매핑해 집합을 표현

1. ord(c) - ord('a') 
    -  문자 -> 비트 위치 계산
    - 예: c = 2(3번째 알파벳)
2. 비트 시프트 연산
- 1 << (위치)
    - 해당 위치에 1을 배치
    - 예: `c` -> `1 << 2` -> `4` (이진수 100)
3. 비트 합산
    - `sum()`으로 모든 문자에 대한 비트를 합침
    - 예: `combo= a, c` -> `1(0001) + 4(0100) = 5(0101)`
