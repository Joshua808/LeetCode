from typing import List
# Things to do
# CHECK FOR DUPLICATE TRIPLETS
# WRITE THREE SUM FUNCTION TO ITERATE THROUGH REST OF THE LIST

class Solution:
    def twoSum(self, nums: List[int], target: int, countf_value:int, countf:int) -> List[int]:
        dic = {}
        output = []
        for count, value in enumerate(nums):
            print(value)
            subtract = target - value
            if count != countf:
                if subtract in dic:
                    print(countf_value, nums[count],subtract)
                    output.append([countf_value, nums[count], subtract])
            dic[value] = count

        print(output)
        return output


    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     output = []
    #
    #     if len(nums) < 3:
    #         return output
    #
    #     for count, value in enumerate(nums):
    #         zero_sum = 0 - value
    #
    #         output = self.twoSum(nums, zero_sum, value, count)


a = Solution()
a.twoSum([-1,0,1,2,-1,-4],-1, 1, 0)