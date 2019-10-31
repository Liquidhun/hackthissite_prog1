'''
HackThisSite - Programming - Level1
https://www.hackthissite.org/missions/prog/1/
'''

WORDLIST = "wordlist.txt"
RIDDLE = "string.txt"

def sortWords(wArray):
	reWord = []
	for i in range(len(wArray)):
		reWord.append(''.join(sorted(wArray[i])))
	return reWord

wordlist = open(WORDLIST)
wlist = wordlist.readlines()
wArray = []
cleanArray = []
for i in wlist:
	i = i.replace("\n","")
	wArray.append(i)
	cleanArray.append(i)

words = sortWords(wArray)


riddlelist = open(RIDDLE)
rlist = riddlelist.readlines()
rArray = []
riddleArray = []
for i in rlist:
	i = i.replace("\n","")
	rArray.append(i)
	riddleArray.append(i)

rwords = sortWords(rArray)
answer = []

for i in range(len(rwords)):
	for x in range(len(words)):
		if rwords[i] == words[x]:
			answer.append(cleanArray[x])

print(",".join(answer))
