from random import random, randint
from Energy.covalent_energy import *
#Создание простейшей анимации
def anim (number,atoms):
    f2 = open("animation.xyz", "w")

    frames = 20
    diff = 0

    for i in range(frames):
        diff += 0.1
        print(number, file = f2)
        print(i, file = f2)
        for atom in atoms:
            print(atom[0], atom[1] + diff, atom[2], atom[3], file = f2)

    f2.close()
def optimus(number, atoms, frames, bonds, bond_angles):
    f2 = open("optimus.xyz", "w")
    n = 0
    key = False
    E_dist = energy_dist(atoms,bonds)
    E_angle = energy_angle(atoms,bond_angles)
    for i in range(frames):
        atom_id = randint(0, number - 1)
        coord_id = randint(1, 3)
        diff = round(random(),5)
        plus_or_minus = randint(0,1)
        print(f'atom_id: {atom_id}\n'
              f'coord_id: {coord_id}\n'
              f'diff: {diff}\n'
              f'plus_or_minus: {plus_or_minus}')
        atoms[atom_id][coord_id] += diff if plus_or_minus == 0 else -diff
        E_dist1 = energy_dist(atoms,bonds)
        E_angle1 = energy_angle(atoms, bond_angles)
        if E_dist < E_dist1:
            n += 1
            E_dist = E_dist1
            key = True

        elif E_angle < E_angle1:
            n += 1 if not key else 0
            E_angle = E_angle1
            key = True
        if key:
            print(number, file=f2)
            print(n, file=f2)
            for atom in atoms:
                print(atom[0], atom[1], atom[2], atom[3], file=f2)
            key = False
    f2.close()
