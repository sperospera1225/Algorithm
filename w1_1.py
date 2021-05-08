# #1) 중복이 없는가 : 문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘. (자료구조를 추가로 사용하지않고 풀 수 있는 알고리즘도 고민)
duplicate_char = input()
duplicate_list = list()
for i in range(len(duplicate_char)):
    duplicate_list.append(duplicate_char[i])
duplicate_set = set(duplicate_list)
if len(duplicate_set) == len(duplicate_list):
    print("중복이 없습니다.")
else:
    print("중복이 있습니다.")
# # #2) 순열 확인 : 문자열 두 개가 주어졌을 때 이 둘이 서로 순열 관계에 있는지 확인하는 메서드를 작성하라.
# # word1, word2 = map(str, input().split())
# # # 3) 회문 수열 : 주어진 문자열이 회문(palindrome)의 순열인지 아닌지 확인하는 함수를 작성하라. 회문이란 앞으로 읽으나 뒤로 읽으나 같은 단어 혹은 구절을 의미하며, 순열이란 문자열을 재배치하는 것을 뜻한다.
word = input()
is_palindrome = True
for i in range(len(word)):
    if word[i] == word[len(word) - (i+1)]:
        continue
    else:
        is_palindrome=False
        break
print(is_palindrome)
# 4) 하나 빼기 : 문자열을 편집하는 방법 세 가지 1) 문자 삽입, 2) 문자 삭제, 3) 문자 교체. 문자열 두 개가 주어졌을 때, 문자열을 같게 만들기 위한 편집 횟수가 1회 이내인지 확인하는 함수를 작성하라

# 5) 문자열 압축 : 반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라. 예를 들어, 문자열 aabccccaaa 압축하면 a2b1c5a3이 된다. 만약 압축한 문자열의 길이가 기존 문자열의 길이보다 길다면 기존 문자열을 반환해야 한다. 문자열은 a-z 으로만 이루어져있다.
string_compress = input()
temp = string_compress[0:1]
count = 0
result = ''

for i in range(len(string_compress)):
    if string_compress[i]==temp:
        count += 1
    else:
        result += (temp+str(count))
        count = 1
        temp = string_compress[i]
    if i == len(string_compress)-1:
        result += (temp+str(count))
if len(result) > len(string_compress):
    print(string_compress)
else:
    print(result)