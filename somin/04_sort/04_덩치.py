import sys
'''
return 덩치 등수 출력
조건: 본인보다 덩치가 큰 사람의 수가 K이면, 본인은 (K+1)등
'''
def solution(arr, n):
    rank = [1] * n  # 모든 사람의 기본 등수를 1로 설정

    # 몸무게, 키를 기준으로 정렬하지 않고 비교
    for i in range(n):
        for j in range(n):
            if i != j and arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:  
                # 몸무게와 키가 모두 큰 사람이 있으면 등수 증가
                rank[i] += 1

    return rank

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())  # 입력
    arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]  

    sol = solution(arr, n)
    print(*sol)  # 공백으로 구분하여 출력