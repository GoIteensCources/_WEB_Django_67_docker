# 1. Базове зображення: визначає основу, на якій будуватиметься образ.
# Використовуємо офіційний тонкий образ Python 3.9
FROM python:3.12-slim

# 2. Робочий каталог: встановлює робочий каталог всередині контейнера
WORKDIR /app

# 3. Копіювання залежностей: копіюємо requirements.txt на хост
COPY requirements.txt .

# 4. Встановлення залежностей: встановлює бібліотеки Python з файлу requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копіювання коду: копіює решту коду програми 
COPY . .

# 6. Відкриття порту: відкриває порт 8000 (або інший порт, який слухає Gunicorn) у контейнері 
EXPOSE 8000

# (Опціонально) Встановлення змінних середовища для налаштувань Production 
ENV DJANGO_SETTINGS_MODULE=dev_portfolio.settings
ENV SECRET_KEY="@(2elv+fb!dki3-x5tc76l!ezu-3ll+o+cr6eo%16pqyb-^uir"

# 7. Команда запуску: визначає команду, яка виконуватиметься при запуску контейнера 
# Тут використовується сервер розробки, але у production слід замінити на Gunicorn 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]