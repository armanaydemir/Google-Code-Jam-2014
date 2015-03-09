s = [item.rstrip('\n') for item in open('prob1in.txt','r').readlines()]
numcases = int(s[0])
text_file = open('prob1out.txt', 'w')
addnum = 0

def check(shortindex):
	inold = []
	notold = []
	for i in flight:
		if str(shortindex) in i and str(shortindex) in old:
			l = 0
			for t in i:
				if t == str(shortindex):
					if l == 0:
						inold.append(i[1])
					else:
						inold.append(i[0])
				else:
					l += 1
		elif str(shortindex) in i:
			l = 0
			for t in i:
				if t == str(shortindex):
					if l == 0:
						notold.append(i[1])
					else:
						notold.append(i[0])
				else:
					l += 1
	print notold
	print inold
	for t in notold:
		for i in check(t):
			inold.append(i)
	return inold

					
def main(index,case):
	final = ''
	add = s[index].split()
	zip = []
	global short
	short = []
	global flight
	flight = []
	pos = []
	global old
	old = []
	for i in range(1,int(add[0])+1):
		zip.append(int(s[i+index]))
	for i in range(1,int(add[1])+1):
		flight.append(s[int(add[0])+i+index].split())
	shortest = int(zip[0])
	for i in range(1,len(zip)):
		if int(zip[i]) < shortest:
			shortest = int(zip[i])
	short.append(shortest)
	shortindex = zip.index(shortest) + 1
	old.append(shortindex)
	temp = []
	while len(short) != int(add[0]):
		oops = 1
		pos = []
		while len(pos) == 0:
			shortindex = old[len(old)-oops]
			for i in flight:
				if str(shortindex) in i:
					l = 0
					for t in i:
						if t == str(shortindex):
							if l == 0:
								pos.append(i[1])
							else:
								pos.append(i[0])
						else:
							l += 1
			for i in old:
				if str(i) in pos:
					pos.remove(str(i))
			oops += 1
		if len(pos) == 1:
			shortest = zip[int(pos[0])-1]
			shortindex = pos[0]
		elif len(pos) > 0:
			shortest = zip[int(pos[0])-1]
			shortindex = pos[0]
			for i in range(1,len(pos)-1):
				if int(zip[int(pos[i])-1]) < shortest:
					shortest = int(zip[int(pos[i])-1])
					shortindex = pos[i]
		for i in flight:
			if str(shortindex) in i:
				l = 0
				for t in i:
					if t == str(shortindex):
						if l == 0:
							temp.append(i[1])
						else:
							temp.append(i[0])
					else:
						l += 1
						
		old.append(shortindex)
		y = check(shortindex)
		old.remove(shortindex)
		if len(temp) > 1:
			for t in y:
				if zip[int(t)-1] < shortest:
					shortest = zip[int(t) - 1]
					shortindex = t
				
		short.append(shortest)
		old.append(shortindex)
	for i in short:
		final = final + str(i)
	return 'Case #' + str(case) + ': ' + final

for t in range(0, numcases):
	text_file.write(main(1+addnum, t+1) + '\n')
	add = s[1+addnum].split()
	for i in add:
		addnum += int(i)
	addnum += 1
text_file.close()