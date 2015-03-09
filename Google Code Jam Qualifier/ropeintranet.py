#Rope Intranet
s = [item.rstrip('\n') for item in open('inputs.txt','r').readlines()]
numcases = int(s[0])
text_file = open('outputropes.txt', 'w')
def main(index, v, case):
	a = []
	b = []
	for li in range(0,v):
		high = s[index+li+1].split()
		a.append(int(high[0]))
		b.append(int(high[1]))
	num = 0
	print a
	print b
	for i in range(0,len(a)):
		if a[i] > b[i]:
			for t in range(i+1,len(b)):
				if a[t] < a[i] and b[t] > b[i]:
					num += 1
		elif a[i] < b[i]:
			for t in range(i+1,len(b)):
				if a[t] > a[i] and b[t] < b[i]:
					num += 1
	return 'Case #' + str(case) + ': ' + str(num)
k = 1
for t in range(0, numcases):
	text_file.write(main(k,int(s[k]), t+1) + '\n')
	k += int(s[k])+1
text_file.close()