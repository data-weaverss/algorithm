from itertools import product

def solution(word):
    """
    - return: word가 사전에서 몇 번째 단어인지
    """
    words = ['A', 'E', 'I', 'O', 'U']
    words_permutation = []

    for i in range(1, 6):
        for perm in list(product(words, repeat=i)): # product() -> itertools.product 객체를 반환하므로 list로 변환
            words_permutation.append("".join(perm))
    
    words_permutation.sort()
    
    return words_permutation.index(word) + 1

if __name__ == "__main__":
    word = "AAAE"
    print(solution(word)) 
