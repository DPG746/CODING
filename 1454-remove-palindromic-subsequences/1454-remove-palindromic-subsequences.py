class Solution:
    def removePalindromeSub(self, s: str) -> int:
        s=list(s)
        l=0
        r=len(s)-1

        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return 2
        return 1