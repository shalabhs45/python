def longestCommonSubsequence(str1, str2):
    # Write your code here.
	m = len(str1)
	n = len(str2)
    length = [[0 for x in range( m + 1)] for y in range( n + 1)]
	for i in range(1, n+1):
		for j in range(1, m+1):
			if str2[i-1] == str1[j-1]:
				length[i][j] = length[i - 1][j - 1]  + 1
			else:
				length[i][j] = max (length[i -1][j], length[i][j-1])
	return buildSequence(length, str1)

def buildSequence(length, string):
	sequence = []
	i = len(length) - 1
	j = len(length[0]) -1
	while i!=0 and j!=0:
		if length[i][j] == length[i-1][j]:
			i -=1
		elif length[i][j] == length[i][j-1]:
			j -= 1
		else:
			sequence.append(string[j-1])
			i -=1
			j -=1
		return list(reversed(sequence))
	
