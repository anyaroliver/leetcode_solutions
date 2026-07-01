# Problem number: 4 on LeetCode
from typing import List

class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i

            Aleft  = A[i-1] if i else float("-inf")
            Aright = A[i]   if i < m else float("inf")
            Bleft  = B[j-1] if j else float("-inf")
            Bright = B[j]   if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright :
               left_max = max(Aleft, Bleft)
               right_min = min(Aright, Bright)
               
               return left_max if(m + n) % 2 else (left_max + right_min) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

sol = Solution()
print(sol.findMedianSortedArrays([1,3], [2]))