# Процедура для вывода списка групп
def print_groups():
    groups = {'ИВБО': 8, 'ИКБО': 33, 'ИМБО': 2, 'ИНБО': 13} # Словарь названий и количества групп
    
    for group_name, group_count in groups.items(): # Перебираем все группы
        print(group_name) # Выводим название группы
        transfer_flag = 0 # Флаг переноса
        for group_num in range(1, group_count + 1): # Перебираем все номера группы
            if group_name == 'ИКБО' and group_num in (23, 29): # Пропускаем некоторые номера группы ИКБО
                continue
            transfer_flag += 1
            print(f"{group_name}-{group_num:02d}-21", end=" ") # Выводим номер группы
            if transfer_flag % 10 == 0: # Переводим строку после каждой 10-й группы
                print()
        print("\n") # Переводим строку после вывода всех групп данной категории
        
print_groups()