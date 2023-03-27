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

# Подсчет количества правильных решений для каждой группы
counts = {}
for _, _, group, _, status, _ in statuses:
    if group not in counts:
        counts[group] = 0
    if group in counts and status == '2':
        counts[group] += 1

# Построение графика
plt.bar(counts.keys(), counts.values())
plt.xticks(rotation=90)
plt.ylabel('Количество правильных решений')
plt.title('Количество правильных решений по группам')
plt.show()