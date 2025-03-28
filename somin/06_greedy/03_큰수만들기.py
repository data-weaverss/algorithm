def solution(number, k):
    answer = []
    m = len(number) - k # 숫자 제거 후의 자릿수
    start = 0 # 시작 포인터

    while start < len(number):
        end = start + k + 1
        if end > len(number):  # 범위를 벗어나지 않도록 조정
            end = len(number)
        
       # start <-> end 사이의 최댓값 찾기
        max_num = '0'
        max_idx = start
        for i in range(start, end):
            if number[i] > max_num:
                max_num = number[i]
                max_idx = i
                if max_num == '9':  # 최댓값을 찾으면 더 이상 탐색 불필요
                    break

        k -= max_idx # 제거된 개수 업데이트
        answer.append(max_num) 

        max_idx += start # number 리스트 내의 index
        start = max_idx + 1 # 최댓값 다음 으로 이동

        if k == 0 or len(answer) == m:
            break

    # 남아있는 숫자 뒤에 이어붙이기
    answer.extend(number[start:len(number)-k]) 
    return ''.join(answer)  

if __name__ == "__main__":
    number = "976543210"
    k = 3
    sol = solution(number, k)
    print(sol)  # 3234