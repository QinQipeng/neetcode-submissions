class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2 # 0-indexed, not referring to the number of el to the left
            j = half - i - 2 # let's say i == 2. This refers that there are 2 + 1 = 3 element to i. j would them be half - 2 = 4, given that half == 2. This would not be correct since j as 4 indicates 5 elements from list B, thus needs remove the 1-index shift from both lists to map into proper index
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                return min(Aright, Bright) if total % 2 else (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1
        