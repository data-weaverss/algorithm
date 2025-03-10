def solution(answers):
    """가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return"""
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0] * 3
    for i in range(len(answers)):
        answer = answers[i]
        if A[i%5] == answer:
            score[0] += 1
        if B[i%8] == answer:
            score[1] += 1
        if C[i%10] == answer:
            score[2] += 1
    
    first_rank = []
    max_score = max(score)
    for i, score in enumerate(score):
        if score == max_score:
            first_rank.append(i+1)
    return first_rank

if __name__ == "__main__":
    answers = [1,3,2,4,2]	

    sol = solution(answers)
    print(sol)