def solution(citations):
    """
    - param citations: 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열

    - 어느 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
        나머지 논문이 h번 이하 인용되었다면, h의 최댓값이 이 과학자의 H-Index
    """
    # 논문의 인용 횟수를 오름차순으로 정렬 (작은 숫자부터 확인하기 위해)
    citations.sort()  # 0, 1, 4, 5, 6

    # 논문의 개수 저장
    n = len(citations)

    # 현재까지 찾은 H-Index 값
    h = 0

    # 모든 논문을 순회하면서 H-Index 조건을 만족하는 최댓값을 찾음
    for idx, citation in enumerate(citations):
        # 현재 논문이 포함된 상태에서 인용 횟수가 citation 이상인 논문의 개수
        above = n - idx
        below = idx  # 현재 논문보다 적게 인용된 논문의 개수

        # h부터 현재 논문의 인용 횟수(citation)까지 하나씩 확인
        for num in range(h + 1, citation + 1):
            # 현재 H-Index 후보(num)가 조건을 만족하는지 확인
            if above >= num:
                h = num
            else:
                return h

    return h


if __name__ == "__main__":
    citations = [4, 0, 6, 1, 5]
    print(solution(citations))
