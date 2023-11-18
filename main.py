# from chess_bot import ChessEngine
# import chess

# class Chess:
#     def __init__(self, stockfish):
#         self.stockfish = stockfish

#     def move_input(self):
#         input = audio_input()
#         return input

#     def update(self):
#         best_move = self.stockfish.get_best_move()

#         if best_move and self.stockfish.legal_move(best_move):
#             return self.stockfish.update_position([best_move])
#         else:
#             print("Invalid move or no legal moves.")
#             return False


# # Example usage:
# stockfish = ChessEngine()
# chess_game = Chess(stockfish)
# chess_game.update()


# from speech_recognition_utils import audio_input
# from chess_bot import ChessEngine

# class ChessGame():
#     def __int__(self):
#         self.stockfish = ChessEngine

#     def player_move(self):
#         print("player's Turn")
#         audio = audio_input()

#     def bot_move(self):
#         print("bot move")
#         return self.stockfish.get_best_move()

#     def play_game(self):
#         while True:
#             #players turn
#             player_move_str  = self.player_move()
#             if player_move_str:
#                 if self.stockfish.legal_move(player_move_str):
#                     self.stockfish.update_position(player_move_str)
#             else:
#                 print("No input recieved, try again")
#                 return self.play_game
            
#             #bot's turn
#             bot_move_str = self.bot_move
#             return self.stockfish.update_position(bot_move_str)

#             current_position = self.stockfish.get_current_position()
#             print("current_position: ", current_position)
# chess = ChessGame()
# chess.play_game()

from stockfish_engine import Stockfish, Board
# from stockfish_engine import Board
from speech_recognition_utils import SpeechRecognition
# from chess import Board

class Chess:
    def __init__(self, stockfish, speech_recognition, board):
        self.stockfish = stockfish
        self.speech_recognition = speech_recognition
        self.board = board
    
    def player_move(self):
        audio_input = self.speech_recognition.audio_input()
        if audio_input and self.stockfish.legal_move(audio_input):
            print(audio_input)
            self.stockfish.update_position([audio_input])
            print("Board after player's move")
            print(self.board.get_board())
        else:
            print("Invalid move or no input received. Try Again")

    def bot_move(self):
        bot_input = self.stockfish.get_best_move()
        self.stockfish.update_position([bot_input])
        print("Board after bot's move")
        print(self.board.get_board())    
    # def play_game(self):
    #     while not self.stockfish.game_over()


stockfish = Stockfish(path_to_stockfish)
speech_recognition = SpeechRecognition()
chess_game = Chess(stockfish, speech_recognition)
chess_game.player_move()
chess_game.bot_move()
