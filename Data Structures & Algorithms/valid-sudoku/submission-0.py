class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        sqrSet = [set() for _ in range(9)]

        for row in range(n):
            for col in range(n):
                if(board[row][col] != "."):
                    if(board[row][col] in rowSet[row]):
                        return False
                    rowSet[row].add(board[row][col])

                    if(board[row][col] in colSet[col]):
                        return False
                    colSet[col].add(board[row][col])

                    sqrIndex = (row // 3) * 3 + (col // 3)
                    if(board[row][col] in sqrSet[sqrIndex]):
                        return False
                    sqrSet[sqrIndex].add(board[row][col])


        return True
        