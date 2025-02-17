# 합이 T가 되는 부 배열 A, B 쌍의 개수
import sys

def create_cumulative_arr(arr):
    cumulative_arr = [0]
    for i in range(len(arr)):
        cumulative_arr.append(cumulative_arr[i] + arr[i])

    return cumulative_arr

def return_cnt_dict(arr, len):
    dict = {}
    for i in range(len):
        for j in range(i+1, len+1):
            key = arr[j] - arr[i]
            dict[key] = dict.get(key, 0) + 1

    return dict

if __name__ == "__main__":
    T = int(input())
    a_len = int(input())
    a_arr = [int(num) for num in input().split()]
    b_len = int(input())
    b_arr = [int(num) for num in input().split()]

    # 누적 합 배열 만들기
    a_arr = create_cumulative_arr(a_arr)
    b_arr = create_cumulative_arr(b_arr)
    # 각 배열의 부분 리스트 합 - 개수 딕셔너리 생성
    a_dict = return_cnt_dict(a_arr, a_len)
    b_dict = return_cnt_dict(b_arr, b_len)

    # a + b = T 가 되는 경우의 수 계산
    combi_cnt = 0 
    for a_key, a_cnt in a_dict.items():
        b_cnt = b_dict.get(T-a_key)
        if b_cnt != None:
            combi_cnt += a_cnt * b_cnt

    print(combi_cnt)