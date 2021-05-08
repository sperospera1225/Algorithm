
def solution(s):
    answer = 0
    test_cases = list()
    for i in range(1,len(s)):
        temp = s[0:i]
        count = 0
        result = ''

        for i in range(len(s)):
            if s[i] == temp:
                count += 1
            else:
                result += (temp + str(count))
                count = 1
                temp = s[i]
            if i == len(s) - 1:
                result += (temp + str(count))
        if len(result) > len(s):
            test_cases.append(s)
        else:
            test_cases.append(result)
    answer = test_cases[0]
    for i in range(len(test_cases)):
        if(len(test_cases[i])<len(answer)):
            answer=test_cases[i]

    return answer

if __name__=='__main__':
    print(solution('aaaaabcabcdef'))

