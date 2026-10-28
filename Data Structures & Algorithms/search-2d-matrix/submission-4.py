class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // COLS # We use COLS to round divide because each row contains COLS elements
            col = mid % COLS
            if matrix[row][col] < target:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        return False