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