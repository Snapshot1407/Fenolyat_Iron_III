from Point_1.detection import *
from Energy.covalent_energy import *


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
bonds, len_bonds = bond_n1(number, atoms)
#Вывести текущую энергию молекулы (учитываются только связи)
print("Энергия молекулы:", energy_dist(atoms, bonds))
bond_angles, len_bonds_angles = bond_n2(number,bonds)
print("Энергия молекулы:",energy_angle(atoms,bond_angles))

