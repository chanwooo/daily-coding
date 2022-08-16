from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, row, col):

            if col >= len(grid[0]) \
                    or col < 0 \
                    or row >= len(grid) \
                    or row < 0 \
                    or grid[row][col] != "1":
                return

            if grid[row][col] == "1":
                grid[row][col] = "#"

            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)

        answer = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # print(row,col, grid[row][col])
                if grid[row][col] == "1":
                    dfs(grid, row, col)
                    answer += 1

        return answer


print(Solution.numIslands(Solution, [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(Solution.numIslands(Solution, [["1", "0", "1", "1", "0", "1", "1"]]))
