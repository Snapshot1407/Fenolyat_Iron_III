from Point_1.animation import *
from Energy.covalent_energy import *
from Energy.noncovalent_energy import *

#Сделать так, чтобы координаты атомов преобразовались из строкового типа в числа (название атома atom[0] мы игнорируем, так как это не число)
def unpacking(atom):
    return [str(atom[0]),float(atom[1]),float(atom[2]),float(atom[3])]

f = open("fenolyat.xyz", "r")

number = int(f.readline())
name = f.readline()

print("Atoms:", number)
print("Name:", name)


#Записать атомы и их координаты в список atoms
atoms = []
for line in f:
    atoms.append(unpacking(line.split()))

#Закрыть файл, так как он больше не нужен
f.close()



print("Центр массы молекулы:", *mass(atoms))

bonds = bond_n1(number, atoms)
bond_angles = bond_n2(number,bonds)

#Вывести текущую энергию молекулы (учитываются только связи)
print("Энергия молекулы (учитываются только связи):", energy_dist(atoms, bonds))
bond, len_b = bond_n3(bonds,bond_angles)

#Вывести текущую энергию молекулы (учитываются только углы)
print("Энергия молекулы(учитываются только углы):",energy_angle(atoms,bond_angles))
bond_vdv, len_vdv = filter_circle(atoms,bond,len_b)

#Вывести текущую энергию молекулы (учитываются только взаимодействие Ван-дер-Вальса)
print("Энергия молекулы(учитываются только взаимодействие Ван-дер-Вальса):",energy_VdV(atoms,bond_vdv))

#оптимизация молекулы
optimus(number, atoms, 50000, bonds, bond_angles,bond_vdv)
print("Энергия молекулы (учитываются только связи):", energy_dist(atoms, bonds))
print("Энергия молекулы(учитываются только углы):",energy_angle(atoms,bond_angles))
print("Энергия молекулы(учитываются только взаимодействие Ван-дер-Вальса):",energy_VdV(atoms,bond_vdv))

