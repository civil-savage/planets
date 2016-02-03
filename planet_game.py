#!/usr/bin/python


class Universe_Builder(object):

    location = 2
    locations = ['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto','Oort Cloud','Kupier Belt']
    planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
    moons = ['Luna', 'Pheobe', 'Io', 'Titan', 'Puck', 'Triton']

    def __init__(self):
        self.set_name()

    def set_name(self):
        self.name = self.locations[self.location]
        self.description ="This is place is called {}".format(self.name)

    def build_planet(self):
        return  type(str(self.planets[self.location]),(Planet,),dict(desc = "Test"))

    def build_moon(self):
        return  type(str(self.moon[self.location]),(Moon,),dict(desc = "Test"))

    def look(self):
        print self.desc

    def move(self,num):
        self.location += num
        self.set_name()
        self.build_planet()


class Planet(Universe_Builder):

    def set_name(self):
        self.name = self.planets[self.location]
    
    def land(self):
        if self.name = "Earth":
            

class Moon(Universe_Builder):

    def set_name(self):
        self.name = self.moon[self.location]


i = Universe_Builder()
bp = i.build_planet()
p = bp()

p.look()
print p.name
p.move(-1)
p.look()
print p.name
# class Mercury(Planet):
#     desc = "The smallest planet"

# class Venus(Planet):
#     pass

# class Earth(Planet):
#     desc = "This planet is Mostly Harmless"
#     pass

# class Mars(Planet):
#     pass

# class Jupiter(Planet):
#     desc = "The largest of the planets"

# class Saturn(Planet):
#     pass

# class Uranus(Planet):
#     pass

# class Neptune(Planet):
#     pass



### WHEN MOVE IS CALLED WE WANT TO ALSO SET THE APPROPRIATE PLANET CLASS TO THE CURRENT INSTANCE.

# p1 = Location()

# print p1.description

# p1.move(2)

# print p1.description

# x = Earth()

# print x.description

# x.look()

# x.move(-2)

# x.look()

# print x.planets[x.location]
