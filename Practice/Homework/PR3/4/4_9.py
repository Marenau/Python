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

# Подсчет количества ачивок для каждого студента
counts = {}
for _, var, group, _, _, achive in statuses:
    var = str(int(var) + 1)
    var_and_group = var + " " + group
    if var_and_group not in counts:
        counts[var_and_group] = 0
    lst = achive.split(',')
    if var_and_group in counts and lst[0] != '[]' and len(lst) > 1:
        counts[var_and_group] += len(achive.split(','))
        
# Построение графика
counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
keys = list(counts.keys())
values = list(counts.values())
plt.bar(keys[:10:], values[:10:])
plt.xticks(rotation=90)
plt.ylabel('Количество достижений')
plt.title('Топ-10 студентов по достижениям')
plt.show()