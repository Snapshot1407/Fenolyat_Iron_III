from numpy import arccos

def mass(atoms):
    #Поиск центра масс плоской молекулы (z = 0), состоящей из атомов углерода и водорода
    mass = {'C': 12, 'H': 1, "O": 16, "Fe": 56}  # словарь с значениями масс, ключ является название атома
    x_mass = 0
    y_mass = 0
    z_mass = 0
    mass_mol = 0
    for i in atoms:
        x_mass += (mass[i[0]] * float(i[1]))
        y_mass += (mass[i[0]] * float(i[2]))
        z_mass += (mass[i[0]] * float(i[3]))
        mass_mol = mass_mol + mass[i[0]]
    return x_mass / mass_mol, y_mass / mass_mol, z_mass/mass_mol


#Функция вычислениия дистанции между атомами
def distance(atom1, atom2):
    dist2 = 0
    for i in range(1, len(atom1)):
        dist2 += (atom1[i] - atom2[i]) ** 2
    return dist2 ** 0.5

#Найти все связи в молекуле и запомнить их, чтобы потом можно было обращаться к атомам в связи.
def bond_n1(number, atoms):
    bonds = []
    for n1 in range(number):
        atom1 = atoms[n1]
        for n2 in range(n1 + 1, number):
            atom2 = atoms[n2]
            if atom2[0] == 'C' and atom1[0] == "C":
                r = 1.63
            elif atom2[0] == 'C' and atom1[0] == "H" or atom2[0] == 'H' and atom1[0] == "C":
                r = 1.54
            elif atom2[0] == 'C' and atom1[0] == "O" or atom2[0] == 'O' and atom1[0] == "C":
                r = 1.32
            elif atom2[0] == 'Fe' and atom1[0] == "O" or atom2[0] == 'O' and atom1[0] == "Fe":
                r = 1.935
            if distance(atom1,atom2) < r:
                bonds.append([n1, n2])
    return bonds, len(bonds)

#Найти все связи в молекуле для образования угла по трем точкам, запомнить их, чтобы потом можно было обращаться к атомам в связи.
#первый атом является центральным, точкой пересечения векторов в пространстве
def bond_n2(number, bonds):
    bond_angles = list()
    for i in range(number):
        neighbour = list()
        len_bond = 0
        for bond in bonds:
            if i == bond[0]:
                len_bond += 1
                neighbour.append(i)
                neighbour.append(bond[1])
            elif i == bond[1]:
                len_bond += 1
                neighbour.append(i)
                neighbour.append(bond[0])
            if len_bond == 2:
                len_bond = 0
                c = sorted(list(set(neighbour)))
                bond_angles.append(c)
    return bond_angles, len(bond_angles)

#Функция вычислениия дистанции между атомами
#первый атом является центральным, точкой пересечения векторов в пространстве
def angle(atom1, atom2, atom3):
    ax, ay, az = (atom1[1] - atom2[1]), (atom1[2] - atom2[2]), (atom1[3] - atom2[3])
    bx = (atom1[1] - atom3[1])
    by = (atom1[2] - atom3[2])
    bz = (atom1[3] - atom3[3])
    return arccos( (ax*bx + ay*by + az*bz) / (distance(atom1,atom2) * distance(atom1,atom3)) )
