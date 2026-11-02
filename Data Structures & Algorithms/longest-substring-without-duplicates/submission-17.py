class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        l = 0 
        ans = 0 
        seen = set()
        while l <= r and r < len(s):
            if s[r] in seen:
                ans = max(ans, r-l)
                seen.remove(s[l])                
                l += 1 
            else:
                seen.add(s[r])
                r += 1 
            ans = max(ans, r - l )
        return ans 
            