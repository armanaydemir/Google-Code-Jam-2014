s = [item.rstrip('\n') for item in open('Q1in.txt','r').readlines()]
numcases = int(s[0])
def main(index, case, x, y):
	ran = int(s[index].split()[1])
	run = int(s[index].split()[0])
	x = s[x].split()
	y = s[y].split()
	switch = 0
	imp = False
	for t in range(0,ran):
		xone = 0
		yone = 0
		yzero = 0
		xzero = 0
		for i in range(0,run):
			if x[i][t] == '1':
				xone += 1
			else:
				xzero += 1
			if y[i][t] == '1':
				yone += 1
			else:
				yzero += 1	
		temprun = t
		if xone == yone:
			continue
		elif xone == yzero:
			#print temprun
			switch += 1
			if y[i][t] == '1':
				y[i][t] = '0'
			else:
				y[i][t] = '1'
		elif xone != yone:
			imp = True
			break
	if imp == True:
		return 'Case #' + str(case) + ': NOT POSSIBLE'
	else:
		for t in x:
			print y.find(t)
		return 'Case #' + str(case) + ': ' + str(switch)
		
		
def checker:

	
text_file = open('Q1out.txt', 'w')
for t in range(0, numcases):
	text_file.write(main(1+(3*t), t+1, 2+(3*t), 3+(3*t)) + '\n')
text_file.close()