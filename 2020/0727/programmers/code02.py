# 디스크 컨트롤러
# jobs List[List[input, process]]
import heapq

def solution(jobs):
    answer = 0
    # 동일한 시간일때는 process 가 짧은 걸 앞으로 하자!
    jobs = sorted(jobs, key = lambda x :(x[0],x[1]))
    
    pri_job = []
    now_index = 0
    now_time = 0
    last_index = 0
    # for i in range(len(jobs)):
    #     if jobs[i][0] == jobs[0][0]:
    #         heapq.heappush(pri_job, (jobs[i][1], jobs[i][0]))
    #         now_index = i
    #     else:
    #         break
    # last_index = now_index
    heapq.heappush(pri_job, (jobs[0][1], jobs[0][0]))
    now_time = jobs[0][0]

    while len(pri_job):
        now = heapq.heappop(pri_job)
        process_time, start_time = now[0], now[1]
        now_time += process_time
        answer += (now_time-start_time)
        for i in range(last_index+1, len(jobs)):
            if jobs[i][0] <= now_time :
                heapq.heappush(pri_job,(jobs[i][1],jobs[i][0]))
                now_index = i
            elif len(pri_job) == 0:
                now_time = jobs[i][0]
                heapq.heappush(pri_job,(jobs[i][1],jobs[i][0]))
                now_index = i
            else:
                break      
        last_index = now_index

    answer //= len(jobs)

    return answer