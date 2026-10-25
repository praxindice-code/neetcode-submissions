class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} 
        final_array = [[] for _ in range(len(strs))]


        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in seen:
                final_array[seen["".join(sorted(strs[i]))]].append(strs[i])
            else:
                seen["".join(sorted(strs[i]))] = i
                final_array[seen["".join(sorted(strs[i]))]].append(strs[i]) 
        filtered_matrix = [item for item in final_array if len(item) > 0]
        return filtered_matrix 