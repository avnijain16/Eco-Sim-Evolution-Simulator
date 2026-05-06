from abc import ABC, abstractmethod

class Organism(ABC):

    def __init__(self, name, energy):
        self.name = name
        self.__energy = energy

    def get_energy(self):
        return self.__energy

    def gain_energy(self, value):
        self.__energy += value

    def lose_energy(self, value):
        self.__energy -= value

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def act(self, world):
        pass

class Plant(Organism):
    def __init__(self, name):
        super().__init__(name, 20)

    def move(self):
        print(self.name, "cannot move")

    def act(self, world):
        print(self.name, "is growing")
        print("Energy increased by 2")

        self.gain_energy(2)

class Animal(Organism):

    def move(self):
        print(self.name, "is moving")
        print("Energy decreased by 1")

        self.lose_energy(1)

class Herbivore(Animal):

    def __init__(self, name):
        super().__init__(name, 30)

    def act(self, world):
        self.move()
        for i in world.organisms[:]:
            if isinstance(i, Plant):
                print(self.name, "eats", i.name)
                print("Energy increased by 5")
                self.gain_energy(5)
                world.organisms.remove(i)
                break

class Carnivore(Animal):

    def __init__(self, name):
        super().__init__(name, 40)

    def act(self, world):
        self.move()
        for i in world.organisms[:]:
            if isinstance(i, Herbivore):
                print(self.name, "hunts", i.name)
                print("Energy increased by 10")

                self.gain_energy(10)
                world.organisms.remove(i)

                break


class World:

    def __init__(self):
        self.organisms = []

    def add(self, obj):
        self.organisms.append(obj)

    def run(self):
        print("\n--- NEW TURN ---")

        for i in self.organisms:
            print(i.name, "Energy =", i.get_energy())

        print()

        for i in self.organisms[:]:
            i.act(self)

        print("\nUpdated Energy:")

        for i in self.organisms:
            print(i.name, "=", i.get_energy())

world = World()

world.add(Plant("Grass"))
world.add(Plant("Tree"))

world.add(Herbivore("Rabbit"))
world.add(Carnivore("Tiger"))


for i in range(3):
    print("\nTURN", i + 1)
    world.run()
