array= [1,2,3,4,5]
shifted = []

for i in range(len(array)):
    shifted.append(array[(i + 1) % len(array)])
    print(shifted[i])
