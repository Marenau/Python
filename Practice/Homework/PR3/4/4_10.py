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

# Подсчет количества ачивок для каждой группы
counts = {}
for _, _, group, _, _, achive in statuses:
    if group not in counts:
        counts[group] = 0
    lst = achive.split(',')
    if group in counts and lst[0] != '[]' and len(lst) > 1:
        counts[group] += len(achive.split(','))
        
# Построение графика
plt.bar(counts.keys(), counts.values())
plt.xticks(rotation=90)
plt.ylabel('Количество достижений')
plt.title('Решение задач различными способами')
plt.show()