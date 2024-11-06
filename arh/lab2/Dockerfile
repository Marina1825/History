# базовый образ с поддержкой C++
FROM ubuntu
RUN apt-get update && apt-get install -y g++ iproute2

# Копируем исходный код программы внутрь контейнера
COPY program.cpp /app/program.cpp
COPY container.txt /app/container.txt

# Компилируем программу
WORKDIR /app
RUN g++ -o program program.cpp

# Запускаем программу при запуске контейнера
CMD ["./program","container.txt"]