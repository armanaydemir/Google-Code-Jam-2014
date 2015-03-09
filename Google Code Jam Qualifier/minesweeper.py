s = [item.rstrip('\n') for item in open('input.txt','r').readlines()]
numcases = int(s[0])
def main(r,c,m):
	global grid
	grid = []
	for t in range(0,r):
		row = []
		for t in range(0,c):
			row.append('0')
		grid.append(row)
	if r > m:
		for t in range(0,m):
			grid[0][t] = '*'
	elif c > m:
		for t in range(0,m):
			grid[t][0] = '*'		
	else:
		mien = True
		rownum = 0
		minenum = 0
		while mien:
			for t in range(0,r):
				minenum += 1
				if minenum > m:
					mien = False
					break
				grid[rownum][t] = '*'
			rownum += 1
	for i in range(0,r):
		for t in range(0,c):
			prox = False
			if grid[i][t] == '0':
				tr = [0]
				ir = [0]
				try:
					fake = grid[i][t-1]
					tr.append(-1)
				except:
					try:
						fake = grid[i][t+1]
						tr.append(1)
					except:
						try:
							fake = grid[i-1][t]
							ir.append(-1)
						except:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
						else:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
					else:
						try:
							fake = grid[i-1][t]
							ir.append(-1)
						except:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
						else:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
				else:
					try:
						fake = grid[i][t+1]
						tr.append(1)
					except:
						try:
							fake = grid[i-1][t]
							ir.append(-1)
						except:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
						else:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
					else:
						try:
							fake = grid[i-1][t]
							ir.append(-1)
						except:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
						else:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
				#print ir
				#print tr
				for d in tr:
					for q in ir:
						if grid[i+q][t+d] == '*':
							prox = True
			if prox:
				grid[i][t] = '1'
				#print '======='
			#else:
				#print '-------'
	for i in grid:
		print i
	print check(r,c,m)
	
	
def check(r,c,m):	
	impos = True
	for i in range(0,r):
		for t in range(0,c):
			prox = True
			if grid[i][t] == '1':
				tr = [0,-1,1]
				ir = [0,-1,1]
				trr = []
				irr = []
				for d in tr:
					if t+d >= 0 and t+d <= c-1:
						trr.append(d)
				for d in ir:
					if i+d >= 0 and i+d <= r-1:
						irr.append(d)
				"""try:
					fake = grid[i][t-1]
					tr.append(-1)
				except:
					try:
						fake = grid[i][t+1]
						tr.append(1)
					except:
						try:
							fake = grid[i-1][t]
							ir.append(-1)
						except:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
						else:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
					else:
						try:
							fake = grid[i-1][t]
							ir.append(-1)
						except:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
						else:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
				else:
					try:
						fake = grid[i][t+1]
						tr.append(1)
					except:
						try:
							fake = grid[i-1][t]
							ir.append(-1)
						except:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
						else:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
					else:
						try:
							fake = grid[i-1][t]
							ir.append(-1)
						except:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0
						else:
							try:
								fake = grid[i+1][t]
								ir.append(1)
							except:
								fake = 0"""
				ir = irr
				tr = trr
				#print ir
				#print tr
				endall = []
				for d in tr:
					for q in ir:
						endall.append(grid[i+q][t+d])
						print str(i) + ', ' + str(t)
						print str(q) + ', ' + str(d)
						print grid[i+q][t+d]
						print '-----'
				for op in endall:
					if op == 0:
						break
	if impos:
		return True
		
	
		
main(3,3,4)
	

	