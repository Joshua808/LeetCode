
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        number_of_ones = [0] * (n+1)
        offset = 1
        for x in range(1, n+1):

            if x == offset * 2:
                offset = x

            number_of_ones[x] = 1+number_of_ones[x-offset]

        return number_of_ones

counting_bits = Solution()
counting_bits.countBits(0)

