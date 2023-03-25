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

# Подсчет количества отправленных решений для каждой задачи
counts = {}
for task, _, _, _, status, _ in statuses:
    task = str(int(task) + 1)
    if task not in counts:
        counts[task] = 0
    if task in counts and status != '2':
        counts[task] += 1

# Построение графика
plt.bar(counts.keys(), counts.values())
plt.xticks(rotation=90)
plt.ylabel('Количество попыток')
plt.title('Количество попыток решения задачи')
plt.show()