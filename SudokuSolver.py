sudoku=[[0,8,3,0,0,9,0,0,0],[0,5,0,0,0,0,9,0,0],[0,0,0,0,0,5,0,0,4],[0,0,9,7,6,0,0,0,3],[3,0,0,0,0,0,0,0,1],[2,0,0,0,9,3,5,0,0],[9,0,0,6,0,0,0,0,0],[0,0,4,0,0,0,0,3,0],[0,0,0,8,0,0,7,1,0]]

"""sudoku=[]

print("Enter the elements Row-wise separated by a space \n blank spaces entered as a 0")
for i in range(9):
	try:
		sudoku.append(list(map(int,input(f"Enter row {i+1} ").split())))
	except ValueError:
		print("Enter an integer between 1 and 9")"""




empty_positions=[]
current_pos=(0,0)
r,c=-1,-1
ptr=0

def disp_board(box):
	for j in range(9):
		print(box[j])
	print("\n"*2)
	print("-"*30)

def checkEmpty(box,i,j):
	if box[i][j]==0:		
		return True
	else :
		return False

def move(i,j):
	if i==-1 and j==-1:
		return 0,0
	if j<8:
		j+=1
	elif j==8:
		if i==8:
			return 9,8
		else:
			i+=1
			j=0
	return i,j


def genBox(box,i,j):
	Box=[]
	triplets=[(0,1,2),(3,4,5),(6,7,8)]
	rw_ind,cl_ind=0,0
	for ind,trp in enumerate(triplets):
		if i in trp:
			rw_ind=ind
		if j in trp:
			cl_ind=ind
	for m in triplets[rw_ind]:
		for n in triplets[cl_ind]:
			Box.append(box[m][n])
	return Box


def fillTheSquare(box,i,j,bk=False):#To find a compatable number and fill the square. Return True if a compatable is found
	init_num=1
	if bk:
		init_num=box[i][j]+1
	val=0
	for num in range(init_num,10):
		val=num
		if num in box[i]:
			continue
		elif num in [box[k][j] for k in range(9)]:
			continue
		elif num in genBox(box,i,j):
			continue
		else:
			box[i][j]=num
			return True
	if not(bk):
		if val==9 :
			return False
	else:
		if val==10-init_num:
			return False
	

backtracking=False

disp_board(sudoku)

while True:
	if not(backtracking):
		r,c=move(r,c)
		if r>8 or c>8:
			break
		if checkEmpty(sudoku,r,c):
			empty_positions.append((r,c))
			current_pos=(r,c)
			if fillTheSquare(sudoku,r,c):
				continue
			else:
				ptr=len(empty_positions)-2
				backtracking=True
	else:
		r,c=empty_positions[ptr]
		if  ptr<=len(empty_positions)-1:
			if fillTheSquare(sudoku,r,c,True):
				ptr+=1
				if ptr==len(empty_positions):
					backtracking=False
				else:	
					r,c=empty_positions[ptr]
			else:
				sudoku[r][c]=0
				ptr-=1
				continue


disp_board(sudoku)








