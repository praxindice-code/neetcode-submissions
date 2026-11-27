class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ub = len(nums) - 1 
        lb = 0 


        while lb <= ub: 
            new_index = (ub + lb)//2

            if nums[new_index] == target:
                return new_index
            elif nums[new_index] < target:
                lb = new_index + 1
            elif nums[new_index] > target:
                ub = new_index - 1
        return -1 
        
