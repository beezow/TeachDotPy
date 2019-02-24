def three_sum(arr, t):
	if arr == None or len(arr) < 3:
		return None
	to_return = []
	for i in combinations(arr, 3):
		if sum(i) is t:
			sorted_triple = sorted(list(i))
			if sorted_triple not in to_return:
				to_return.append(sorted_triple)
	return to_return
