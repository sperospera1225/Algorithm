def solution(N, stages):
    answer = []
    for i in range(len(stages)):
        cnt = 0
        for item in stages:
            if item <= i+1:
                cnt += 1
        answer[i] = cnt/len(stages)
    return answer

if __name__ == '__main__':
    solution(5, [2,1,2,6,2,4,3,3])