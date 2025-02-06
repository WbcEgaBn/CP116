


#set a body's pos, vel, and acc
def euler(body1, lisBodies):
    #update acceleration
    acc = []
    for body in lisBodies:
        if body != body1:
            accAdd = getForce(body1, body)
            acc[0] += accAdd[0]
            acc[1] += accAdd[1]

    #update velocity
    vel = [body1.get_Vel()[0] + body1.get_Acc()[0], body1.get_Vel()[1] + body1.get_Acc()[1]]
    body1.set_Vel(vel)

    #update position
    pos  = body1.get_Pos()
    pos[0] += body1.get_Vel()[0]
    pos[1] += body1.get_Vel()[1]
    body1.set_Pos(pos)


def getForce(body1, body2):
    # this is where we set units
    g_constant = 1

    return body2.get_mass() * g_constant / (getDistance(body1, body2) ** 2)

def getDistance (body1, body2):

    return 1


class Simulate:
    def __init__(self):
        self.lisBodies = []
        #gives the center of mass of the system
        self. CMsys = []

    #run simulation, enter the amount of time between calculations
    def run(self, timeStep):
        #update each body
        for body in self.lisBodies:
            body = euler(body, self.lisBodies)


