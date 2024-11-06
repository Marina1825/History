import matplotlib.pyplot as plt

# Ваш цифровой бифазный код (пример)
digital_biphase_code = [1, -1, -1, 1, 1, -1, 1, -1]

# Временной интервал между отсчетами
time_interval = 1.0

# Создаем список временных точек для графика
time_points = [i * time_interval for i in range(len(digital_biphase_code))]

# Построение графика цифрового бифазного кода
plt.step(time_points, digital_biphase_code, where='mid', marker='o', color='b', linestyle='-')
plt.title('Цифровой бифазный код')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.ylim(-1.5, 1.5)  # Ограничиваем значения по оси Y

# Отображаем график
plt.show()