def solution(n, lost, reserve):
    """
    Args
        n: 전체 학생 수 
        lost: 체육복을 도난당한 학생들의 번호가 담긴 배열
        reserve: 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
    
    Return
        체육수업을 들을 수 있는 학생의 최댓값
    """
    
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    for i in sorted(reserve_set):
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    
    return n - len(lost_set)


if __name__ == "__main__":
    n = 5
    lost = [2, 3]
    reserve = [1, 2]
    print(solution(n, lost, reserve)) 


    # lost = [1, 2, 3, 4, 5]
    # reserve = [3, 5, 6]