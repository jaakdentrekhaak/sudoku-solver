# Sudoku is being presented by a 9x9 matrix


def check_row(matrix, row):
	'''
	Check if the current row contains each number maximum one time.
	If there is 'None' in the row, it will negotiate this.
	'''
	# Get the numbers of the current row
	row_entries = matrix[row].copy()
	original_length = len(row_entries)
	row_entries_copy = row_entries.copy()

	# Remove 'None' in the row
	nb_of_none = 0

	for element in row_entries_copy:
		if element is None:
			row_entries.remove(element)
			nb_of_none += 1

	# Remove duplicate numbers
	row_entries_set = set(row_entries)

	# Check if there were any duplicates in the row
	if len(row_entries_set) == original_length - nb_of_none:
		return True
	else:
		return False


# test_check_row_matrix1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 2, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, None, 7, 8, 9]]
# assert check_row(test_check_row_matrix1, 0)
# assert not check_row(test_check_row_matrix1, 1)
# assert check_row(test_check_row_matrix1, 2)


def check_col(matrix, col):
	'''
		Check if the current column contains each number maximum one time.
		If there is 'None' in the column, it will negotiate this.
		'''
	# Get the numbers of the current column
	col_entries = []

	for row in matrix:
		col_entries.append(row[col])

	original_length = len(col_entries)
	col_entries_copy = col_entries.copy()

	# Remove 'None' in the column
	nb_of_none = 0

	for element in col_entries_copy:
		if element is None:
			col_entries.remove(element)
			nb_of_none += 1

	# Remove duplicate numbers
	col_entries_set = set(col_entries)

	# Check if there were any duplicates in the col
	if len(col_entries_set) == original_length - nb_of_none:
		return True
	else:
		return False


# test_check_col_matrix1 = [[1, 2, None], [2, 2, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 1], [9, 1, 2]]
# assert check_col(test_check_col_matrix1, 0)
# assert not check_col(test_check_col_matrix1, 1)
# assert check_col(test_check_col_matrix1, 2)


def roster(row, col):
	'''
	If you divide the sudoku board into 9 3x3 squares, check in which square the current position is.
	The squares are numbered from 0 to 8 in the same way as you read.
	'''
	# Determine the row (horizontal) and column (vertical) of the given position inside the big 3x3 square (which contains 9 3x3 squares)
	horizontal = int((row-row%3)/3)
	vertical = int((col-col%3)/3)

	return horizontal*3+vertical



def check_square(matrix, row, col):
	'''
	This function checks if every number only occurs once in a the 3x3 square where the position (row, col) is in.
	If there is 'None' in the square, it will ignore that.
	There are 9 such 3x3 squares on the sudoku board numbered from 0 to 8.
	'''

	square = []

	position = roster(row, col)

	# TODO: shrink this

	if position == 0:
		for a in range(0, 3):
			for b in range(0, 3):
				square.append(matrix[a][b])
	elif position == 1:
		for a in range(0, 3):
			for b in range(3, 6):
				square.append(matrix[a][b])
	elif position == 2:
		for a in range(0, 3):
			for b in range(6, 9):
				square.append(matrix[a][b])
	elif position == 3:
		for a in range(3, 6):
			for b in range(0, 3):
				square.append(matrix[a][b])
	elif position == 4:
		for a in range(3, 6):
			for b in range(3, 6):
				square.append(matrix[a][b])
	elif position == 5:
		for a in range(3, 6):
			for b in range(6, 9):
				square.append(matrix[a][b])
	elif position == 6:
		for a in range(6, 9):
			for b in range(0, 3):
				square.append(matrix[a][b])
	elif position == 7:
		for a in range(6, 9):
			for b in range(3, 6):
				square.append(matrix[a][b])
	elif position == 8:
		for a in range(6, 9):
			for b in range(6, 9):
				square.append(matrix[a][b])

	# Remove 'None' in the square
	square_copy = square.copy()
	nb_of_none = 0

	for element in square_copy:
		if element is None:
			square.remove(element)
			nb_of_none += 1

	# Remove duplicates
	square_set = set(square)

	# Check if there were duplicates
	if len(square_set) == 9 - nb_of_none:
		return True
	else:
		return False

