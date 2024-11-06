import os
import sys

# Функция для вывода содержимого файла
def print_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Содержимое файла {file_path}:\n{content}")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    # Чтение переменной среды окружения
    env_var_path = os.getenv("MYVAR")

    if env_var_path:
        print_file_content(env_var_path)
    else:
        print("Переменная окружения MYVAR не установлена.")

    # Бесконечный цикл, программа не завершит свою работу до получения сигнала остановки
    while True:
        pass
