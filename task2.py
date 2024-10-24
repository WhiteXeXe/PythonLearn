# TODO Напишите функцию find_common_participants

def find_common_participants(fir, sec, raz = ","):
    v = []

    fir = fir.split(raz)
    sec = sec.split(raz)


    for i in fir:
        for j in sec:
            if (i == j):
                v.append(i)

    return sorted(v)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, "|"))