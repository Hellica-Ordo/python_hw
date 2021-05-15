# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def profile(name, surname, birth_year, city, email, phone_number):
    return f"Ваши данные:{name} {surname}, год рождения {birth_year}. Контактная информация: {city}, телефон {phone_number}, e-mail {email}."

print(profile(surname = input('Ваша фамилия: '), name = input('Ваше имя: '), birth_year = input('Ваш год рождения: '), email = input('Электронная почта: '),
              phone_number = int(input('Телефон для связи: ')), city = input('Город проживания: ')))