from itertools import cycle
from random import random


class Sequence:
    def next(self):
        raise NotImplementedError('subclass must override next')


class DeterministicSequence(Sequence):
    def __init__(self, values):
        self.it = cycle(values)

    def next(self):
        return next(self.it)


class RandomSequence(Sequence):
    def next(self):
        return random()
