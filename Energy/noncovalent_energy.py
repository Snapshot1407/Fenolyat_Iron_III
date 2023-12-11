from Point_1.detection import *

ε = 0.25
σ = 3.345

#функция вычисления энергии по связям для молекулы
def energy_VdV(atoms, bonds):
    en_simple = 0
    for bond in bonds:
        nom_at_1 = bond[0]
        nom_at_2 = bond[1]
        rr = distance(atoms[nom_at_1], atoms[nom_at_2])
        σ_12 = pow(σ/rr,12)
        σ_6 = pow(σ/rr,6)
        en_simple += 4 * ε * (σ_12 - σ_6)
    return round(en_simple, 5)