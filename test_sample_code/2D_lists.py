a = []
a.append([1,2,3])
a.append([1,2,3])
a.append([1,2,3])

sum = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        sum += a[i][j] 

newsum = 0
for row in a:
    for cell in row:
        newsum += cell
