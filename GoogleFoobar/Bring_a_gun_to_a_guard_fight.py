import math

def hypotenuse(a,b):
    return math.sqrt(float(a)**2 + float(b)**2)

def Eucl_dist(posA, posB):
    return hypotenuse(posA[0]-posB[0], posA[1]-posB[1])

class guard_fight:
    def __init__(self, _x_dim, _y_dim, _distance):
        self.x_dim = float(_x_dim)
        self.y_dim = float(_y_dim)
        self.distance = float(_distance)

    def guard_positions(self, badguy_position):
        badguy_position = map(float, badguy_position)
        self.x_mirrored, self.y_mirrored = int(math.ceil(self.distance/self.x_dim)), int(math.ceil(self.distance/self.y_dim))
        guard_mirror_positions = {}
        guard_mirror_positions[(0,0)] = badguy_position
        for i in xrange(-self.x_mirrored, self.x_mirrored+1):
            for j in xrange(-self.y_mirrored, self.y_mirrored+1):
                self.mirroring(i, j, guard_mirror_positions)
        return guard_mirror_positions
    def mirroring(self, i, j, mirror_positions):
        if (i,j) not in mirror_positions:
            if j > 0: 
                self.mirroring(i, j-1, mirror_positions)
                mirror_positions[(i,j)] = [mirror_positions[(i,j-1)][0],  2*self.y_dim*j-mirror_positions[(i,j-1)][1]]
            elif j < 0:
                self.mirroring(i, j+1, mirror_positions)
                mirror_positions[(i,j)] = [mirror_positions[(i,j+1)][0],  2*self.y_dim*(j+1)-mirror_positions[(i,j+1)][1]]
            elif i > 0:
                self.mirroring(i-1, j, mirror_positions)
                mirror_positions[(i,j)] = [2*self.x_dim*i- mirror_positions[(i-1,j)][0],  mirror_positions[(i-1,j)][1]]
            elif i < 0:
                self.mirroring(i+1, j, mirror_positions)
                mirror_positions[(i,j)] = [2*self.x_dim*(i+1)- mirror_positions[(i+1,j)][0],  mirror_positions[(i+1,j)][1]]
    def shooting_directions(self, captain_mirror_positions, badguy_mirror_positions):
        angle_captain = {}
        angle_badguy = {}
        ct = 0
        for i in xrange(-self.x_mirrored, self.x_mirrored+1):
            for j in xrange(-self.y_mirrored, self.y_mirrored+1):
                
                shooting_angle = math.atan2(captain_mirror_positions[(i,j)][1]-captain_mirror_positions[(0,0)][1],
                     captain_mirror_positions[(i,j)][0]-captain_mirror_positions[(0,0)][0])
                if (i!=0 or j!=0) and shooting_angle not in angle_captain:
                    angle_captain[shooting_angle] = captain_mirror_positions[(i,j)]
                elif (i!=0 or j!=0) and shooting_angle in angle_captain:
                    if Eucl_dist(captain_mirror_positions[(i,j)],captain_mirror_positions[(0,0)]) < Eucl_dist(angle_captain[shooting_angle],captain_mirror_positions[(0,0)]):
                        angle_captain[shooting_angle] = captain_mirror_positions[(i,j)]

        for i in xrange(-self.x_mirrored, self.x_mirrored+1):
            for j in xrange(-self.y_mirrored, self.y_mirrored+1):
                shooting_angle = math.atan2(badguy_mirror_positions[(i,j)][1]-captain_mirror_positions[(0,0)][1],
                     badguy_mirror_positions[(i,j)][0]-captain_mirror_positions[(0,0)][0] )
                # already shot that direction before
                if shooting_angle in angle_badguy: 
                    continue
                # not in range
                if Eucl_dist(captain_mirror_positions[(0,0)],badguy_mirror_positions[(i,j)]) > self.distance:
                    continue 
                # would shoot myself
                if shooting_angle in angle_captain and Eucl_dist(captain_mirror_positions[(0,0)],badguy_mirror_positions[(i,j)]) > Eucl_dist(captain_mirror_positions[(0,0)],angle_captain[shooting_angle]):
                    continue
                ct += 1
                angle_badguy[shooting_angle] = 1
        return ct







        
def answer(dimensions, captain_position, badguy_position, distance):
    # your code here
    x_dim, y_dim = tuple(dimensions)
    myfight = guard_fight(x_dim, y_dim, distance)
    ct = 0
    badguy_mirror_positions = myfight.guard_positions(badguy_position)
    captain_mirror_positions = myfight.guard_positions(captain_position)
    
    return myfight.shooting_directions(captain_mirror_positions,badguy_mirror_positions)






# dimensions =[3,2]
# captain_position = [1,1]
# guard = [2,1]
# distance = 4
## test 
# dimensions =[300,275]
# captain_position = [150,150]
# guard = [185,100]
# distance = 500
## test 
dimensions =[2,5]
captain_position = [1,2]
guard = [1,4]
distance = 11
print answer(dimensions, captain_position, guard, distance)






