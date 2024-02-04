"""
36. Valid Sudoku
Medium
Topics
Companies
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Create 3 different hash sets using defaultdict so key == row number, value is a set of all values in row. 
        # 3rd set will refer to each 3x3 box. We can refer to this using [row // 3][column // 3]

        #Iterate through each row & column and add each new number to the appropriate 
        #row, column, box set. 
        #If we've already seen that element before in the row, column, or box, then false. 

        columns = collections.defaultdict(set)
        rows    = collections.defaultdict(set)
        boxes   = collections.defaultdict(set)

        #Loop through rows
        for row in range(9):
            #Loop through columns
            for col in range(9):
                if board[row][col] == ".":
                    continue
                #Check if current number in the current row set, column set, or box set. 
                if (board[row][col] in rows[row] or
                    board[row][col] in columns[col] or
                    board[row][col] in boxes[(row // 3, col // 3)]):
                    return False
                columns[col].add(board[row][col])
                rows[row].add(board[row][col])
                boxes[row // 3, col // 3].add(board[row][col])
        return True
