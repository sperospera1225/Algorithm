# 2)  문자열 회전 : 한 단어가 다른 문자열에 포함되어 있는지 판별하는 isSubstring이라는 메서드가 있다고 치자. s1 과 s2 두 문자열이 주어지고, s2가 s1을 회전시킨 결과인지 판별하고자 한다.
# ex) ‘waterbottle’ 은 ‘erbottlewat’ 을 회전시켜서 얻을 수 있는 문자열이다.

def string_rotation(s1, s2):
    if (len(s1) == len(s2) and len(s1)>0):
        s2s2 = s2+s2
        if s2s2.find(s1) >= 0:
            print("True")
        else:
            print("False")
    else:
        print("False")

if __name__=='__main__':
    s1_input, s2_input = map(str,input().split(' '))
    string_rotation(s1_input, s2_input)
