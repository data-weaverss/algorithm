# 최대한 다양한 종류의 폰켓몬을 가기질 원함
# nums는 항상 짝수
def solution(nums):
    mons_dict = {}

    for num in nums:
        mons_dict[num] = mons_dict.get(num, 0) + 1

    return min(len(mons_dict), len(nums) // 2)


if __name__ == "__main__":
    arr = [3, 3, 3, 2, 2, 2]
    sol = solution(arr)
    print(sol)
