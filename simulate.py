import planets
import math

from planets import Planet


#set a body's acc
def eulerA(body1, lisBodies):
    #update acceleration
    acc = [0,0]
    for body2 in lisBodies:
        if body2 != body1:
            accAdd = getAcceleration(body1, body2)
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
def getAcceleration(body1, body2):
        # this is where we set units
    g_constant = 1
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
    def __init__(self):
        self.lisBodies = []
        #gives the center of mass of the system
        self. CMsys = []

    #run simulation, enter the amount of time between calculations
    def run(self, timeStep):
        #update each body
        for body in self.lisBodies:
            eulerA(body, self.lisBodies)

        for body in self.lisBodies:
            eulerV(body)
            eulerP(body)

    def addBodies(self, body):
        self.lisBodies.append(body)

    def getBodies(self):
        return self.lisBodies

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


