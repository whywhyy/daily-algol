# 입국심사

# 풀이를 보고 풀었다 ㅠㅠ
# 무조건 끝날 시간을 찾는다 !
# 무조건 끝날 시간을 반으로 쪼개며 이래도 끝나는지 확인한다 !
# 최소한 임으로 total == n 이 같아도 right = mid -1 을 한다 !
def solution(n, times):
    answer = 0
    times = sorted(times)
    left = 0
    right = n * times[-1]

    while left <= right:
        mid = (left+right) // 2
        total = sum([mid // i for i in times])
        if total < n:
            left = mid + 1
        elif total > n:
            right = mid -1
        else:
            right = mid -1

    return left


def solution(n, times):

    lo, hi = 0, max(times) * n

    while hi >= lo:
        mid = lo + (hi - lo) // 2
        time = sum([mid // t for t in times])
        if time == n and hi == lo:
            break
        if time < n:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo