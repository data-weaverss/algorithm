def solution(numbers):
    """
    - 30, 301 -> 문자열 정렬 할 경우 30130 의 결과가 나옴.
    - 이를 4자리로 확장하면 3030, 3013 이어서 30을 먼저 정렬하고, 301이 그 후로 오게되는 원리
    - 따라서, 각 숫자를 4자리까지 반복 확장하면 비교되는 숫자들이 어떤 순서로 올 때 더 큰 결과가 나오는지 미리 확인할 수 있음
    """
    answer = ""

    # 숫자를 문자열로 변환
    num_str = [str(number) for number in numbers]

    # 문자열을 4자리까지 반복하여 만든 값으로 정렬
    num_str.sort(key=lambda x: (x * 4), reverse=True)

    # "0000" 같은 경우 "0"으로 변환
    return "".join(num_str) if num_str[0] != "0" else "0"


if __name__ == "__main__":
    numbers = [0, 0, 0, 0]

    print(solution(numbers))
