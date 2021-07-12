array = [3, 5, 4, 6, 11, 1, -1]
targetSum = 10

def twoNumberSum(array, targetSum):
	ht = dict()
	for i in range(len(array)):
		if array[i] in ht:
			print(ht[array[i]], array[i])
			return True
		else:
			ht[targetSum - array[i]] = array[i]
	return False
	
print(twoNumberSum(array, targetSum))