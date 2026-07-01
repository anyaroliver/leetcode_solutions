from collections import deque
import heapq
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def in_bounds(r, c):
            return 0 <= r < n and 0 <= c < n

        # Multi-source BFS to compute distance from the nearest thief
        def precompute():
            dist = {}
            q = deque()

            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                        dist[(r, c)] = 0
                        q.append((r, c))

            while q:
                r, c = q.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if in_bounds(nr, nc) and (nr, nc) not in dist:
                        dist[(nr, nc)] = dist[(r, c)] + 1
                        q.append((nr, nc))

            return dist

        min_dist = precompute()

        # Max heap: (-safeness, row, col)
        max_heap = [(-min_dist[(0, 0)], 0, 0)]
        visited = {(0, 0)}

        while max_heap:
            safeness, r, c = heapq.heappop(max_heap)
            safeness = -safeness

            if (r, c) == (n - 1, n - 1):
                return safeness

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if in_bounds(nr, nc) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_safeness = min(safeness, min_dist[(nr, nc)])
                    heapq.heappush(max_heap, (-new_safeness, nr, nc))

        return -1
    

if __name__ == "__main__":
    sol = Solution()

    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    result = sol.maximumSafenessFactor(grid)
    print("Maximum Safeness Factor:", result)