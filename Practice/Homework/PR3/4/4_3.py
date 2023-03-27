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

# Создание словаря для хранения количества сообщений по задачам
message_counts = {}

# Подсчет количества сообщений для каждой задачи
for row in messages:
    task = row[1]
    task = str(int(task) + 1)
    if task not in message_counts:
        message_counts[task] = 0
    message_counts[task] += 1

# Создание гистограммы распределения количества сообщений по задачам
plt.bar(range(len(message_counts)), list(message_counts.values()), align='center')
plt.xticks(range(len(message_counts)), list(message_counts.keys()))
plt.xlabel('Задачи')
plt.ylabel('Количество сообщений')
plt.show()