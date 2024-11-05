def is_number(s):

  for c in s:
    if not (c.isdigit() or c == "." or c == "," or c == "-"):
      return False
  return True

numbers = []
while True:
  input_value = input("Введите число (end для завершения): ")
  if input_value == "end":
    break
  if is_number(input_value):
    numbers.append(float(input_value))
  else:
    print("Некорректный ввод. Введите число или 'end'.")

even_count = 0
odd_count = 0
for number in numbers:
  if number % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

print("Количество четных элементов:", even_count)
print("Количество нечетных элементов:", odd_count)


