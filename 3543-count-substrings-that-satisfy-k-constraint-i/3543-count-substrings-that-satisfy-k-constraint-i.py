class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res=0
        n=len(s)
        for i in range(n):
            zero=0
            one=0
            for j in range(i,n):
                if s[j]=='0':
                    zero+=1
                if s[j]=='1':
                    one+=1
                if zero<=k or one<=k :
                    res+=1
        return res