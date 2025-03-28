def solution(n, lost, reserve):
    status = [-1] + [1] * n
    for l in lost: status[l] -= 1
    for r in reserve: status[r] += 1

    for i in range(1, len(status)-1):
        if status[i] == 0: # 체육복 없으면
            if status[i-1] == 2: # 앞번호 여벌옷 있으면
                status[i], status[i-1] = 1, 1
            elif status[i+1] == 2: # 앞번호 여벌옷 있으면
                status[i], status[i+1] = 1, 1
    # 마지막 번호
    if status[n] == 0: # 체육복 없으면
        if status[n-1] == 2: # 앞번호 여벌옷 있으면
            status[n], status[n-1] = 1, 1
    # 체육복 있는 사람 수 계산
    answer = sum([1 for i in status if i > 0])

    return answer

if __name__ == "__main__":
    n = 7
    lost = [6, 7]
    reserve = [5, 7]
    sol = solution(n, lost, reserve)
    print(sol)  # 5