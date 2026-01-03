from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]

        for i in strs[1:]:
            while lcp and not i.startswith(lcp):
                lcp = lcp[:-1]
            if not lcp:
                return ""

        return lcp


obj = Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))