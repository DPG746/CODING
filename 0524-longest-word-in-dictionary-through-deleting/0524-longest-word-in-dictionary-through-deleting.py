class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x),x))
        for word in dictionary:
            i=0
            for char in s:
                if i<len(word) and char==word[i]:
                    i+=1
                if i==len(word):
                    break
            if i==len(word):
                return word
        return ""