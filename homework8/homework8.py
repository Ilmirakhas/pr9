import random

def generate_ticket():
  """Генерирует случайный лотерейный билет с уникальными числами."""
  ticket = []
  all_numbers = list(range(1, 26))
  random.shuffle(all_numbers)

  for _ in range(5):
    row = all_numbers[:5]  
    all_numbers = all_numbers[5:] 
    ticket.append(row)
  return ticket

ticket = generate_ticket()

print("Лотерейный билет:")
for i in range(5):
    print(f"Строка {i + 1}: {ticket[i]}")

user_numbers = []
for i in range(5):
    while True:
        number_str = input(f"Введите число из строки {i + 1}: ")
        if number_str.isdigit():
            number = int(number_str)
            if 1 <= number <= 25 and number in ticket[i]:
                user_numbers.append(number)
                break
            else:
                print("Неверное число. Попробуйте снова.")
        else:
            print("Некорректный ввод. Введите целое число.")


computer_numbers = []
for row in ticket:
    computer_numbers.append(random.choice(row))


print("\nВаш билет:")
for i in range(5):
    print(f"Строка {i + 1}: {user_numbers[i]}")

print("\nБилет компьютера:")
for i in range(5):
    print(f"Строка {i + 1}: {computer_numbers[i]}")


matches = 0
for i in range(5):
    if user_numbers[i] == computer_numbers[i]:
        matches += 1

print("\nКоличество совпадений:", matches)




