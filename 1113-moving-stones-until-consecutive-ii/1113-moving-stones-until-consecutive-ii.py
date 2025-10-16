class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n=len(stones)

        max_moves = max(stones[-1]-stones[1],stones[-2]-stones[0])-(n-2)

        min_moves=n
        left=0

        for right in range(n):
            while stones[right]-stones[left]+1>n:
                left+=1
            stones_in_window=right-left+1
            moves_needed=n-stones_in_window

            if moves_needed == 1 and stones[right]-stones[left]+1==n-1:
                moves_needed = 2
            
            min_moves=min(min_moves, moves_needed)

        return [min_moves, max_moves]