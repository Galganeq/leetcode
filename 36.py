test =[["5","3","3",".","7",".",".",".","9"]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """


        #Row
        for board_current in board:
            check = set(board_current)
            for n in check:
                repeats = board_current.count(n)
                if ((repeats > 1) and (n != '.')):
                    return False
        
        #Column

        for n in range(9):
            board_current1 = []
            for k in range(9):
                board_current1.append(board[k][n])
            check = set(board_current1)
            for l in check:
                repeats = board_current1.count(l)
                if ((repeats > 1) and (l != '.')):
                    return False

        #Square

        for a in [0,3,6]:
             for b in [0,3,6]:
                board_current3 = []

                for c in range(a,3+a):
                    for d in range(b,3+b):
                        board_current3.append(board[c][d])

                check = set(board_current3)

                for l in check:
                    repeats = board_current3.count(l)
                    if ((repeats > 1) and (l != '.')):
                        return False
        
(isValidSudoku(test))
