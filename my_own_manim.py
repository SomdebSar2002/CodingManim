from manim import *

# config.background_color = BLACK
# config.frame_width = 16
# config.frame_height = 9

class FirstExample(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        green_square = Square(color=GREEN, fill_opacity=0.8)
        green_square.next_to(blue_circle,RIGHT)
        self.add(blue_circle,green_square)

class SecondExample(Scene):
    def construct(self):
        ax = Axes(x_range=(-3,3),y_range=(-3,3))
        curve = ax.plot(lambda x:(x+2)*x*(x-2)/2, color= RED)
        area = ax.get_area(curve,x_range=(-2,0))
        # self.add(ax,curve,area)
        self.play(Create(ax))
        self.wait(2)
        self.play(Create(curve))
        self.wait(1)
        self.play(Create(area), run_time=2)
        #also multiple args can be passed to self.play

class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        green_circle = Circle(color=GREEN,fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))
        self.play(ReplacementTransform(green_square,green_circle))
        self.play(Indicate(green_circle))
        self.play(FadeOut(green_circle))

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot,RIGHT+UP)
        self.add(red_dot,green_dot)

        #shift
        s = Square(color=ORANGE)
        s.shift(2*UP+4*RIGHT)
        self.add(s)

        #move_to
        c = Circle(color=PURPLE)
        c.move_to([-3,-2,0])
        self.add(c)

        #align_to
        c2 = Circle(radius=0.5,color=RED,fill_opacity=0.5)
        c3=c2.copy().set_color(YELLOW)
        c4 = c2.copy().set_color(ORANGE)
        c2.align_to(s,UP)
        c3.align_to(s,RIGHT)
        c4.align_to(s,UP+RIGHT)
        self.add(c2,c3,c4)


class CriticalPoints(Scene):
    def construct(self):
        c=Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)

        for d in[(0,0,0),UP,UR,RIGHT,DR,DOWN,DL,LEFT,UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))

        s =Square(color=RED,fill_opacity=0.2)
        s.move_to([1,0,0],aligned_edge=UL)
        self.add(s)

from manim.utils.unit import Percent,Pixels

class UsefulUnits(Scene):
    def construct(self):
        for perc in range(5,51,5):
            self.add(Circle(radius=perc*Percent(X_AXIS)))
            self.add(Square(side_length=perc*Percent(Y_AXIS),color=YELLOW))

            d = Dot()
            d.shift(100*Pixels*RIGHT)
            self.add(d)


class Grouping(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        green_dot=Dot(color=GREEN).next_to(red_dot,RIGHT)
        blue_dot = Dot(color=BLUE).next_to(red_dot,UP)
        dot_group = VGroup(red_dot,green_dot,blue_dot)
        self.add(red_dot)
        dot_group.to_edge(RIGHT)
        self.add(dot_group)

        circles =VGroup(*[Circle(radius=0.2) for _ in range(10)])

        circles.arrange(UP,buff=0.5)
        self.add(circles)

        stars = VGroup(*[Star(color=YELLOW,fill_opacity=1).scale(0.5) for _ in range(20)])
        stars.arrange_in_grid(4,5,buff=0.2)
        self.add(stars)
        t = Text("Hello World!",color= WHITE)
        self.add(t)
        # self.play(Create(circles))

