import math
from planets import Planets

#set a body's acc
def eulerA(body1, lisBodies, g_constant):
    #update acceleration
    acc = [0,0]
    for body2 in lisBodies:
        if body2 != body1:
            accAdd = getAcceleration(body1, body2, g_constant)
            acc[0] += accAdd[0]
            acc[1] += accAdd[1]
    body1.set_acc(acc)

#set a bodies velocity
def eulerV(body1):
    vel = [body1.get_velocity()[0] + body1.get_acc()[0], body1.get_velocity()[1] + body1.get_acc()[1]]
    body1.set_velocity(vel)

#set a bodies position
def eulerP(body1):
    #update position
    pos  = body1.get_position()
    pos[0] += body1.get_velocity()[0]
    pos[1] += body1.get_velocity()[1]
    body1.set_position(pos)


#used with eulerA
def getAcceleration(body1, body2, g_constant):
        # this is where we set units
    if body1 != body2:
        d_list = getDistance(body1, body2)

        #total acceleration
        acceleration_total = body2.get_mass() * g_constant / (d_list[2] ** 2)

        acceleration = []
        #acc x component
        acceleration.append(d_list[0] * acceleration_total)
        #acc y component
        acceleration.append(d_list[1] * acceleration_total)
        return acceleration
    return [0,0]

#used with eulerA, getForce
def getDistance (body1, body2):
    d_list = [] #x, y, total distance
    dx = body2.get_position()[0] - body1.get_position()[0]
    dy = body2.get_position()[1] - body1.get_position()[1]
    #get the total distance
    d_list.append(math.sqrt(dx ** 2 + dy ** 2))
    #get ratios for x and y
    d_list.insert(0, dx / d_list[0])
    d_list.insert(1, dy/d_list[1])
    return d_list


class Simulate:
    def __init__(self, g_constant = 100):
        self.lisBodies = []
        #gives the center of mass of the system
        self. CMsys = []
        self.g_constant = g_constant

    #run simulation, enter the amount of time between calculations
    def run(self, timeStep):
        #update each body
        for body in self.lisBodies:
            eulerA(body, self.lisBodies, self.g_constant)

        for body in self.lisBodies:
            eulerV(body)
            eulerP(body)

    def addBodies(self, body):
        self.lisBodies.append(body)

    def getBodies(self):
        return self.lisBodies

    #return the location of the center of mass for the system
    def getCOM(self):
        xloc = 0
        yloc = 0
        mtotal = 0

        for body in self.lisBodies:
            mtotal += body.get_mass()
            xloc += body.get_location()[0] * body.get_mass()
            yloc += body.get_location()[1] * body.get_mass()
        xloc = xloc / mtotal
        yloc = yloc / mtotal

        return [xloc, yloc]

    def get_g_constant(self):
        return self.g_constant

    def set_g_constant(self, g_constant):
        self.g_constant = g_constant

    def deleteBodies(self):
        self.lisBodies = []

        #check if bodies collide
    def check_collide(self, body1, body2):
        if body1 is not body2:
            if getDistance(body1, body2)[2] < 10:
                return True
        return False

    #use if the bodies did collide
    def collide(self, body1, body2):
        pos3 = [body1.get_position()[0] + body2.get_position()[0] / 2, body1.get_position()[1] + body2.get_position()[1] / 2]
        mass3 = body1.get_mass() + body2.get_mass()
        vel3 = [(body1.get_velocity()[0] * body1.get_mass() + body2.get_velocity()[0] * body2.get_mass()) / mass3 , (body1.get_velocity()[1] * body1.get_mass() + body2.get_velocity()[1] * body2.get_mass()) / mass3 ]
        body3 = Planets(pos3, mass3, vel3)
        self.lisBodies.remove(body1)
        self.lisBodies.remove(body2)
        self.lisBodies.append(body3)


# system = Simulate()
# system.addBodies(Planet())
# system.addBodies(Planet(position=[5,5]))
# system.addBodies(Planet(position=[-5,5]))
# system.addBodies(Planet(position=[-5,-5]))
# system.addBodies(Planet(position=[5,-5]))
#
# for i in range (4):
#     system.run(1)
#     for body in system.getBodies():
#         print(body.get_position())
#         print(system.get)


