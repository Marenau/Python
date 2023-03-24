import csv
import datetime
import matplotlib.pyplot as plt

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

# id, task, variant, group, time
messages = load_csv('messages.csv')

# id, message_id, time, status
checks = load_csv('checks.csv')

# task, variant, group, time, status, achievements
statuses = load_csv('statuses.csv')

activity_by_hour = {}

for message in messages[1:]:
    timestamp = parse_time(message[4])
    hour = timestamp.hour
    
    if hour in activity_by_hour:
        activity_by_hour[hour] += 1
    else:
        activity_by_hour[hour] = 1

x = list(activity_by_hour.keys())
y = list(activity_by_hour.values())

plt.plot(x, y)
plt.xlabel('Hour')
plt.ylabel('Number of messages')
plt.title('Student activity by hour')
plt.show()