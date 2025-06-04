# class TictactoeException(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)


# class Board():
#     valid_moves=["upper left", "upper center", "upper right", 
#                  "middle left", "center", "middle right", 
#                  "lower left", "lower center", "lower right"]
#     def __init__(self):
#         self.board_array = [[" " for _ in range(3)] for _ in range(3)]
#         self.turn = "X"