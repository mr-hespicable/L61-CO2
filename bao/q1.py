import math

ANGLE_INTERVAL = 2.8125

class Pos:
    def __init__(self, cam: str, pos: str):
        self.cam: int = int(cam)
        self.pos: int = int(ord(pos) - 64)

    def angle(self):
        return (4 * (self.cam-1) + self.pos) * ANGLE_INTERVAL

    def line_length(self, pos):
        g = abs(self.angle() - pos.angle())
        return 90 * math.sin(math.radians(g/2))

    def distance_from_center(self, t1, t2, pos):
        g = abs(self.angle() - pos.angle())
        biggest_d = max(t1, t2) * 3.0 * 10
        
        l1 = biggest_d - 45 * math.sin(math.radians(g/2))
        h1 = 45 * math.cos(math.radians(g/2))

        e = math.sqrt((h1**2) + (l1**2))
        return e

    def t_angle(self, t1, t2, pos):
        e = self.distance_from_center(t1, t2, pos)
        
        d2 = min(t1, t2) * 3.0 * 10

        top = d2**2 - 45**2 - e**2

        bottom = -2 * 45 * e
        print(self.angle())
        print(pos.angle())

        return math.degrees(math.acos(top/bottom)) + max(self.angle(), pos.angle())
        

time_a, time_b = map(float, input().split())
cam_a, pos_a, cam_b, pos_b = input().split()
 
pos_a = Pos(cam_a, pos_a)
pos_b = Pos(cam_b, pos_b)

distance = pos_a.distance_from_center(time_a, time_b, pos_b)
angle = pos_a.t_angle(time_a, time_b, pos_b) 

print(f"{angle:.2f} {distance:.2f}")

