import random

def is_number(s):

 for c in s:
  if not (c.isdigit() or c == "." or c == "," or c == "-"):
   return False
 return True

numbers = []
for _ in range(10):
 while True:
  number_str = str(random.randint(-100, 100))
  if is_number(number_str):
   numbers.append(int(number_str))
   break

print("Список чисел:", numbers)
for i in range(1, len(numbers)):
 if numbers[i] > numbers[i - 1]:
  print(numbers[i])

