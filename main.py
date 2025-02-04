def satisfiesRequirements(query, word):
	if '*' in query:
		r = []
		for i in range(len(word)-len(query)+2):
			if satisfiesRequirements(query.replace('*','?'*i,1), word):
				return True
		return False
	if len(query) != len(word):
		return False
	for i in range(len(word)):
		if word[i] != query[i] and query[i] != '?':
			return False
	return True
words = []
wordlist = open('wordlist.txt','r')
getls=input('Letters: ')
for i in wordlist:
	i = i.strip()
	if sum([i.count(j) for j in getls]) == len(i):
		words.append(i)
wordlist.close()
while True:
	q = input('Query: ')
	count = 0
	for i in words:
		if satisfiesRequirements(q, i):
			print(i)
			count += 1
	print(str(count)+" words found.")
