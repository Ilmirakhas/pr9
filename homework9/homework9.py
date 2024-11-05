import re

def split_email(email):
 """
 Разделяет email на имя пользователя и доменное имя.

 Args:
  email: Email адрес.

 Returns:
  Словарь с ключами 'username' и 'domain', содержащий имя 
  пользователя и доменное имя соответственно. Если email не 
  соответствует формату, возвращает None.
 """
 match = re.match(r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$", email)
 if match:
  username, domain = match.groups()
  return {"username": username, "domain": domain}
 else:
  return None

# Получение email от пользователя
while True:
 email = input("Введите ваш email: ")
 email_parts = split_email(email)
 if email_parts:
  break
 else:
  print("Некорректный формат email. Попробуйте снова.")

# Вывод результата
print(f"Имя пользователя: {email_parts['username']}")
print(f"Доменное имя: {email_parts['domain']}")
