from numpy.random import random, randint
from Energy.covalent_energy import *
from Energy.noncovalent_energy import *
from math import sin, cos

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

            atom[1] += sin(30)
            atom[2] += sin(-45)
            atom[3] += sin(30)

            print(atom[0], atom[1], atom[2], atom[3], file = f2)

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
    while n < (frames):
        atom_id = randint(0, number - 1)

        plus_or_minus_x = randint(0,1)
        diff_x = random()
        atoms[atom_id][1] += diff_x if plus_or_minus_x == 0 else -diff_x

        plus_or_minus_y = randint(0,1)
        diff_y = random()
        atoms[atom_id][2] += diff_y if plus_or_minus_y == 0 else -diff_y

        plus_or_minus_z = randint(0,1)
        diff_z = random()
        atoms[atom_id][3] += diff_z if plus_or_minus_z == 0 else -diff_z



        E_dist1 = energy_dist(atoms,bonds)
        E_angle1 = energy_angle(atoms, bond_angles)
        E_VdV1 = energy_VdV(atoms,bond_vdv)

        if E_dist + E_angle + E_VdV > E_dist1 + E_angle1 + E_VdV1:
            n += 1
            E_dist = E_dist1
            E_angle = E_angle1
            E_VdV = E_VdV1
            print(round(E_dist + E_angle + E_VdV,5),n,sep='\t',file=f3)
            key = True
        else:
            atoms[atom_id][1] += diff_x if plus_or_minus_x == 1 else -diff_x
            atoms[atom_id][2] += diff_y if plus_or_minus_y == 1 else -diff_y
            atoms[atom_id][3] += diff_z if plus_or_minus_z == 1 else -diff_z
        if key:
            print(number, file=f2)
            print(n, file=f2)
            for atom in atoms:
                print(atom[0], atom[1], atom[2], atom[3], file=f2)
            key = False
    f2.close()
    f3.close()
    print(n)