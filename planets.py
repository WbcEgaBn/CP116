#store data types as a list
class Planets:
    def __init__(self, position=None, mass=1, velocity=None, acc=None, color = None):
        if velocity is None:
            velocity = [0, 0]
        if position is None:
            position = [0, 0]
        if acc is None:
            acc = [0,0]
        self.position = position[:]
        self.mass = mass
        self.velocity = velocity[:]
        self.acc = acc[:]
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_position(self):
        return self.position[:]
    def set_position(self,position):
        self.position = position[:]
    
    def get_acc(self):
        return self.acc[:]
    def set_acc(self,acceleration):
        self.acc = acceleration[:]

    def get_velocity(self):
        return self.velocity[:]

    def set_velocity(self, velocity):
        self.velocity = velocity[:]

    def get_mass(self):
        return self.mass
    def set_mass(self, mass):
        self.mass = mass


    

        
        