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

numbers_copy = numbers.copy()

temp = numbers_copy[-1]
for i in range(len(numbers_copy) - 1, 0, -1):
 numbers_copy[i] = numbers_copy[i - 1]
numbers_copy[0] = temp

print("Исходный список:", numbers)
print("Список после циклического сдвига:", numbers_copy)
