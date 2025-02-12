# 하루에 최소 한 개의 의상을 입음
# 각 종류별로 최대 1가지 의상만 착용 가능
# return 서로 다른 옷의 조합의 수
def solution(clothes):
    clothes_count = {}  # 의상 종류별 개수를 저장할 딕셔너리

    for _, clothe in clothes:
        clothes_count[clothe] = clothes_count.get(clothe, 0) + 1

    result = 1  # 곱셈 연산을 위해 초기값을 1로 설정

    # 각 의상 종류별 {의상 개수 + 1(입지 않는 경우)} 를 곱함 - 의상 조합 경우의 수
    for value in clothes_count.values():
        result *= value + 1

    return result - 1  # 모든 의상을 입지 않는 경우의 수 제외


if __name__ == "__main__":
    clothes = [
        ["crow_mask", "face"],
        ["blue_sunglasses", "face"],
        ["smoky_makeup", "face"],
        ["green_turban", "headgear"],
    ]
    sol = solution(clothes)
    print(sol)
