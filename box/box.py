class Cuboid(object):
    # Create a class that represents a cuboid:
    # It should take its three dimensions as constructor parameters (numbers)
    # It should have a method called `get_surface` that returns the cuboid's surface
    # It should have a method called `get_volume` that returns the cuboid's volume

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def get_surface(self):
        self.surface = int((self.x * self.y + self.x * self.z + self.y * self.z) * 2)
        return self.surface

    def get_volume(self):
        self.volume = int(self.x * self.y * self.z)
        return self.volume

box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000
