# 3. https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    dictionary = {}

    for item in record:
        action1 = item.split()
        if action1[0] == 'Enter' or 'Change':
            dictionary[action1[1]] == action1[2]
    for item in record:
        action1 = item.split()
        if action1[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(dictionary[action1[1]]))
        elif action1[0] == 'Change':
            answer.append("{}님이 나갔습니다.".format(dictionary[action1[1]]))
    return answer
