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

# Создание словаря для хранения количества сообщений по группам
group_messages = {}

# Считывание количества сообщений для каждой группы
for message in messages[1:]:
    group = message[3]
    if group not in group_messages:
        group_messages[group] = 1
    else:
        group_messages[group] += 1

# Отображение результатов на графике
plt.bar(group_messages.keys(), group_messages.values())
plt.xticks(rotation=90)
plt.title('Количество сообщений по группам')
plt.ylabel('Количество сообщений')
plt.show()