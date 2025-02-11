def solution(phone_book):
    phone_dict = {}  # 전화번호 목록을 딕셔너리로 저장

    # 모든 전화번호를 딕셔너리에 저장
    for phone in phone_book:
        phone_dict[phone] = 1

    # 각 전화번호가 다른 전화번호의 접두어인지 확인
    for phone in phone_book:
        prefix = ""
        for char in list(phone):
            prefix += char
            if prefix in phone_dict and prefix != phone:
                return False

    return True


if __name__ == "__main__":
    phone_book = ["119", "97674223", "1195524421"]
    sol = solution(phone_book)
    print(sol)
