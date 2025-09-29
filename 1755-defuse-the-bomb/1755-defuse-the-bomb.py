from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        result = [0] * n
        if k > 0:
            # For each position i, sum the next k elements (circular)
            for i in range(n):
                for j in range(1, k + 1):
                    result[i] += code[(i + j) % n]
        else:
            # For negative k, sum the previous |k| elements (circular)
            m = -k
            for i in range(n):
                for j in range(1, m + 1):
                    result[i] += code[(i - j) % n]
        
        return result