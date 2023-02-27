import random
all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
max_len = 10
print("".join(random.choice(all_chars) for _ in range(random.randint(1, max_len))))