# test_check_square_matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
# 							 [4, 5, 6, 5, 6, 7, 8, 9, 1],
# 							 [7, 8, 9, 6, 7, 8, 9, 1, 2],
# 							 [4, 5, 6, 7, 8, 9, 1, 2, 3],
# 							 [5, 6, 7, 8, 9, 1, 4, 5, 6],
# 							 [6, 7, 8, 9, 1, 2, 7, 8, 7],
# 							 [7, 8, 9, 1, 2, 3, 4, 5, 6],
# 							 [8, 9, 1, 2, 3, 4, 5, 6, 7],
# 							 [9, 1, 2, 3, 4, 5, 6, 7, 8]]
# assert check_square(test_check_square_matrix, 1, 1)
# assert check_square(test_check_square_matrix, 2, 2)
# assert not check_square(test_check_square_matrix, 2, 3)
# assert not check_square(test_check_square_matrix, 8, 8)
# assert not check_square(test_check_square_matrix, 8, 0)
# assert not check_square(test_check_square_matrix, 5, 6)
# assert not check_square(test_check_square_matrix, 3, 8)


def coordinates_of_position(position):
	'''
	Takes the given position and gives back the corresponding coordinates of that position on the board.
	The coordinates are (row, column)
	'''
	
	row = int((position-position%9)/9)
	col = position%9	

	return (row, col)


# assert coordinates_of_position(80) == (8, 8)
# assert coordinates_of_position(36) == (4, 0)


def solve(matrix, position=0):
	mat = matrix.copy()

	# There are 9x9=81 positions on the sudoku board and we read them from left to right, top to bottom
	# If every position is covered: return the resulting matrix
	if position > 80:
		return mat

	co = coordinates_of_position(position)

	for input in range(1, 10):
		if mat[co[0]][co[1]] is None:
			mat[co[0]][co[1]] = input
			if check_row(mat, co[0]) and check_col(mat, co[1]) and check_square(mat, co[0], co[1]):
				rec_sol = solve(mat, position + 1)
				if rec_sol is not None:
					return rec_sol
				else:
					mat[co[0]][co[1]] = None
			else:
				mat[co[0]][co[1]] = None

		else:
			return solve(mat, position + 1)
	else:
		return None

# test_matrix = [[None, None, None, None, None, 3, None, None, None],
# 			   [3, None, 8, 4, None, 7, 1, None, 5],
# 			   [None, None, 2, None, 9, 1, None, None, 6],
# 			   [2, None, 6, None, None, 8, 4, None, None],
# 			   [9, None, 5, None, 7, None, None, 1, 3],
# 			   [7, None, 4, 9, 3, None, None, None, 2],
# 			   [1, None, None, None, 6, None, 7, None, 8],
# 			   [None, None, None, None, None, None, 9, None, None],
# 			   [6, None, 7, None, 8, 9, 5, 3, None]]

#
# test_matrix_sol = 	[[4, 9, 1, 6, 5, 3, 2, 8, 7],
# 			   		[3, 6, 8, 4, 2, 7, 1, 9, 5],
# 			   		[5, 7, 2, 8, 9, 1, 3, 4, 6],
# 			   		[2, 3, 6, 5, 1, 8, 4, 7, 9],
# 			   		[9, 8, 5, 2, 7, 4, 6, 1, 3],
# 			   		[7, 1, 4, 9, 3, 6, 8, 5, 2],
# 			   		[1, 4, 9, 3, 6, 5, 7, 2, 8],
# 			   		[8, 5, 3, 7, 4, 2, 9, 6, 1],
# 			   		[6, 2, 7, 1, 8, 9, 5, 3, 4]]
#
# assert solve(test_matrix) == test_matrix_sol