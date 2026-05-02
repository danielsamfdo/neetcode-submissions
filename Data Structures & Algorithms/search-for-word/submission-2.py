class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        m = len(board)
        n = 0 if m == 0 else len(board[0])
        def recurse(board, i, j, word, idx):
            nonlocal visited
            if idx == len(word):
                return True
            
            
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                x = dx+i
                y = dy+j
                if ((x,y) not in visited) and min(x,y) >=0 and x < m and y < n and board[x][y] == word[idx]:
                    visited.add((x,y))
                    if recurse(board, x,y,word,idx+1):
                        return True
                    visited.remove((x,y))
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if recurse(board, i, j, word, 1):
                        return True
                    visited.remove((i,j))
        return False
