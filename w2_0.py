# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).
# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

def truncate_sentence(s,k):
    str_list = s.split()
    final_text = ''
    for i in range(0,k):
        final_text += (str_list[i]+' ')
    return final_text.strip()
if __name__=='__main__':
    s = "Hello how are you Contestant"
    k = 4
    print(truncate_sentence(s, k))
