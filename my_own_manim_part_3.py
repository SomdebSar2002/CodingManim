from manim import *
import os
os.environ["PATH"] = os.environ["PATH"] + r";C:\Users\SOMDEB\AppData\Local\Programs\MiKTeX\miktex\bin\x64\\"

class Updater(Scene):
    def construct(self):
        blue_dot = Dot(color=BLUE)
        dot_label = Text("Hello dot!").next_to(blue_dot,UP)
        dot_label.add_updater(
            lambda mobject: mobject.next_to(blue_dot,UP)
        )
        self.add(blue_dot,dot_label)
        self.play(blue_dot.animate.shift(RIGHT))
        self.play(blue_dot.animate.scale(3))
        self.play(blue_dot.animate.center())

class AllUpdaterTypes(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        pointer = Arrow(ORIGIN,RIGHT).next_to(red_dot,LEFT)
        pointer.add_updater(
           lambda mobject: mobject.next_to(red_dot,LEFT) 
        )

        def shifter(mob,dt):
            mob.shift(2*dt+RIGHT)
        red_dot.add_updater(shifter)

        def scene_scaler(dt):
            for mob in self.mobjects:
                mob.set(width=2/(1+np.linalg.norm(mob.get_center())))
        self.add_updater(scene_scaler)

        self.add(red_dot,pointer)
        self.update_self(0)
        self.wait(5)

class UpdaterAndAnimation(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        rotating_square = Square()
        rotating_square.add_updater(
            lambda mob,dt:mob.rotate(PI*dt)
        )
        def shifter(mob,dt):
            mob.shift(2*dt+RIGHT)
        red_dot.add_updater(shifter)

        self.add(red_dot,rotating_square)
        self.wait(1)
        red_dot.suspend_updating()
        self.wait()
        self.play(
            red_dot.animate.shift(UP),
            rotating_square.animate.move_to([-2,-2,0])
        )
class OtherClass(Scene):
    def construct(self):
        line = NumberLine(x_range=[-5,5])
        position = ValueTracker(0)
        pointer = Vector(UP)
        pointer.add_updater(
            lambda mob: mob.next_to(
                line.number_to_point(position.get_value()),DOWN
            )
        )
        pointer.update()
        self.add(line,pointer)
        self.wait()
        self.play(position.animate.set_value(4))
        self.play(position.animate.set_value(-2))
        self.wait(1)

class ValueTrackerPlot(Scene):
    def construct(self):
        a = ValueTracker(1)
        ax = Axes(x_range=[-2, 2, 1], y_range=[-8.5, 8.5, 1], x_length=4, y_length=6)
        parabola = ax.plot(lambda x: a.get_value() * x**2, color=RED)
        parabola.add_updater(
            lambda mob: mob.become(ax.plot(lambda x: a.get_value() * x**2, color=RED))
        )
        
        a_number = DecimalNumber(
            number=a.get_value(),  # Replace 0 with your desired numeric value
            num_decimal_places=2,
            color=RED,
            show_ellipsis=False,
        )
        a_number.add_updater(
            lambda mob: mob.set_value(a.get_value()).next_to(parabola, RIGHT)
        )
        self.add(ax, parabola,a_number)
        self.play(a.animate.set_value(2))
        self.play(a.animate.set_value(-2))
        self.play(a.animate.set_value(1))

    


