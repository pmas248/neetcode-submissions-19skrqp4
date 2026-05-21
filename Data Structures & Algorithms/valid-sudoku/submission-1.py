class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == ".": continue
                if curr in row[r] or \
                curr in col[c] or \
                curr in grid[r//3, c//3]:
                    return False
                
                row[r].add(curr)
                col[c].add(curr)
                grid[r//3, c//3].add(curr)
        return True