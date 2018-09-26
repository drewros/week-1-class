class Fish:
    name = "Zeek"
    color = "blue"

    def Swim(self):
        print ("Blub! My name is " + self.name)

myfish = Fish()
myfish.name = "Blubby"
print (myfish.name)

neighborfish = Fish()
neighborfish.name = "Jeff"

myfish.Swim()
neighborfish.Swim()
