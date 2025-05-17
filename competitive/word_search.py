def word_search(board,word):
    row_size = len(board)
    column_size = len(board[0])

    def dfs(row,column,word_index):

        if row >= row_size or column >= column_size or row < 0 or column < 0 or board[row][column] != word[word_index]:
            return False

        if word_index == len(word)-1:
            return True

        tmp, board[i][j] = board[i][j],"/"
        result =  (
            dfs(row+1,column,word_index+1) or
            dfs(row-1,column,word_index+1) or
            dfs(row,column+1,word_index+1) or
            dfs(row,column-1,word_index+1)
        )
        board[i][j] = tmp
        return result

    for i in range(row_size):
        for j in range(column_size):
            if board[i][j] == word[0]:
                if dfs(i,j,0):
                    return True

    return False


if __name__ == "__main__":
    print(word_search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABFCSF"))
