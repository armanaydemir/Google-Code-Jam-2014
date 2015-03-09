s = [item.rstrip('\n') for item in open('smalls.txt','r').readlines()]
num = int(s[0])
def main(i,z):
	row = []
	col = []
	sel = int(s[i])
	row = s[sel+i].split()
	cho = int(s[i+5])
	col = s[cho+i+5].split()
	let = 0
	for r in row:
		for c in col:
			if c == r:
				card = r
				let+=1
	if let == 0:
		print 'Case #' + str(z) + ': Volunteer cheated!'
	elif let > 1:
		print 'Case #' + str(z) + ': Bad magician!'
	else:
		print 'Case #' + str(z) + ': ' + str(card)

for t in range(0,num):
	main(1+(10*t), t+1)
	