arr = [1,2,3,4,5]
answer = []
shift = 1
for i in range(len(arr)):
    answer.append(arr[(i + shift) % len(arr)])
    print(answer[i])
