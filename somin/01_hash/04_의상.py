# 서로 다른 옷의 조합의 수 return 
# 조건: 종류 별 1가지 의상만 착용 가능, 의상은 최소 1개 이상 입기
def solution(clothes):
    clothes_dict = {}
    for cloth, cat in clothes:
        # 입지 않는 경우 1로 초기화
        clothes_dict[cat] = clothes_dict.get(cat, 1) + 1

    # 종류별 조합 계산
    total_combi = 1
    for count in clothes_dict.values():
        total_combi *= count # 종류 별 한 개로 제한되므로 nC1
        
    # 모두 입지 않는 경우 1을 뺀다.
    return total_combi - 1


if __name__ == '__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    sol = solution(clothes)
    print(sol)