import inspect
import random
import threading
import time
from tkinter import *

import hudfunctions

Window_Width = 800

Window_Height = 800

callable_hud_functions = inspect.getmembers(hudfunctions, inspect.isfunction)


def create_window():
    window = Tk()
    window.title("Python Guides")

    window.geometry(f'{Window_Width}x{Window_Height}')
    return window


class Renderer:
    # window: tkinter.Tk
    # canvas: tkinter.Canvas
    # bodies: []

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):

        self.window: Tk = create_window()
        self.canvas = self.create_canvas()
        self.canvas.pack
        self.canvas.update()
        # self.polygons = Position[0]
        # self.bodies: Body

    def create_canvas(self):
        self.window.title("sd")

        canvas = Canvas(self.window)
        canvas.configure(bg="white", bd="-1")
        canvas.pack(fill="both", expand=True)
        return canvas

    def loop(self):
        self.update(True)

    def async_update(self):
        threading.Thread(target=self.update(), args=(1,))

    def update(self, loop):
        # polygons_to_render = self.polygons.copy
        begin_draw_time = 1
        canvas_object_ids = []

        frames = 0
        fps_sum = 0
        avg_fps = 1
        avg_fps_period = 50

        target_fps = 60

        def current_td():
            return time.time() - begin_draw_time

        while loop:
            td = current_td()
            left_over_frame_time = (1 / target_fps) - current_td()
            if (left_over_frame_time >= 0):
                time.sleep(left_over_frame_time)
                continue

            frames = frames + 1
            fps_sum = fps_sum + (1 / td)
            if frames % avg_fps_period == 0:
                avg_fps = fps_sum / frames + 1
                fps_sum = frames = 0

            begin_draw_time = time.time()
            # for p in polygons_to_render:
            #    self.canvas.delete(p)
            # polygons_to_render = self.polygons.copy()
            # for p in polygons_to_render:
            #    pass
            v = 0

            for y in range(0, 100):
                sides = []

                for s in range(0, random.randint(3, 4)):
                    v += 1
                    sides.append(random.randint(0, 800))
                    sides.append(random.randint(0, 800))

                canvas_object_ids.append(
                    self.canvas.create_polygon(sides, fill="", width=0, outline=_from_rgb(
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))))

            canvas_object_ids.append(
                self.canvas.create_text(0, 12, text="fps: {:.2f}".format(1 / td), anchor=NW, fill="red", font=12))
            canvas_object_ids.append(
                self.canvas.create_text(0, 24, text="avg fps(per {}frames): {:.2f}".format(avg_fps_period, avg_fps), anchor=NW, fill="red", font=12))
            canvas_object_ids.append(
                self.canvas.create_text(0, 36, text="canvas objects: {}".format(len(canvas_object_ids)), anchor=NW, fill="red", font=12))
            canvas_object_ids.append(
                self.canvas.create_text(0, 48, text="verts: {}".format(v), anchor=NW, fill="red", font=12))
            canvas_object_ids.append(
                self.canvas.create_text(0, 60, text="left over frame time: {}".format(left_over_frame_time), anchor=NW, fill="red", font=12))

            self.canvas.update()

            # Clear canvas objects
            while len(canvas_object_ids) > 0:
                self.canvas.delete(canvas_object_ids.pop(0))

            endtime = time.time()

            # self.canvas.update()


# animate_ball(Animation_Window, Animation_canvas, Ball_min_movement, Ball_min_movement)
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb
