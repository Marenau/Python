import csv
import datetime
import matplotlib.pyplot as plt

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

# id, task, variant, group, time
messages = load_csv('D:\messages.csv')

# id, message_id, time, status
checks = load_csv('D:\checks.csv')

# task, variant, group, time, status, achievements
statuses = load_csv('D:\statuses.csv')

# Извлечение временных меток из данных messages, checks и statuses
message_times = [parse_time(row[4]) for row in messages]
check_times = [parse_time(row[2]) for row in checks]
status_times = [parse_time(row[3]) for row in statuses]

# Объединение временных меток в один список
all_times = message_times + check_times + status_times

# Преобразование временных меток в часы суток
hour_of_day = [t.hour for t in all_times]

# Создание гистограммы распределения активности по часам суток
plt.hist(hour_of_day, bins=24, range=(0, 24))
plt.xlabel('Часы суток')
plt.ylabel('Количество событий')
plt.show()