import inspect
import random
import time
from tkinter import *

import hudfunctions

Window_Width = 800

Window_Height = 800


callable_hud_functions = inspect.getmembers(hudfunctions, inspect.isfunction)


class Renderer:
    # window: tkinter.Tk
    # canvas: tkinter.Canvas
    # bodies: []

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):

        self.window: Tk = self.create_window()
        self.canvas = self.create_canvas()
        self.canvas.pack
        self.canvas.update()
        # self.polygons = Position[0]
        # self.bodies: Body

    def create_window(self):
        window = Tk()
        window.title("Python Guides")

        window.geometry(f'{Window_Width}x{Window_Height}')
        return window

    def create_canvas(self):
        self.window.title("sd")

        canvas = Canvas(self.window)
        canvas.configure(bg="yellow", bd="-1")
        canvas.pack(fill="both", expand=True)
        return canvas

    def loop(self):
        self.canvas.update()
        # polygons_to_render = self.polygons.copy
        begin_draw_time = 1
        td = 1
        canvas_object_ids = []

        while True:
            begin_draw_time = time.time()
            # for p in polygons_to_render:
            #    self.canvas.delete(p)
            # polygons_to_render = self.polygons.copy()
            # for p in polygons_to_render:
            #    pass
            v = 0
            for y in range(0, 4):
                sides = []
                for s in range(0, random.randint(3, 6)):
                    v += 1
                    sides.append(random.randint(0, 800))
                    sides.append(random.randint(0, 800))

                canvas_object_ids.append(
                    self.canvas.create_polygon(sides, fill="", width=0, outline=_from_rgb(
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))))
            canvas_object_ids.append(
                self.canvas.create_text(0, 12, text="{:.2f}".format(1 / td), anchor=NW, fill="black", font=12))
            canvas_object_ids.append(
                self.canvas.create_text(0, 24, text=len(canvas_object_ids) - 1, anchor=NW, fill="black", font=12))
            canvas_object_ids.append(
                self.canvas.create_text(0, 36, text="verts: {}".format(v), anchor=NW, fill="black", font=12))
            self.canvas.update()

            # Clear canvas objects
            while len(canvas_object_ids) > 0:
                self.canvas.delete(canvas_object_ids.pop(0))

            td = (time.time() - begin_draw_time)
            # self.canvas.update()
            time.sleep(0.01)


# animate_ball(Animation_Window, Animation_canvas, Ball_min_movement, Ball_min_movement)
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb
