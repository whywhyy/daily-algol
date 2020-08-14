def solution(stock, dates, supplies, k):
    import heapq as hq
    answer = 0
    heap = []
    j = 0

    # 버티다가 가장 크게 supplies 된날꺼를 가져옴
    # 왜냐하면 초기 stock 으로 ~ n 일까지 버틸 수 있다고 할때,
    # ~ n 일중 전에 어차피 최소한 한번은 보급을 받아야 한다.
    # 기왕 받는거 가장 큰 값으로 받아서 횟수를 가장 줄이자!

    while stock < k:
        for i in range(j, len(dates)):
            if dates[i] <= stock:
                hq.heappush(heap, (-supplies[i], supplies[i]))
                j = i + 1

            else:
                break

        temp = hq.heappop(heap)[1]
        stock += temp
        answer += 1

    return answer