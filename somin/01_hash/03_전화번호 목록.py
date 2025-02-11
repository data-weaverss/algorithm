# 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
# 있으면 False, 없으면 True
def solution(phone_book):
    phone_book.sort()
    # 정렬된 전화번호부에서 앞뒤 전화번호 비교 -> 접두어가 있는지 확인
    for i in range(1, len(phone_book)): 
        prev_number = phone_book[i-1]
        if prev_number == phone_book[i][:len(prev_number)]:
            return False
    return True

if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421"]
    sol = solution(phone_book)
    print(sol)
