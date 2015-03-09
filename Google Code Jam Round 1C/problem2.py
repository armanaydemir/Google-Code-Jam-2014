s = [item.rstrip('\n') for item in open('prob2in.txt','r').readlines()]
numcases = int(s[0])
text_file = open('prob2out.txt', 'w')

def main(grid, case):
	grid = grid.split(' ')
	print grid
	if grid[2] <= 4:
		return 'Case #' + str(case) + ': ' + str(grid[2])
	
	
			
		


for t in range(0, numcases):
	text_file.write(main(s[1+t], t+1) + '\n')

text_file.close()