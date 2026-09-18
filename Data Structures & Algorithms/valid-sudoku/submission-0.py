class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check horizontal
        for row in board:
            record = []
            for element in row:
                if element != "." and element in record:
                    return False
                else:
                    record.append(element)
        
        #check vertical
        for i in range(9):
            record = []
            for row in board:
                if row[i] != "." and row[i] in record:
                    return False
                else:
                    record.append(row[i])

        #check 3 x 3 subbox
        hashy = defaultdict(list)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                x = col // 3
                y = row // 3

                if board[row][col] in hashy[(x, y)]:
                    return False
                else:
                    hashy[(x,y)].append(board[row][col])
        
        return True


                

