# 최대한 다양한 종류의 폰켓몬을 가기질 원함
# nums는 항상 짝수
def solution(nums):
    mons = {}

    for num in nums:
        mons[num] = mons.get(num, 0) + 1

    return min(len(mons), len(nums) // 2)


# 숏코딩: return min(len(set(nums)), len(nums) // 2)
