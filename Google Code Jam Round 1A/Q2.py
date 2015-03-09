s = [item.rstrip('\n') for item in open('Q2in.txt','r').readlines()]
text_file = open('Q2out.txt', 'w')
numcases = int(s[0])

def main(n, case, li):
	same = 0
	for t in li:
		if int(t) == li.index(t):
			same += 1
	if same >= int(n/4):
		return 'Case #' + str(case) + ': BAD'
	else:
		return 'Case #' + str(case) + ': GOOD'

for t in range(0, numcases):
	text_file.write(main(int(s[1+(2*t)]), t+1, s[2+(2*t)].split()) + '\n')
text_file.close()