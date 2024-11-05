def squares(a, b):

  if not num(a) or not num(b):
    return "Ошибка: введены некорректные значения."

  a = int(float(a))
  b = int(float(b))

  gsquares = []

  if a > b:
    for i in range(b + 1, a):
      gsquares.append(i * i)
    gsquares.reverse()
  else:
    for i in range(a + 1, b):
      gsquares.append(i * i)

  return gsquares

def num(s):

  for c in s:
    if not (c.isdigit() or c == "." or c == "," or c == "-"):
      return False

  return True

a = input("Введите число a: ")
b = input("Введите число b: ")

gsquares = squares(a, b)

print(gsquares)


