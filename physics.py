# This is a sample Python script.
import ast
import threading

import numpy

import gui

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


g = 9.8
dimensions = 1


def vec_build() -> numpy.ndarray:
    return numpy.empty(dimensions, dtype=object)


class Vector:
    components: numpy.ndarray

    def __new__(cls, *args, **kwargs):
        cls.components = vec_build()
        return cls


class Position(Vector):
    pass


class Body:
    def __new__(cls, *args, **kwargs):
        pass


universes_bodies = []
universes_bodies.append(Body())
a = Vector()
b = Position()
print(a.components.size)
print(b.components.size)
universes_bodies.append(a)
ren = gui.Renderer()
ren.loop()
