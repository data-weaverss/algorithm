# 앨범에 들어갈 노래의 고유 번호를 순서대로 return
# 1. 장르 별 노래 두 개씩 선택
# 2. 기준: 장르 - 재생 수가 많은 순, 
#         노래 - 재생 수 많은 순, 동일하면 고유 번호가 낮은 순
def solution(genres, plays): 
    album_order = []
    genre_plays = {}
    genre_sum = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):  
        # 장르 - 고유번호: 재생수 dict 생성
        genre_plays[genre] = genre_plays.get(genre, {})
        genre_plays[genre][idx] = play
        # 장르 별 재생수 전체 합 dict 생성
        genre_sum[genre] = genre_sum.get(genre, 0) + play

    # 장르 순서 정렬
    genre_order = sorted(genre_sum.items(), key=lambda x: -x[1])

    # 정렬된 장르 순서대로, 재생수별 정렬 > 앨범 수록
    for genre, _ in genre_order:
        sorted_plays = sorted(genre_plays[genre].items(), key=lambda x: -x[1])
        for idx, _ in sorted_plays[:2]: # 2곡씩 수록
            album_order.append(idx)

    return album_order

if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]	
    plays = [500, 600, 150, 800, 2500]	
    sol = solution(genres, plays)
    print(sol)