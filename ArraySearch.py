import sys
from indexObjClass import indexObj



# MergeSort in Python
# source: https://www.programiz.com/dsa/merge-sort
def mergeSort(array, motherString):
	if len(array) > 1:

		#  r is the point where the array is divided into two subarrays
		r = len(array)//2
		L = array[:r]
		M = array[r:]

		# Sort the two halves
		mergeSort(L, motherString)
		mergeSort(M, motherString)

		i = j = k = 0

		# Until we reach either end of either L or M, pick larger among
		# elements L and M and place them in the correct position at A[p..r]
		while i < len(L) and j < len(M):
			Le = motherString[L[i].start:]
			Mi = motherString[M[j].start:]

			if Le < Mi:

				array[k] = L[i]
				i += 1
			else:
				array[k] = M[j]
				j += 1
			k += 1

		# When we run out of elements in either L or M,
		# pick up the remaining elements and put in A[p..r]
		while i < len(L):
			array[k] = L[i]
			i += 1
			k += 1

		while j < len(M):
			array[k] = M[j]
			j += 1
			k += 1


def patternFind(suffixArray, pattern, motherString):
	R = len(motherString)
	L = 0

	while R > L:
		M = int((L + R) / 2)

		s = motherString[suffixArray[M].start:]
		#print(s)

		res = 0
		
		if pattern > s:
			res = -1
		elif pattern < s:
			res = 1

		if res < 0:
			L = M + 1
		else:
			R = M

	start = L
	R = len(motherString)

	while R > L:
		M = int((L + R) / 2)

		s = motherString[suffixArray[M].start:]
		#print(s)

		res = 0
		
		if s[:len(pattern)] == pattern:
			res = -1
		else:
			res = 1

		if res < 0:
			L = M +1
		else:
			R = M

	end = R - 1 


	f = [i for i in range(start,end+1)]
	found = [suffixArray[i].start for i in f]


	print(f"Pattern found at: {found}")
	return found






text_file = sys.argv[1]
pattern_file = sys.argv[2]

s = sys.argv[1]
p = sys.argv[2]


with open(text_file, "r") as f:
	s = f.readline()
f.close()

with open(pattern_file, "r") as f:
	p = f.readline()
f.close()



suffixArray = []

counter = 0


for i in range(len(s)):
	slic = indexObj(start=i)
	suffixArray.append(slic)


print("sorting")
mergeSort(suffixArray, s)
print("finished")

for obj in suffixArray:
	print(f"index: {obj.start}, suffix: {s[obj.start:]}")



matchArray = patternFind(suffixArray, p, s)
