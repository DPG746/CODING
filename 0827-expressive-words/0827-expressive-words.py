class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(x):
            i = j = 0   # two pointers: i for s, j for query word x
            while i < len(s) and j < len(x):
                
                # Count group length in s
                counts = 1
                while i < len(s)-1 and s[i] == s[i+1]:
                    i += 1
                    counts += 1
                
                # Count group length in x
                countx = 1
                while j < len(x)-1 and x[j] == x[j+1]:
                    j += 1
                    countx += 1
                
                # If chars differ => not stretchy
                if s[i] != x[j]: 
                    return 0
                
                # Move both pointers to next char
                i += 1
                j += 1

                # If word has more letters than s → invalid
                if counts < countx: 
                    return 0
                
                # If s group > word group, then s group must be ≥ 3 
                if countx != counts and counts <= 2:
                    return 0
            
            # Both strings must be fully consumed
            return 1 if i >= len(s) and j >= len(x) else 0
        
        return sum(check(x) for x in words)