arr = [['a','b','c','d','e'], ['f','g','h','i','j'], ['k','l','m','n','o'], ['p','q','r','s','t'], ['u','v','w','x','y']]
path = []
left = 0
right = len(arr[0])
up = 0
down = len(arr)

while (right > left) and (down > up):
    for i in range(left, right):
        path.append(arr[up][i])
    up += 1
    if (right > left) and (down > up):
        for i in range(up, down):
            path.append(arr[i][right - 1])
        right -= 1
    if (right > left) and (down > up):
        for i in range(right - 1, left - 1, -1):
            path.append(arr[down - 1][i])
        down -= 1
    if (right > left) and (down > up):
        for i in range(down - 1, up - 1, -1):
            path.append(arr[i][left])
        left += 1
for i in range(len(path)):
    print(path[i])
