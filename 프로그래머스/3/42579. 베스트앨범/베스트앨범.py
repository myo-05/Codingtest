'''
1.곡번호(index)
2.장르(for genre in genres)
3.재생수(for play in plasys)

재생수 많은 장르순으로, 장르당 상위 2곡 번호
0) 곡번호 장르 재생수 저장
1) 장르 정렬
    2) 장르 내 정렬
    3) 상위 2곡 선별
4) 반복
'''

def solution(genres, plays):
    answer = []
    pick = 2 # 곡 선별 수 
    play_map = {genre: {} for genre in set(genres)} # 장르별 곡 저장
    for i,(genre,play) in enumerate(zip(genres,plays)): 
        play_map[genre][i] = play # 곡 저장
        
    genre_totals = {genre: sum(play_map[genre].values()) for genre in play_map} # 장르별 총 재생수
    genres_sorted = sorted(genre_totals.keys(),key=genre_totals.get,reverse=True) # 장르정렬 - 재생수내림차순
    
    for genre in genres_sorted:
        song_sorted = sorted(play_map[genre].keys(),key=play_map[genre].get,reverse=True) # 장르 내 정렬
        answer += song_sorted[:pick] # 상위 2곡 선별 후 수록
    return answer