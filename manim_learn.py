from manim import *

class BraceAnnotation(Scene):
    def construct(self):
        a1  = Dot(color=WHITE)
        l2 = Line(ORIGIN,[2,0,0])
        a2 =  Dot(color=WHITE).move_to([2,2,0])
        l1 = Line(color=ORANGE,start=a1,end=a2)
        t2 = MathTex(" x - x_{1}").next_to(l1,UP)
        a = Angle(l2,l1)
        t2.rotate(angle=a.get_value())
        t = Text("Horizontal Distance").move_to([0,-2,0])
        b1 = Brace(l1,direction=l1.copy().rotate(PI/2).get_unit_vector())
        self.add(b1)
        self.add(a1)
        self.add(a2)
        self.add(l1)
        self.add(t2)
        self.add(t)

class VectorArrow(Scene):
    def construct(self):
        ax = Axes(x_range=(-10,10),y_range=(-10,10))
        a = Arrow(ORIGIN,[2,2,0])
        t1 = MathTex((0,0))
        t2 = MathTex((2,2)).move_to([2,2,0])
        self.add(a)
        self.add(ax)
        self.add(t1)
        self.add(t2)
        self.add(NumberPlane())

class BooleanOperation(Scene):
    def construct(self):
        a = Ellipse(width=2,height=4,fill_opacity=0.2,color=BLUE)
        b = Ellipse(width=2,height=4,fill_opacity=0.2,color=ORANGE)
        c = VGroup(a,b).arrange(RIGHT,buff=-0.6)
        u = Union(a,b).move_to(-4*LEFT+UP).scale(0.5).set_color(RED).set_opacity(0.5)
        
        e = Exclusion(a,b)
        d = Difference(a,b)
        self.add(u,e,d)
        self.add(c)

class Rolling(Scene):
    def construct(self):
        r1 = Circle(radius=1,color=RED,fill_opacity=0.4)
        r2 = Circle(radius=1,color=RED,fill_opacity=0.4).shift(3*DOWN)
        p1 = VGroup(*[Dot(radius=0.08).move_to(r1.point_from_proportion(p)*(0.75)) for p in np.linspace(0,1,20)])
        p2 = VGroup(*[Dot(radius=0.08).move_to(r2.point_from_proportion(p)*(0.75)) for p in np.linspace(0,1,20)])
        c = ArcBetweenPoints([0,-1,0],[0,-2,0],radius=1e8,stroke_width=0,color=YELLOW)
        d = ArcBetweenPoints([1,0,0],[1,-3,0],radius=-1e8,stroke_width=0,color=YELLOW)
        a = ArcBetweenPoints([0,-1,0],[1,0,0],radius=1,stroke_width=0,color=YELLOW)
        b = ArcBetweenPoints([0,-2,0],[1,-3,0],radius=-1,stroke_width=0,color=YELLOW)
        area = ArcPolygonFromArcs(a,b,c,d,color=YELLOW,fill_opacity=0.3,stroke_width=0)
        rec1 = Polygon([1,0,0],[3,0,0],[3,-3,0],[1,-3,0],color=YELLOW,fill_opacity=0.3,stroke_width=0)
        rec2 = Polygon([0,-2,0],[-3,-2,0],[-3,-1,0],[0,-1,0],color=YELLOW,fill_opacity=0.3,stroke_width=0)
        p1.move_to(r1.get_center())
        p2.move_to(r2.get_center())
        
        self.add(p1,p2)
        self.add(r1,r2)
        
        def rshifter(mob,dt):
            c = mob.get_width()
            mob.set_width(c-0.5*dt*+RIGHT).shift(0.25*dt*-RIGHT)
        
        def lshifter(mob,dt):
            c = mob.get_width()
            mob.set_width(c+dt*RIGHT).shift(0.5*dt*LEFT)
        def urotater(mob,dt):
            mob.rotate(angle=-2*PI*dt)
        def drotater(mob,dt):
            mob.rotate(angle=2*PI*dt)
        
        rec1.add_updater(rshifter)
        rec2.add_updater(lshifter)
        p1.add_updater(urotater)
        p2.add_updater(drotater)
        self.add(rec1)
        self.add(rec2,area)
        self.wait(2)
        

