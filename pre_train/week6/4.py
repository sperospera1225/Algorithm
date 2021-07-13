def solution(gems):
    answer = []
    size = len(set(gems))
    dic = {gems[0]: 1}
    temp = [1, len(gems)]
    start, end = 0, 0
    while (start < len(gems) and end < len(gems)):
        if len(dic) != size:
            end += 1
            if end >= len(gems):
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
        else:
            if end - start < temp[1] - temp[0]:
                temp = [start + 1, end + 1]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
    return temp


a = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
a