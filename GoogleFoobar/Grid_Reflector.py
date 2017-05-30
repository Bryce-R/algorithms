import math
import matplotlib.pyplot as plt

def hypotenuse(a,b):
    return math.sqrt(float(a)**2 + float(b)**2)

def intersection(a_start, a_end, b_start, b_end):
    s1_x,s1_y = float(a_end[0]-a_start[0]), float(a_end[1]-a_start[1])
    s2_x,s2_y = float(b_end[0]-b_start[0]), float(b_end[1]-b_start[1])
    if -s2_x*s1_y + s1_x*s2_y == 0: return None
    s =  ( -s1_y*(a_start[0] - b_start[0]) + s1_x*(a_start[1] - b_start[1]) )/( -s2_x*s1_y + s1_x*s2_y )
    t = ( s2_x*(a_start[1] - b_start[1]) - s2_y*(a_start[0] - b_start[0]) )/(-s2_x*s1_y + s1_x*s2_y )
    if (s>0 and s <1 and t>0 and t<= 1 ):
        return [a_start[0] + t*s1_x, a_start[1] + t*s1_y]
    else:
        return None

class grid:
    def __init__(self, _n, _m):
        self.n = _n
        self.m = _m
        plt.xlim(0,self.n)
        plt.ylim(0,self.m)

    def draw_grid(self):
        for i in xrange(self.m+1):
            plt.plot(xrange(0,self.n+1),[i for j in xrange(0,self.n+1)],'r:')
        for j in xrange(self.n+1):
            plt.plot([j for i in xrange(0,self.m+1)],xrange(0,self.m+1),'r:')
    def draw_line(self, position, velocicty, length):
        end_position = [position[0]+velocicty[0]*length, position[1]+velocicty[1]*length]
        intersect_data = self.wall_intersect(position, end_position, velocicty, length)
        if intersect_data:
            print "Relected off of wall."
            reflect_pt,length_travelled,velocicty_new = intersect_data
            print reflect_pt,  length_travelled, velocicty_new
            plt.plot([ position[0], reflect_pt[0] ],[ position[1],reflect_pt[1] ],'b-')
            self.draw_line( reflect_pt, velocicty_new, math.fabs(length -length_travelled) )
        else:
            print "No reflection. end position: ",
            print end_position
            plt.plot([ position[0], end_position[0] ],[ position[1],end_position[1] ],'b-+',markersize=20,linewidth=2)


    def wall_intersect(self, position, end_position, velocicty, length):
        edges = [ [(0.0,0.0), (self.n, 0.0)], [(self.n, 0.0), (self.n, self.m)], [(self.n, self.m), (0.0, self.m)], [(0.0, self.m), (0.0,0.0)] ]
        for i in xrange(len(edges)):
            edge_seg = edges[i]
            if intersection(position, end_position, edge_seg[0], edge_seg[1]):
                reflect_pt = intersection(position, end_position, edge_seg[0], edge_seg[1])
                distance = hypotenuse(reflect_pt[0]-position[0],reflect_pt[1]-position[1])
                velocicty_new = velocicty
                if i == 0 or i == 2: 
                    velocicty_new[1] *= -1
                else: velocicty_new[0] *= -1
                if i == 0: 
                    reflect_pt[1] = 0
                elif i == 1:
                    reflect_pt[0] = self.n
                elif i == 2:
                    reflect_pt[1] = self.m
                elif i == 3:
                    reflect_pt[0] = 0
                return reflect_pt, distance, velocicty_new
        return None
                


            






class line:
    def __init__(self, me, guard):
        self.k = (float(guard[1])-me[1])/(float(guard[0])-me[0])
        self.b = guard[1] - self.k*(float(guard[0]))

    def draw_line(self,n):
        for i in xrange(n):
            plt.plot(xrange(0,n+1), [self.k*i+self.b for i in xrange(0,n+1)])

# mygrid = grid(300,275)

# plt.plot([150],[150],'b+',markersize=20,linewidth=2)
# plt.plot([185],[100],'bx',markersize=20,linewidth=2)
# # myline = line([150,150],[185,100])
# # myline.draw_line(300)
# mygrid.draw_grid()
# plt.xlim(0,300)
# plt.ylim(0,275)
# plt.show()

# mygrid = grid(10,9)
# mygrid.draw_grid()
# # velocicty = [1,-200]
# velocicty = [4,-5]
# velocicty = [i/hypotenuse(velocicty[0],velocicty[1]) for i in velocicty]
# mygrid.draw_line([5,5],velocicty,120)
# plt.plot([5],[5],'b*',markersize=20,linewidth=2)
# plt.plot([5],[6],'bx',markersize=20,linewidth=2)
# plt.show()

mygrid = grid(3,2)
mygrid.draw_grid()
# velocicty = [1,-200]
velocicty = [1.9,-1]
velocicty = [i/hypotenuse(velocicty[0],velocicty[1]) for i in velocicty]
mygrid.draw_line([1,1],velocicty,200)
plt.plot([1],[1],'b*',markersize=15,linewidth=2)
plt.plot([2],[1],'b*',markersize=15,linewidth=2)
plt.show()

# mygrid = grid(300,275)
# mygrid.draw_grid()
# # velocicty = [1,-200]
# velocicty = [1.9,-1]
# velocicty = [i/hypotenuse(velocicty[0],velocicty[1]) for i in velocicty]
# mygrid.draw_line([150,150],velocicty,50000)
# plt.plot([150],[150],'b*',markersize=15,linewidth=2)
# plt.plot([185],[100],'b*',markersize=15,linewidth=2)
# plt.show()