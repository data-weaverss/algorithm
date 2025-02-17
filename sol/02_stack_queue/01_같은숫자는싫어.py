def solution(arr):
    stack = []

    for num in arr:
        if stack and stack[-1] == num:  # stack의 peek()
            continue

        stack.append(num)

    return stack


if __name__ == "__main__":
    arr = [1, 1, 3, 3, 0, 1, 1]
    sol = solution(arr)
    print(sol)
