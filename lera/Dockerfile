FROM python:3.8-slim
RUN apt-get update && apt-get install -y iproute2
# Создайте рабочий каталог внутри контейнера
WORKDIR /app

# Копируйте файл с вашим Python-скриптом в контейнер
COPY my_program.py /app/

# Копируйте файл izol.txt в контейнер
COPY izol.txt /app/

# Запустите программу при запуске контейнера
CMD ["python", "my_program.py"]