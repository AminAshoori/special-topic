import random

# تنظیم Seed
random.seed(400121028)

# تعداد درایه ها
n = 10000

# لیست برای ذخیره اعداد تصادفی
numbers = []

# تولید اعداد تصادفی بین 0 تا 20
for i in range(n):
  numbers.append(random.randint(0, 20))

# شمارش تعداد تکرار هر عدد
counts = [0] * 21

for number in numbers:
  counts[number] += 1

# چاپ تعداد تکرار هر عدد
for i in range(21):
  print(f"عدد {i}: {counts[i]}")