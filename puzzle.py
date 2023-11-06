import copy
def validate_board(board: list) -> bool:
    """
    The validate_board(board) function should return a boolean value.
    he cells of the playing field must be filled in according to the following rules before the game starts:
    The coloured cells of each row must contain the digits from 1 to 9 without repetition.
    The coloured cells of each column must contain digits from 1 to 9 without repetition.
    Each block of cells of the same colour must contain digits from 1 to 9 without repetition.

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["****5****", "***1 ****", "**  3****", "* 4  ****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["****5****", "***1 ****", "**  3****", "* 4  ****", "     9   ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    if isinstance(board, list):
        for string in board:
            string = list(string)
            for ch in string:
                if ch != '*' and ch != ' ':
                    if string.count(ch) != 1:
                        return False
                    else:
                        continue

        for i in range(9):
            col = [board[j][i] for j in range(9) if board[j][i] != '*' and board[j][i] != ' ']
            for ch in col:
                if col.count(ch) != 1:
                    return False
                else:
                    continue
        board1 = copy.deepcopy(board)
        rev = copy.copy(board)
        rev.reverse()
        ind = 0
        for line1 in rev:
            cline = []
            line12 = line1[ind:]
            for i in line12:
                if i != ' ' and i != '*':
                    cline.append(i)
                else:
                    continue
            board1.remove(line1)
            board.remove(line1)
            for line2 in board1:
                line2 = list(line2)
                if line2[ind] != ' ' and line2[ind] != '*':
                    cline.append(line2[ind])
                else:
                    continue
            for j in cline:
                if cline.count(j) > 1:
                    return False
                else:
                    continue
            ind += 1
        return True
        
import doctest
print(doctest.testmod())
# board1 = []
            # for i in range(len(board)):
            #     board1.append(board[i][ind:])
            # rev = copy.copy(board1)
            # rev.reverse()