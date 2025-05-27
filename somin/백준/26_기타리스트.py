import sys

def solution(volumes, num_songs, start_volume, max_volume):
    """
    마지막 곡의 최대볼륨을 구하시오.
    마지막 곡을 연주할 수 없다면 -1
    """
    # dp[i][v] = i번째 곡에서 볼륨 v가 가능한지 여부 (1: 가능, 0: 불가능)
    dp = [[0] * (max_volume + 1) for _ in range(num_songs + 1)]
    dp[0][start_volume] = 1

    for song_idx in range(num_songs):
        for vol in range(max_volume + 1):
            if dp[song_idx][vol] == 0:
                continue
            increased = vol + volumes[song_idx]
            if increased <= max_volume:
                dp[song_idx + 1][increased] = 1
            decreased = vol - volumes[song_idx]
            if decreased >= 0:
                dp[song_idx + 1][decreased] = 1

    # 마지막 곡에서 가능한 최대 볼륨 탐색
    for vol in range(max_volume, -1, -1):
        if dp[num_songs][vol] == 1:
            return vol

    return -1
            

if __name__ == "__main__":
    songs_len, start, max_volume = map(int, sys.stdin.readline().split())
    volumes = list(map(int, sys.stdin.readline().split()))

    print(solution(volumes, songs_len, start, max_volume))