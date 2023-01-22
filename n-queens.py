

class QueensProblem:
    def __init__(self, n):
        self.n = n

        # initialize columns and rows for n number of queens
        self.chess_table = [[None for i in range(n)] for j in range(n)]
    
    def solve_queens(self):

        # start with the first queen w/ index, 0
        if self.solve(0):
            self.print_queens()
        else:
            print('There is no solution to the problem...')
    
    def solve(self, col_index):

        # BASE CASE
        # if there's a 3X3 board and we've placed all 3 queens w/o issue, we've solved the problem
        if col_index == self.n:
            return True
        
        # find a position for queen (col_index) within a given column
        for row_index in range(self.n):
            if self.is_place_valid(row_index, col_index):
                # 1 means that there is a queen at the given location
                self.chess_table[row_index][col_index] = 1

                # we try to find the position of the next queen in the next column
                if self.solve(col_index + 1):
                    return True
                
                # BACKTRACK
                print('BACKTRACKING....')
                self.chess_table[row_index][col_index] = 0

        # we've considered all the rows in a column w/o finding a valid cell   
        return False
    
    def is_place_valid(self, row_index, col_index):

        # check rows -whether given queens can attack each other horizontally
        for i in range(self.n):
            # there's already a queen in that given row
            if self.chess_table[row_index][i] == 1:
                # Two queens can attack each other
                return False
        
        # we don't have to check the columns b/c we'll place one queen in each column
        # we do have to check the diagonals

        # from top-left to bottom-right
        j = col_index
        for i in range(row_index, -1, -1):

            if i < 0:
                break
            
            if self.chess_table[i][j] == 1:
                return False
            j -= 1
        
        # check diaganols from top-right to bottom-left
        j = col_index
        for i in range(row_index, self.n):

            if j < 0:
                break

            if self.chess_table[i][j] == 1:
                return False
            
            j -= 1
        
        return True


    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(' Q ', end='')
                else:
                    print(' - ', end='')
            print('\n')


if __name__ == '__main__':
    queens = QueensProblem(4)
    queens.solve_queens()



