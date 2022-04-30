def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsList = nums
        for index, value in enumerate(nums):
            for ind, val in enumerate(numsList):
                if index!=ind:
                    if target == value+val:
                        return [index, ind]
