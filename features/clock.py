from functools import cached_property

import chess

from features.abstract import Features


class Clock(Features):
    """Features relating to time control and game clock. """

    def __init__(self, time_control, clock):
        self.time_control = time_control
        self.clock = clock

    @classmethod
    def from_row(cls, row):
        return cls(row.time_control, row.clock)

    @cached_property
    def approximate_game_length(self):
        """Approximate game length in seconds (T = S + 40 * I) where S is the starting time and I is the increment"""
        # https://lichess.org/forum/general-chess-discussion/is-there-any-data-or-statistics-that-shows

        # TODO: why are some games missing time_controls?
        if self.time_control == '-':
            return None

        s, i = self.time_control.split('+')
        s = int(s)
        i = int(i)
        return s + i * 40

    @cached_property
    def relative_time_remaining(self):
        """Clock divided by approximate game length."""
        if self.time_control == '-':
            return None

        return self.clock / self.approximate_game_length

    # TODO: difference in our clock vs. their clock? Would need to add their clock to lichess csv.