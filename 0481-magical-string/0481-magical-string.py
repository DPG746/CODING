class Solution:
    def magicalString(self, n: int) -> int:
    
        if n == 0:
            return 0
        if n <= 3:
            return 1  # Because "122" has only one '1'

        s = [1, 2, 2]  # Start of magical string
        count = 1      # We already have one '1'
        i = 2          # Index in s that tells how many times to add next number
        num = 1        # Next number to append (alternates between 1 and 2)

        while len(s) < n:
            for _ in range(s[i]):
                s.append(num)
                if num == 1 and len(s) <= n:
                    count += 1
            num = 3 - num  # Toggle between 1 and 2
            i += 1

        return count
