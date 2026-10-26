class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_i, right_i = 0, len(matrix) - 1
        while left_i <= right_i:
            mid_i = left_i + (right_i - left_i) // 2
            curRow = matrix[mid_i]

            left_j, right_j = 0, len(curRow) - 1
            if target > curRow[right_j]:     # if the target is larger than all nums in the current row
                left_i = mid_i + 1
            elif target < curRow[left_j]:    # if the target is smaller than all nums in the current row
                right_i = mid_i - 1
            else:
                while left_j <= right_j:
                    mid_j = left_j + (right_j - left_j) // 2
                    if target < curRow[mid_j]:
                        right_j = mid_j - 1
                    elif target > curRow[mid_j]:
                        left_j = mid_j + 1
                    else:
                        return True
                break
        
        return False
        