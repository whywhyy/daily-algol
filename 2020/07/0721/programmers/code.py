# problem : 베스트 앨범

def solution(genres, plays):
    dict_genres = {}
    obj = {} # gerner , play , index
    for i in range(len(genres)):
        try:
            dict_genres[genres[i]] += plays[i]
            obj[genres[i]].append((i,plays[i]))
        except KeyError:
            dict_genres[genres[i]] = plays[i]
            obj[genres[i]] = []
            obj[genres[i]].append((i,plays[i]))

    sort_gernres = sorted(dict_genres.items(), key= lambda x : x[1], reverse=True)

    
    answer = []
    for i in sort_gernres:
        now = obj[i[0]]
        # sorting 시 2개이상의 요소일때 reverse 를 -(음수) 로 하는 방법이 있다는걸 배워간다.
        now = sorted(now, key= lambda x : (-x[1],x[0]))
        for i in range(len(now)):
            if i == 2:
                break
            answer.append(now[i][0])
        """
        Test code 에서 장르별 노래가 1개만 있는 경우가 많아 자주 KeyError 
        발생하여 EAFP 가 더 느림.(런타임 에러의 이유)
        try:
            answer.append(now[0][0])
            answer.append(now[1][0])
        except KeyError:
            continue
        """
    
    return  answer