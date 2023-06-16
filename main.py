def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    def resolve(board: list[list[int]]) -> bool:
        i, j = encontra_célula_vazia(board)
        if i == None or j == None:
            return True  # Já está resolvido nesse caso

        for num in range(1, 10):
            board[i][j] = num  # Aloca um número no espaço necessário

            if is_valid(board) and resolve(board): #De forma iterada resolve adiciona números
                return True

            board[i][j] = 0 #Refaz a última jogada

        return False

    if resolve(board):
        return board
    else:
        raise ValueError

def is_valid(board: list[list[int]]) -> bool:
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                for col in range(9):
                    if col != j and board[i][col] == num:
                        return False

                for row in range(9):
                    if row != i and board[row][j] == num:
                        return False

                start_row = 3 * (i // 3)
                start_col = 3 * (j // 3)
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        if (row != i or col != j) and board[row][col] == num:
                            return False

    return True

def encontra_célula_vazia(board: list[list[int]]) -> tuple[int, int]:

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None
