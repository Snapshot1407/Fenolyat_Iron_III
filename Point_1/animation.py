from random import random, randint, seed
from Energy.covalent_energy import *
from Energy.noncovalent_energy import *


#Создание простейшей анимации
def anim(number,atoms):
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
def optimus(number, atoms, frames, bonds, bond_angles,bond_vdv):
    f2 = open("optimus.xyz", "w")
    f3 = open('grafick.txt','w')
    print('Energy','time',sep='\t\t',file=f3)
    n = 0
    key = False
    E_dist = energy_dist(atoms,bonds)
    E_angle = energy_angle(atoms,bond_angles)
    E_VdV = energy_VdV(atoms,bond_vdv)
    for i in range(frames):
        atom_id = randint(0, number - 1)
        coord_id = randint(1, 3)
        diff = round(random(),5)
        plus_or_minus = randint(0,1)
        atoms[atom_id][coord_id] += diff if plus_or_minus == 0 else -diff
        E_dist1 = energy_dist(atoms,bonds)
        E_angle1 = energy_angle(atoms, bond_angles)
        E_VdV1 = energy_VdV(atoms,bond_vdv)

        if E_dist + E_angle + E_VdV > E_dist1 + E_angle1 + E_VdV1:
            n += 1
            E_dist = min(E_dist1,E_dist)
            E_angle = min(E_angle1,E_angle)
            E_VdV = min(E_VdV1,E_VdV)
            print(round(E_dist + E_angle + E_VdV,5),n,sep='\t',file=f3)
            key = True
        else:
            atoms[atom_id][coord_id] += diff if plus_or_minus == 1 else -diff
        if key:
            print(number, file=f2)
            print(n, file=f2)
            for atom in atoms:
                print(atom[0], atom[1], atom[2], atom[3], file=f2)
            key = False
    f2.close()
    f3.close()
    print(n)