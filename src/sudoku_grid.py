def row_correct(sudoku: list, row_no: int) -> bool:
    """
        This function checks whether a row is filled correctly in sudoku grid.
    """
    numbers = 0
    checklist = []
    length = len(sudoku[row_no]) - sudoku[row_no].count(0)
    for each in sudoku[row_no]:
        if each != 0 and each not in checklist:       
            checklist.append(each)
    if length == len(checklist):
        return True 
    else: 
        return False
    
    
def column_correct(sudoku: list, column_no: int) -> bool:
    """
        This function checks whether a column is filled correctly in sudoku grid.
    """
    
    numbers = 0
    checklist = []
    col = []
    for each in sudoku:
        if each[column_no] != 0:
            col.append(each[column_no])
    for i in col:    
        if i != 0 and i not in checklist:       
            checklist.append(i)
    if len(col) == len(checklist):
        return True 
    else: 
        return False
    

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    """    
        This function checks whether a 3x3 block is filled correctly in sudoku grid. 
    """
    block = []
    check = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            if sudoku[i][j] != 0:
                block.append(sudoku[i][j])
    
    for i in block:
        if i not in check:
            check.append(i)
    
    if len(check) == len(block):
        return True 
    else:
        return False


def sudoku_grid_correct(sudoku: list) -> bool:
    """    
        This function checks whether a 9x9 sudoku grid is filled correctly. 
    """
    for row in range(9):    
        if row_correct(sudoku, row) == False:
            return False
    for col in range(9):
        if column_correct(sudoku, col) == False:
            return False
    for i in range(0,7,3):
        for j in range(0,7,3):
            if block_correct(sudoku, i, j) == False:
                return False
    return True 

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]]

    print(sudoku_grid_correct(sudoku2))