def solution(priorities, location):
    answer = 0
    queue = []

    for i, item in enumerate(priorities):
        queue.append([item, i])
    while (True):
        max_num = max(queue)[0]
        a = queue.pop(0)
        if a[0] == max_num:  # minqueue를 따로 관리하도록해도 가능
            answer += 1
            if a[1] == location:
                break
        else:
            queue.append(a)
    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))