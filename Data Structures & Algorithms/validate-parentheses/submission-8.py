class Solution:
    def isValid(self, s: str) -> bool:
        correspondence = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        queue = [] 



        for i in range(len(s)):
            if s[i] in list(correspondence.keys()):
                queue.append(s[i])
            elif s[i] in list(correspondence.values()) and len(queue) != 0:
                if correspondence[queue[-1]] == s[i]:
                    queue.pop()
                else:
                    return False 
            else:
                return False
            
        if len(queue) != 0:
            return False
        return True
