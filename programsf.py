print("Программа рассчета уропа пушек!")
print()
canon_ist6 = int(input("Кол-во пушек Истязатель 6 ур: "))
canon_ist5 = int(input("Кол-во пушек Истязатель 5 ур: "))
canon_destroyer5 = int(input("Кол-во пушек Погибель 5 ур: "))
canon_destroyer4 = int(input("Кол-во пушек Погибель 4 ур: "))
canon_destroyer3 = int(input("Кол-во пушек Погибель 3 ур: "))


all_canon = canon_ist6 + canon_ist5 + canon_destroyer5 + canon_destroyer4 + canon_destroyer3
procent_canon_ist6 = (canon_ist6 / all_canon)
procent_canon_ist5 = (canon_ist5 / all_canon)

ed_dmg_ist6 = 110 * procent_canon_ist6
ed_dmg_ist5 = 110 * procent_canon_ist5
sum_ed = ed_dmg_ist6 + ed_dmg_ist5

sum_ist = ((canon_ist6 * 110) + (canon_ist5 * 100)) + ((canon_ist5 + canon_ist6) * (round(sum_ed, 2)))

sum_dest = ((canon_destroyer3 * 195) + (canon_destroyer4 * 224) + (canon_destroyer5 * 255)) + ((canon_destroyer5 + canon_destroyer4 + canon_destroyer3) * (round(sum_ed, 2)))

all_dmg = sum_ist + sum_dest

print(f'Урон пушек без ядре {all_dmg}')
