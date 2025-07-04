class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        result = ""
        base = strs[0]
        if len(strs) == 0:
            return ""
        for i in range(0, len(base)):
            for words in strs[1:]:
                if i == len(words) or words[i] != base[i]:
                    return result
            result += base[i]
        return result    

