from manim import *

# class Test(Scene):
#     def construct(self):

#         circ = Circle(radius=2.4, color=RED)
#         self.play(Create(circ))

# class Pith(Scene):
#     def construct(self):
#         sq = Square(side_length=5,stroke_color = GREEN, fill_color = BLUE, fill_opacity = 0.75
#         )
#         self.play(Create(sq), run_time = 3)
#         self.wait()

# class Testing(Scene):
#     def construct(self):

#         name = Tex("Somdeb").to_edge(UL,buff=0.5)
#         sq = Square(side_length=0.5,fill_color = GREEN,fill_opacity = 0.75).shift(LEFT*3)
#         tri = Triangle().scale(0.6).to_edge(DR)

#         self.play(Write(name))
#         self.play(DrawBorderThenFill(sq),run_time=2)
#         self.play(Create(tri))
#         self.wait()

#         self.play(name.animate.to_edge(UR),run_time = 2)
#         self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time = 3)
#         self.wait()

class Errors(Scene):
    def construct(self):

        c = Circle(radius=2,fill_color = GREY_BROWN,fill_opacity=1)
        rect  = Rectangle(color=WHITE,height=3,width=2.5).to_edge(UL)
        arrow = always_redraw(lambda:Line(start=rect.get_center(), end=c.get_top(), buff=0.2).add_tip())
        self.play(Write(c))
        self.play(Create(c))
        self.play(Uncreate(c))
        self.play(Create(VGroup(rect,c,arrow)))
        self.wait()
        self.play(Write(rect))
        self.play(rect.animate.to_edge(UR))
        ax = Axes()
        self.play(Create(ax))
        self.wait()
        self.play(rect.animate.to_edge(UR),c.animate.scale(0.5),run_time= 4)

class Updaters(Scene):
    def construct(self):

        num= MathTex("ln(2)")
        box = SurroundingRectangle(num,color=BLUE,fill_opacity=0.4,fill_color=RED, buff=2)