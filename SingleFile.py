def exist(board, word):
    m, n = len(board), len(board[0])
    
    # Helper function to perform DFS (Depth First Search)
    def dfs(i, j, index):
        # If we have matched the whole word
        if index == len(word):
            return True
        
        # Check if out of bounds or current cell does not match the word's character
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
            return False
        
        # Mark the current cell as visited by changing its value
        temp = board[i][j]
        board[i][j] = '#'
        
        # Explore the four possible directions (up, down, left, right)
        res = (dfs(i + 1, j, index + 1) or  # move down
               dfs(i - 1, j, index + 1) or  # move up
               dfs(i, j + 1, index + 1) or  # move right
               dfs(i, j - 1, index + 1))    # move left
        
        # Restore the cell back to its original state
        board[i][j] = temp
        
        return res
    
    # Iterate through every cell in the grid
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:  # If the first character matches
                if dfs(i, j, 0):  # Try to find the word starting from (i, j)
                    return True
    
    return False

# Read inputs
m, n = map(int, input().split())  # Read the dimensions of the board
board = [input().split() for _ in range(m)]  # Read the board
word = input().strip()  # Read the word to search for

# Output the result
print("True" if exist(board, word) else "False")
