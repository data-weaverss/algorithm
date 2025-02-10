def solution(nums):
    max_pick = len(nums) // 2  # 선택할 수 있는 최대 폰켓몬 수
    unique_types = len(set(nums))  # 폰켓몬 종류의 개수
    return min(max_pick, unique_types)

if __name__ == '__main__':
    arr = [3,3,3,2,2,2]
    sol = solution(arr)
    print(sol)
