def solution(answers):
    patterns = [ # 수포자가 찍는 방식
        [1,2,3,4,5] * 2000, # 최대 10,000문제이므로 
        [2,1,2,3,2,4,2,5] * 1250,
        [3,3,1,1,2,2,4,4,5,5] * 1000
    ]
    
    scores = [0, 0, 0] # 수포자들의 점수
    
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i]:
                scores[j] += 1
    
    max_score = max(scores)
        
    return [i+1 for i, score in enumerate(scores) if score == max_score] # 최고점을 받은 수포자의 번호

if __name__ == "__main__":
    answers = [1,3,2,4,2]
    print(solution(answers))
