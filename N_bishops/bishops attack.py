#Place exactly N bishops on an N×N chessboard such that no two bishops attack each other diagonally.
#Print one valid board configuration using 1s and 0s.
def place_bishops(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    used_main_diagonal = set()
    used_anti_diagonal = set()
    count = 0

    for row in range(n):
        for col in range(n):
            main_diag = row - col
            anti_diag = row + col

            if main_diag not in used_main_diagonal and anti_diag not in used_anti_diagonal:
                board[row][col] = 1
                used_main_diagonal.add(main_diag)
                used_anti_diagonal.add(anti_diag)
                count += 1
                if count == n:
                    break
        if count == n:
            break

   
    for row in board:
        print(' '.join(str(cell) for cell in row))

n = int(input("Enter the size of the board: "))
place_bishops(n)
