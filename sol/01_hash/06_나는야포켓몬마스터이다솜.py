import sys


def solution(pocketmons, problems):
    """
    - 포켓몬이름을 입력하면 포켓몬번호 반환
    - 포켓몬번호를 입력하면 포켓몬이름 반환
    """

    # name_to_id[포켓몬 이름] = 포켓몬 번호
    name_to_id = {}
    # id_to_name[포켓몬 번호] = 포켓몬 이름
    id_to_name = {}

    for pocketmon_id, pocketmon_name in enumerate(pocketmons, start=1):
        name_to_id[pocketmon_name] = pocketmon_id
        id_to_name[str(pocketmon_id)] = pocketmon_name

    for query in queries:
        if query.isdigit():  # 숫자(포켓몬 번호) 입력 시
            print(id_to_name[query])
        else:
            print(name_to_id[query])


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())

    pocketmons = [input().rstrip() for _ in range(N)]
    queries = [input().rstrip() for _ in range(M)]

    solution(pocketmons, queries)
