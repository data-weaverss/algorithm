def solution(citations):
    citations.sort(reverse=True) # 내림차순 정렬 [8344, 328, 164, 46, 1]
    # 본인보다 큰 논문 수 <= 인용 수, 만족하는 것만 bigger_arr에 저장.
    # 최대 h-index를 구하는 것이기 때문에, 위를 만족하는 갯수와 같다.
    bigger_arr = [(i+1, c) for i, c in enumerate(citations) if i+1 <= c]
    # bigger_arr = [(1, 8344), (2, 328), (3, 164), (4, 46)]
    return len(bigger_arr)

if __name__ == "__main__":
    citations = [46, 328, 8344, 164, 1]

    sol = solution(citations)
    print(sol)