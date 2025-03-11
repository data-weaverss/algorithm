def solution(brown, yellow):
    """
    - 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫
    - return: 카펫의 가로, 세로 크기 배열
    
    - 카펫의 가로 길이 >= 세로 길이
    
    - brown = 2w + 2h - 4 (겹치는 부분 4개 제외)
    - yellow = (w-2)(h-2)
    """
    
    answer = []
    
    w_plus_h = brown//2 + 2
    
    for h in range(3, w_plus_h): 
        w = w_plus_h - h
        if (h-2)*(w-2) == yellow:
            return w, h

if __name__ == "__main__":
    brown = 10
    yellow = 2
    print(solution(brown, yellow))
