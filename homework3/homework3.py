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

odd_numbers = [number for number in numbers if  number % 2 != 0]

print("Нечетные элементы списка:", odd_numbers)



