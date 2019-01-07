#NOT MY SOLUTION
class Game():
    AROUND = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    def __init__(self, board):
        self.toCheck = {(x, y) for x in range(len(board)) for y in range(len(board)) if board[x][y] == 1}
        self.boardD = {x + y * 1j for x, l in enumerate(board) for y, c in enumerate(l) if c}
    def play(self):
        c = 0
        while self.toCheck:
            newInLeap = {self.toCheck.pop()}
            while newInLeap:
                newInLeap = {(x + dx, y + dy) for x, y in newInLeap for dx, dy in self.AROUND if
                             (x + dx, y + dy) in self.toCheck}
                self.toCheck -= newInLeap
            c += 1
        return c



board = [[1,0,1,0,1],
         [1,0,1,0,1],
         [1,1,1,0,0],
         [0,0,0,1,1],
         [0,0,0,1,1]]

game = Game(board)
print(game.play())
