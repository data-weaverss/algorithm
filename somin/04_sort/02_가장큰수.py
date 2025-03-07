def solution(numbers):
    if all(num == 0 for num in numbers):
        return '0'

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return ''.join(numbers)


if __name__ == "__main__":
    numbers = [3, 30, 34, 5, 9]

    sol = solution(numbers)
    print(sol) # "9534330"