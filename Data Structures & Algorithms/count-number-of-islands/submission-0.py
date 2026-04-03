class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0

        # 今いる陸地と，つながっている陸地をすべて沈める
        def sink_island(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return
            
            grid[r][c] = "0"
            sink_island(r-1, c)
            sink_island(r+1, c)
            sink_island(r, c+1)
            sink_island(r, c-1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # もし陸地（'1'）を発見したら！
                if grid[r][c] == '1':
                    count += 1         # 島を1つ見つけたのでカウントアップ
                    sink_island(r, c)  # その島を連鎖的にすべて海に沈める（二重カウント防止）
        
        return count