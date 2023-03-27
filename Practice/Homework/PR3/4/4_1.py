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

# Создание словаря, где ключами являются дни недели (0-6), а значениями - количество сообщений/статусов
message_counts = {i: 0 for i in range(7)}
status_counts = {i: 0 for i in range(7)}

# Обход всех сообщений и подсчет количества сообщений по дням недели
for message in messages:
    day_of_week = parse_time(message[4]).weekday()
    message_counts[day_of_week] += 1
    
# Обход всех статусов и подсчет количества статусов по дням недели
for status in statuses:
    day_of_week = parse_time(status[3]).weekday()
    status_counts[day_of_week] += 1

# Отображение графика с количеством сообщений и статусов по дням недели
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.bar(range(len(days_of_week)), message_counts.values(), align='center', color='b', label='Messages')
plt.bar(range(len(days_of_week)), status_counts.values(), align='center', color='r', label='Statuses')
plt.xticks(range(len(days_of_week)), days_of_week)
plt.xlabel('Day of the week')
plt.ylabel('Number of messages/statuses')
plt.legend()
plt.show()