from collections import defaultdict


def solution(genres, plays):
    """
    - 가장 많이 재생된 장르를 우선 선택
    - 각 장르에서 가장 많이 재생된 노래 2곡씩 선정(재생 수 같으면 고유번호 낮은 순)
    """
    # 장르별 총 재생 횟수 저장(key: 장르, value: 총 재생 횟수)
    genre_play_count = defaultdict(int)

    # 장르별 노래 리스트 저장(key: 장르, value: [(노래 ID, 재생 횟수)] 리스트)
    genre_songs = defaultdict(list)

    for song_id, (genre, play_count) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play_count  # 장르별 총 재생 횟수 합산
        genre_songs[genre].append((song_id, play_count))  # (노래 ID, 재생 횟수) 저장

    # 장르별 총 재생 횟수를 기준으로 내림차순 정렬
    sorted_genres = sorted(genre_play_count, key=lambda g: -genre_play_count[g])

    result = []

    for genre in sorted_genres:
        # 해당 장르의 노래를 (재생 횟수 내림차순, 고유번호 오름차순) 정렬 후 상위 2곡 선택
        top_songs = sorted(genre_songs[genre], key=lambda x: (-x[1], x[0]))[:2]
        result.extend([song_id for song_id, _ in top_songs])

    return result


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic"]
    plays = [500, 1500, 150, 150]
    sol = solution(genres, plays)
    print(sol)
