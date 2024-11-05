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
      numbers.append(float(number_str))
      break

min_index = 0
max_index = 0
for i in range(1, len(numbers)):
  if numbers[i] < numbers[min_index]:
    min_index = i
  if numbers[i] > numbers[max_index]:
    max_index = i

print(f"Минимальный элемент: {numbers[min_index]} \nМаксимальный элемент: {numbers[max_index]}")

numbers_copy = numbers.copy()
numbers_copy[min_index], numbers_copy[max_index] = numbers_copy[max_index], numbers_copy[min_index]

print("Исходный список:", numbers)
print("Список с поменянными элементами:", numbers_copy)