class RollingGeneric(MovingCameraScene):
    def construct(self):
        spacing = 2
        rad = 1
        ll = 1
        theta = np.deg2rad(70)
        rl = 5
        r1 = Circle(radius=rad,color=RED,fill_opacity=0.4).move_to(ORIGIN)
        r2 = Circle(radius=rad,color=RED,fill_opacity=0.4).move_to([0,-2*rad-spacing,0])
        p1 = VGroup(*[Dot(radius=0.08).move_to(r1.point_from_proportion(p)*(0.75)) for p in np.linspace(0,1,20)])
        p2 = VGroup(*[Dot(radius=0.08).move_to(r2.point_from_proportion(p)*(0.75)) for p in np.linspace(0,1,20)])
        tex = MathTex(r" \alpha =",round(theta,2))
        
        rr1  = [rad*np.sin(theta),-rad*np.cos(theta),0]
        rr2 =  [rad*np.sin(theta)+rl,-rad*np.cos(theta),0]
        rr3 = [rad*np.sin(theta)+rl,-2*rad+rad*np.cos(theta)-spacing,0]
        rr4 = [rad*np.sin(theta),-2*rad+rad*np.cos(theta)-spacing,0]


        ll1 = [0,-rad,0]
        ll2 = [0,-rad-spacing,0]
        ll3 = [-ll,-rad-spacing,0]
        ll4 = [-ll,-rad,0]
        uc = [0,0,0]
        ud = [0,-2*rad-spacing,0]
        u1 = Line(uc,ll1,color=WHITE)
        u2 = Line(uc,rr1,color=WHITE)
        self.add(u1,u2)
        au = Angle(u1,u2,color=WHITE)
        d1 = Line(ud,ll2,color=WHITE)
        d2 = Line(ud,rr4,color=WHITE)
        ad = Angle(d2,d1,color=WHITE)
        self.add(d1,d2,ad,au)
        self.add(tex.next_to(ad),tex.copy().next_to(au))
        c = ArcBetweenPoints(rr1,rr4,radius=-1e8,stroke_width=10,color=YELLOW)
        d = ArcBetweenPoints(ll1,ll2,radius=1e8,stroke_width=10,color=YELLOW)
        a = ArcBetweenPoints(ll1,rr1,radius=rad,stroke_width=10,color=YELLOW)
        b = ArcBetweenPoints(ll2,rr4,radius=-rad,stroke_width=10,color=YELLOW)
        area = ArcPolygonFromArcs(d,b,a,c,color=YELLOW,fill_opacity=0.3,stroke_width=0)
        rec1 = Polygon(rr1,rr2,rr3,rr4,color=YELLOW,fill_opacity=0.3,stroke_width=0)
        rec2 = Polygon(ll1,ll2,ll3,ll4,color=YELLOW,fill_opacity=0.3,stroke_width=0)
        p1.move_to(r1.get_center())
        p2.move_to(r2.get_center())
        # self.add(rec1)
        def rshifter(mob,dt):
            c = mob.get_width()
            mob.set_width(c-0.5*dt*+RIGHT).shift(0.25*dt*-RIGHT)
        
        def lshifter(mob,dt):
            c = mob.get_width()
            mob.set_width(c+dt*RIGHT).shift(0.5*dt*LEFT)
        def urotater(mob,dt):
            mob.rotate(angle=-2*PI*dt)
        def drotater(mob,dt):
            mob.rotate(angle=2*PI*dt)
        self.camera.frame.move_to([0,-1.5*rad-0.5*spacing,0])
        self.add(p1,p2)
        self.add(r1,r2)
        self.add(a,b,c,d)
        rec1.add_updater(rshifter)
        rec2.add_updater(lshifter)
        p1.add_updater(urotater)
        p2.add_updater(drotater)
        self.add(rec1)
        self.add(rec2,area)
        self.wait(5)

        # D1 = DashedLine(ll2,rad)
        # D2 = DashedLine
# MoveAlongPath()
# MoveToTarget()
# GrowFromCenter()
# ValueTracker(110).get_value()*DEGREES
class CylinderAnimation(ThreeDScene):
    def construct(self):
        cylinder = Cylinder(radius=1, height=2)
        self.play(Create(cylinder))
        self.wait(1)

# class ProjectileAnimation(Scene):
#     def construct(self):
#         c1 = Circle(radius=1,fill_opacity=1,color=RED)
#         def lshifter(mob,dt):
            