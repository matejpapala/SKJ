
import playground
import random

from typing import List, Tuple, NewType

Pos = NewType('Pos', Tuple[int, int])


class Atom:

    def __init__(self, pos: Pos, vel: Pos, rad: int, col: str):
        """
        Initializer of Atom class

        :param x: x-coordinate
        :param y: y-coordinate
        :param rad: radius
        :param color: color of displayed circle
        """
        self.x = pos[0]
        self.y = pos[1]
        self.velX = vel[0]
        self.velY = vel[1]
        self.rad = rad
        self.color = col

    def to_tuple(self) -> Tuple[int, int, int, str]:
        """
        Returns tuple representing an atom.

        Example: pos = (10, 12,), rad = 15, color = 'green' -> (10, 12, 15, 'green')
        """
        return (self.x, self.y, self.rad, self.color)

    def apply_speed(self, size_x: int, size_y: int):
        """
        Applies velocity `vel` to atom's position `pos`.

        :param size_x: width of the world space
        :param size_y: height of the world space
        """
        if self.x - self.rad <= 0 or self.x + self.rad >= size_x:
            self.velX = -self.velX
            
        if self.y - self.rad <= 0 or self.y + self.rad >= size_y:
            self.velY = -self.velY

        self.x += self.velX
        self.y += self.velY


class FallDownAtom(Atom):
    """
    Class to represent atoms that are pulled by gravity.
     
    Set gravity factor to ~3.

    Each time an atom hits the 'ground' damp the velocity's y-coordinate by ~0.7.
    """
    g = 4.0
    damping = 0.7

    def apply_speed(self, size_x, size_y):
        self.velY += self.g

        if self.y + self.rad >= size_y and self.velY > 0:
            self.velY *= self.damping

        super().apply_speed(size_x, size_y)


class ExampleWorld:

    def __init__(self, size_x: int, size_y: int, no_atoms: int, no_falldown_atoms: int):
        """
        ExampleWorld initializer.

        :param size_x: width of the world space
        :param size_y: height of the world space
        :param no_atoms: number of 'bouncing' atoms
        :param no_falldown_atoms: number of atoms that respect gravity
        """

        self.width = size_x
        self.height = size_y
        self.no_atoms = no_atoms
        self.no_falldown_atoms = no_falldown_atoms
        self.atoms = self.generate_atoms(self.no_atoms, self.no_falldown_atoms)

    def generate_atoms(self, no_atoms: int, no_falldown_atoms) -> List[Atom|FallDownAtom]:
        """
        Generates `no_atoms` Atom instances using `random_atom` method.
        Returns list of such atom instances.

        :param no_atoms: number of Atom instances
        :param no_falldown_atoms: numbed of FallDownAtom instances
        """
        generated_atoms = []
        for _ in range(no_atoms):
            generated_atoms.append(self.random_atom())

        for _ in range(no_falldown_atoms):
            generated_atoms.append(self.random_falldown_atom())

        return generated_atoms

    def random_atom(self) -> Atom:
        """
        Generates one Atom instance at random position in world, with random velocity, random radius
        and 'green' color.
        """
        return Atom((random.randint(0, self.width), random.randint(0, self.height)), (random.randint(-10, 10), random.randint(-8, 8)), random.randint(5, 15), 'green')

    def random_falldown_atom(self):
        """
        Generates one FalldownAtom instance at random position in world, with random velocity, random radius
        and 'yellow' color.
        """
        return FallDownAtom((random.randint(0, self.width), random.randint(0, self.height)), (random.randint(-10, 10), random.randint(-8, 8)), random.randint(5, 15), 'yellow')
        pass

    def add_atom(self, pos_x, pos_y):
        """
        Adds a new Atom instance to the list of atoms. The atom is placed at the point of left mouse click.
        Velocity and radius is random.

        :param pos_x: x-coordinate of a new Atom
        :param pos_y: y-coordinate of a new Atom

        Method is called by playground on left mouse click.
        """
        vel_x = random.randint(-10, 10)
        vel_y = random.randint(-8, 8)
        rad = random.randint(5, 15)
        
        new_atom = Atom((pos_x, pos_y), (vel_x, vel_y), rad, 'green')
        self.atoms.append(new_atom)

    def add_falldown_atom(self, pos_x, pos_y):
        """
        Adds a new FallDownAtom instance to the list of atoms. The atom is placed at the point of right mouse click.
        Velocity and radius is random.

        Method is called by playground on right mouse click.

        :param pos_x: x-coordinate of a new FallDownAtom
        :param pos_y: y-coordinate of a new FallDownAtom
        """
        vel_x = random.randint(-10, 10)
        vel_y = random.randint(-8, 8)
        rad = random.randint(5, 15)

        new_atom = FallDownAtom((pos_x, pos_y), (vel_x, vel_y), rad, 'yellow')
        self.atoms.append(new_atom)
        pass

    def tick(self):
        """
        Method is called by playground. Sends a tuple of atoms to rendering engine.

        :return: tuple or generator of atom objects, each containing (x, y, radius, color) attributes of atom 
        """

        for atom in self.atoms:
            atom.apply_speed(self.width, self.height)

        return tuple(atom.to_tuple() for atom in self.atoms)


if __name__ == '__main__':
    size_x, size_y = 700, 400
    no_atoms = 4
    no_falldown_atoms = 3

    world = ExampleWorld(size_x, size_y, no_atoms, no_falldown_atoms)

    playground.run((size_x, size_y), world)
