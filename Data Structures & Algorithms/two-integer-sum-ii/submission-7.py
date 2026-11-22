class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        r = len(numbers) - 1 
        l = 0
        while r and l < r and r < n:
            if numbers[r] + numbers[l] < target:
                l += 1 
            elif numbers[r] + numbers[l] > target:
                r -=1 
            elif numbers[r] + numbers[l] == target:
                return [l+1,r+1]
