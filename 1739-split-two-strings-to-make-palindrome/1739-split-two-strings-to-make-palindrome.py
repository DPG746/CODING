class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_palindrome(s,l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        def check(x,y):
            l,r=0,len(x)-1
            while l<r and x[l]==y[r]:
                l+=1
                r-=1
            return is_palindrome(x,l,r) or is_palindrome(y,l,r)
        return check(a,b) or check(b,a)
