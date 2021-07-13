import heapq


# SJF scheduling is optimization scheduling
def solution(jobs):
    num = len(jobs)
    q = []
    i = 0
    waiting_time = []
    while (True):
        print(i, '초')
        for job in jobs:
            if i == job[0]:
                heapq.heappush(q, [job[1], job[0]])
            else:
                jobs.pop(0)
                break
        print(q)
        if q[0][0] != 0:
            q[0][0] -= 1
        elif q[0][0] == 0:

            waiting_time.append(i - q[0][1])
            a = heapq.heappop(q)
            if q:
                q[0][0] -= 1
        if not q:
            break
        i += 1
    return int(sum(waiting_time) / num)


solution([[0, 3], [1, 9], [2, 6]])