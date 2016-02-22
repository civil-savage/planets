#!/usr/bin/python


## This might be better off setting up a bunch of abstract clasess for
## planets, Planets, Moons and moons, and then calling them.  Also the
## interface needs more thought, Planet would be the _metaclass_ and
## perhaps use the super(method to call into Universe_Builder?


### Overall perhaps redesign this entire project.  The idea of
### metaclassess is ok and perhaps also consider making it more
### modular and try and decouple some of the clasess? Also the game
### interface perhaps could be class instatiaed?

class Universe_Builder(object):

    location = 2
    locations = ['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto','Oort Cloud','Kupier Belt']

    planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto','Oort Cloud','Kupier Belt']
    moons = ['Luna', 'Pheobe', 'Io', 'Titan', 'Puck', 'Triton']

    def __init__(self):
        self.set_name()

    def set_name(self):
        self.name = self.locations[self.location]
        self.description ="This location is called {}.".format(self.name)

    def build_planets(self):
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
        if self.name == "Earth":
            print('The eagle has landed.')
        elif self.location < 4:
            print("{} has a solid surface, however it is non inhabitable.").format(self.name)
        else:
            print("No solid surface on {}.").format(self.name)
    


class Moon(Universe_Builder):

    def set_name(self):
        self.name = self.moon[self.location]



def start_screen(s):
    if raw_input("Would you like to blast off and explore space? (Y/N) ").upper() == "Y":
        print(s().name)
    else:
        print("Trouble on the launch pad, Abort, Abort")


def game():
    solar_system_location = Universe_Builder().build_planets()
    start_screen(solar_system_location)
    

game()
# p.look()
# print p.name
# p.move(-1)
# p.look()
# print p.name
# p.move(1)
# p.land()
# p.move(3)
# p.land()
# p.move(2)
# p.land()
# p.move(-7)
# p.land()
# p.move(1)
# p.land()
# p.move(1)
# p.land()
