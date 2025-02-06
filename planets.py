#store data types as a list
class Planet:
    def __init__(self, position, mass, velocity, acc):
        self.position = [1,1]
        self.mass = 1
        self.velocity = [1,1]
        self.acc = acc

    def get_position(self):
        return self.position
    def set_position(self,position):
        self.position = position
    
    def get_acc(self):
        return self.acc
    def set_acc(self,acceleration):
        self.acc = acceleration

    def get_velocity(self):
        return self.velocity
    def set_velocity(self, velocity):
        self.velocity = velocity

    def get_mass(self):
        return self.mass
    def set_mass(self, mass):
        self.mass = mass


    

        
        