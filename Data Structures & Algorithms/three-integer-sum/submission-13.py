class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        #anchor 1, then run 2 sum on 
        seen = set()
        for i in range(len(nums)-2):
            if nums[i] in seen:
                continue
            seen.add(nums[i])

            target = 0 - nums[i]
            l = i + 1 
            r = len(nums) - 1 


            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1 
                elif nums[l] + nums[r] > target:
                    r -= 1 
                else:
                    answer.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[r] == nums[r-1]:
                        r-=1 
                    while l < r and nums[l] == nums[l+1]:
                        l+=1 
                    l += 1 
                    r -= 1 
                    
        

        return answer 