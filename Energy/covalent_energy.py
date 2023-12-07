from Point_1.detection import *
#Словарь для расчёта энергии по связям, равновесные длины связей C, H, O and Fe
en_b = {}
en_b["CC"] = [1050, 1.39, 25, 2, 1] # заготовка под ВДВ взаимодействие
en_b["CH"] = [700, 1.02]
en_b["HC"] = [700, 1.02]
en_b["FeO"] = [700, 1.835] # заготовка под ВДВ взаимодействие( подскажите для железа кислорода пожалуйста ;) )
en_b["OFe"] = [700, 1.835] # заготовка под ВДВ взаимодействие( подскажите для железа кислорода пожалуйста ;) )
en_b["OC"] = [1400, 1.25, 2, 2, 1] # заготовка под ВДВ взаимодействие
en_b["CO"] = [1400, 1.25, 2, 2, 1] # заготовка под ВДВ взаимодействие
# равновесные константы для углов, по трем точкам
en_b["O"] = [100, 1.824043601]
en_b["Fe"] = [100, 1.57]
en_b["C"] = [100, 2.094395102]



#функция вычисления энергии изгиба по углу для молекулы
def energy_angle(atoms, bonds):
    en_simple = 0
    for bond in bonds:
        nom_at_1 = atoms[bond[0]]
        nom_at_2 = atoms[bond[1]]
        nom_at_3 = atoms[bond[2]]
        intersection = nom_at_1[0]  # точка пересечения( атом связывающий два остальных)
        K_ug = en_b.get(intersection)[0]
        angle_ravn = en_b.get(intersection)[1]
        angle_angle = angle(nom_at_1,nom_at_2,nom_at_3) #нахождение угла в радианах
        en_simple += 0.5 * K_ug * (angle_angle - angle_ravn) ** 2
    return en_simple

#функция вычисления энергии по связям для молекулы
def energy_dist(atoms, bonds):
    en_simple = 0
    for bond in bonds:
        nom_at_1 = bond[0]
        nom_at_2 = bond[1]
        name_at_1 = atoms[nom_at_1][0]
        name_at_2 = atoms[nom_at_2][0]
        full_name = name_at_1 + name_at_2
        K_sv = en_b.get(full_name)[0]
        r_ravn = en_b.get(full_name)[1]
        rr = distance(atoms[nom_at_1], atoms[nom_at_2])
        en_simple += 0.5 * K_sv * (rr - r_ravn) ** 2
    return en_simple
