# 1)  행렬 회전 :  NxN 행렬이 있다. 이 행렬을 오른쪽으로 90도, 180도, 270도 회전시키는 코드를 작성하라.

def rotate_90(m):
    matrix_a = [[0]*len(m) for _ in range(len(m))]
    # [[0]*len(m)]*len(m)을 쓰며는 대입연산시 얕은복사로 인한 모든열이 바뀜
    # for문을 활용하자
    for i in range(len(m)):
        for j in range(len(m)):
            # print(m[i][j], j, len(m)-1-i)
            matrix_a[j][len(m)-1-i] = m[i][j]
    return matrix_a

def rotate_180(m):
    matrix_b = [[0] * len(m) for _ in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            matrix_b[len(m) - 1 - i][len(m) - 1 - j] = m[i][j]
    return matrix_b

def rotate_270(m):
    matrix_c = [[0] * len(m) for _ in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            matrix_c[len(m) - 1 - j][i] = m[i][j]
    return matrix_c

if __name__=='__main__':
    n = int(input())
    field = [[int(x) for x in input().split()] for i in range(n)]
    print(rotate_90(field))
    print(rotate_180(field))
    print(rotate_270(field))

