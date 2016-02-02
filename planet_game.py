#!/usr/bin/python

class Location(object):
    location = 2
    planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']

    def __init__(self):
        self.set_names()

    def set_names(self):
        self.name = self.planets[self.location]
        self.description ="This is place is called {}".format(self.name)

    def move(self,num):
        self.location += num
        self.set_names()


class Planet(Location):
    
    def look(self):
        print self.desc




class Mercury(Planet):
    desc = "The smallest planet"

class Venus(Planet):
    pass

class Earth(Planet):
    desc = "This planet is Mostly Harmless"
    pass

class Mars(Planet):
    pass

class Jupiter(Planet):
    desc = "The largest of the planets"

class Saturn(Planet):
    pass

class Uranus(Planet):
    pass

class Neptune(Planet):
    pass



### WHEN MOVE IS CALLED WE WANT TO ALSO SET THE APPROPRIATE PLANET CLASS TO THE CURRENT INSTANCE.

# p1 = Location()

# print p1.description

# p1.move(2)

# print p1.description

x = Earth()

print x.description

x.look()


