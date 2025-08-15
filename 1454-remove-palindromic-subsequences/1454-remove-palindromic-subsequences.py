class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
 # Internally: loop from index 3 → 0, build "abba"
