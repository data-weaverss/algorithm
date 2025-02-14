# 입력: N(포켓몬 개수), M(문제 개수), 포켓몬 이름, 문제
# 출력: 문제에 대한 답
#      - 포켓몬 번호 > 포켓몬 이름 출력
#      - 포켓몬 이름 > 포켓몬 번호 출력
import sys

n, m = map(int, sys.stdin.readline().split())
# 포켓몬 이름 → 번호, 번호 → 이름 딕셔너리 생성
name_to_num = {}
num_to_name = {}

for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    name_to_num[name] = i
    num_to_name[i] = name

output = []
for _ in range(m):
    query = sys.stdin.readline().strip()
    if query.isdigit():  # 숫자 입력
        output.append(num_to_name[int(query)])
    else:  # 문자열 입력
        output.append(str(name_to_num[query]))

# 한 번에 출력하여 성능 개선
sys.stdout.write("\n".join(output) + "\n")