import csv
import datetime
import matplotlib.pyplot as plt

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

# id, task, variant, group, time
messages = load_csv('C:\Python\messages.csv')

# id, message_id, time, status
checks = load_csv('C:\Python\checks.csv')

# task, variant, group, time, status, achievements
statuses = load_csv('C:\Python\statuses.csv')

# Создание словарей для хранения времени сообщений, проверок и изменения статусов по задачам
message_times = {}
check_times = {}
status_times = {}

# Заполнение словарей времени сообщений, проверок и изменения статусов по задачам
for row in messages:
    task = row[1]
    time = datetime.datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f')
    if task not in message_times:
        message_times[task] = []
    message_times[task].append(time)

for row in checks:
    task = row[1]
    time = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')
    if task not in check_times:
        check_times[task] = []
    check_times[task].append(time)

for row in statuses:
    task = row[0]
    time = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
    if task not in status_times:
        status_times[task] = []
    status_times[task].append(time)

# Создание графиков для каждой задачи
for task in message_times.keys():
    times = message_times[task] + check_times.get(task, []) + status_times.get(task, [])
    times.sort()

    # Создание списка с количеством сообщений/проверок/статусов на каждый день
    activity = []
    current_day = times[0].date()
    count = 0
    for time in times:
        if time.date() != current_day:
            activity.append(count)
            count = 0
            current_day = time.date()
        count += 1
    activity.append(count)

    # Создание графика активности студентов по задаче за период с начала семестра
    plt.plot(activity)
    plt.xlabel('Дни с начала выгрузки задачи')
    plt.ylabel('Количество сообщений/проверок/статусов')
    plt.title(f'Задача "{int(task) + 1}"')
    plt.show()