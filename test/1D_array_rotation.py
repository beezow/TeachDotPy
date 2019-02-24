array= [1,2,3,4,5]
answer = []

for i in range(len(array)):
    answer.append(arr[(i + 1) % len(arr)])
    print(answer[i])
