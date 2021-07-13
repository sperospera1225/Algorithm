n = input()
m = input()
queue = []
queue2 = []

result=''
for i in range(len(n)):
    queue.append(n[i])
for i in range(len(m)):
    queue2.append(m[i])
for i in range(len(queue)):
    a = queue.pop(0)
    if a not in stack2:
        result += a
if len(result)==0:
    print("FRULA")
else:
    print(result)