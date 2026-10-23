class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n 
        L = 1 
        R = 1 
        for i in range(n):
            answer[i] =answer[i] * L 
            L *= nums[i]

        for i in range(n-1, -1, -1):
            answer[i] = answer[i] * R 
            R *= nums[i]  
        return answer 