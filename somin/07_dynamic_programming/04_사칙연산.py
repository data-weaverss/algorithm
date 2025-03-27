def solution(arr):

    def compute(start, end):
        # 숫자 하나만 있는 경우
        if start == end:
            return [int(arr[start])]

        results = []
        for i in range(start + 1, end, 2):  # 연산자 위치만 순회
            op = arr[i]
            left = compute(start, i - 1)
            right = compute(i + 1, end)

            for l in left:
                for r in right:
                    if op == '+':
                        results.append(l + r)
                    elif op == '-':
                        results.append(l - r)
        return results

    return max(compute(0, len(arr) - 1))


if __name__ == "__main__":
    arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]	
    print(solution(arr))  