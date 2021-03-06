from functools import cached_property

import chess

from features.abstract import Features


class Pawns(Features):

    def __init__(self, fen):
        self.board = chess.Board(fen)

    @cached_property
    def our_doubled(self):
        files = [chess.square_file(s) for s in self.board.pieces(self.board.turn, chess.PAWN)]
        return len(files) - len(set(files))

    @cached_property
    def their_doubled(self):
        files = [chess.square_file(s) for s in self.board.pieces(not self.board.turn, chess.PAWN)]
        return len(files) - len(set(files))

    @cached_property
    def our_opposed(self):
        their_pawn_files = set([chess.square_file(s) for s in self.board.pieces(not self.board.turn, chess.PAWN)])
        our_opposed_pawns = [s for s in self.board.pieces(self.board.turn, chess.PAWN) if chess.square_file(s) in their_pawn_files]
        return len(our_opposed_pawns)
    
    @cached_property
    def their_opposed(self):
        our_pawn_files = set([chess.square_file(s) for s in self.board.pieces(self.board.turn, chess.PAWN)])
        their_opposed_pawns = [s for s in self.board.pieces(not self.board.turn, chess.PAWN) if chess.square_file(s) in our_pawn_files]
        return len(their_opposed_pawns)
        

if __name__ == '__main__':
    Pawns(chess.Board().fen()).features()