def rotate_matrix(matrix):
	if matrix is None or len(matrix) is 0:
		return None
	#This solution was found on Geeksforgeeks; my code (in comments)
	#was not efficient enough as it didn't modify the matrix in place
	length = len(matrix)
	for i in range(0, int(length / 2)):
		for j in range(i, length - i - 1):
			temporary = matrix[i][j]# store current value as temp so it doesn't get lost
			matrix[i][j] = matrix[j][length - 1 - i] #moves from right to top
			matrix[j][length - 1 - i] = matrix[length - 1 - i][length - 1 - j] #moves from bottom to right
			matrix[length - 1 - i][length - 1 - j] = matrix[length - 1 - j][i] #moves from left to bottom
			matrix[length - 1 - j][i] = temporary
	return matrix
