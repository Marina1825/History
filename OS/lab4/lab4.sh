#!/bin/bash

while true; do
    echo "Меню:"
    echo "1) Копирование файла"
    echo "2) Перемещение файла"
    echo "3) Создание файла"
    echo "0) Выход"

    read -p "Выберите пункт меню: " choice

    case $choice in
        1)
            read -p "Введите имя файла для копирования: " filename
	    if [[ -z "$filename" ]]; then
		echo "Ошибка: вы не ввели имя файла."
		continue
	    fi
            read -p "Введите подкаталог откуда копировать (пустая строка для текущего каталога): " directory_old
	    if [[ -f "$directory_old" ]]; then
		echo "Ошибка: данная деректория не найдена."
		continue
	    fi
	    if [[ ! -f "${directory_old}/${filename}" ]]; then
		echo "Ошибка файла $filename нет в директории $directory_old"
		continue
	    fi
	    read -p "Введите подкаталог для сохранения копии файла (пустая строка для текущего каталога): " directory_new
	    if [[ -f "$directory_new" ]]; then
		echo "Данная деректория не найдена. Создание директории."
		mkdir "$directory_new"
	    fi
	    if [[ -f "${directory_new}/${filename}" ]];  then
                echo "Ошибка: файл с именем $filename уже существует."
                continue
            fi
	    if [[ -n "$directory_old" && ! -d "$directory_old" ]]; then
                if [[ -n "$directory_new" && ! -d "$directory_new" ]]; then
                    cp "$filename" "$filename"
                else
                    cp "$filename" "${directory_new}/${filename}"
                fi
            else
                if [[ -n "$directory_new" && ! -d "$directory_new" ]]; then
                    cp "${directory_old}/${filename}" "$filename"
                else
                    cp "${directory_old}/${filename}" "${directory_new}/${filename}"
                fi
            fi
	    echo "Файл успешно скопирован."
            ;;
        2)
            read -p "Введите имя файла для перемещения: " filename
	    if [[ -z "$filename" ]]; then
                echo "Ошибка: вы не ввели имя файла."
                continue
            fi
	    read -p "Введите подкаталог откуда перемещаете (пустая строка для текущего каталога): " directory_old
            if [[ -f "$directory_old" ]]; then
                echo "Ошибка: данная деректория не найдена."
                continue
            fi
            if [[ ! -f "${directory_old}/${filename}" ]]; then
                echo "Ошибка файла $filename нет в директории $directory_old"
                continue
            fi
	    read -p "Введите подкаталог куда перемещаете (пустая строка для текущего каталога): " directory_new
	    if [[ -f "$directory_new" ]]; then
                echo "Данная деректория не найдена. Создание директории."
                mkdir "$directory_new"
            fi
	    if [[ -f "${directory_new}/${filename}" ]];  then
		echo "Ошибка: файл с именем $filename уже существует."
                continue
            fi
	    if [[ -n "$directory_old" && ! -d "$directory_old" ]]; then
		if [[ -n "$directory_new" && ! -d "$directory_new" ]]; then
                    mv "$filename" "$filename"
		else
                    mv "$filename" "${directory_new}/${filename}"
                fi
	    else
		if [[ -n "$directory_new" && ! -d "$directory_new" ]]; then
                    mv "${directory_old}/${filename}" "$filename"
                else
                    mv "${directory_old}/${filename}" "${directory_new}/${filename}"
                fi
	    fi

            echo "Файл успешно перемещен."
            ;;
        3)
            read -p "Введите имя файла для создания: " filename
	    if [[ -z "$filename" ]]; then
                echo "Ошибка: вы не ввели имя файла."
                continue
            fi
            read -p "Введите подкаталог для создания файла (пустая строка для текущего каталога): " directory

            if [[ -n "$directory" && ! -d "$directory" ]]; then
                echo "Указанный подкаталог не существует. Создается директория."
		mkdir "$directory"
		touch "${directory}/${filename}"
		continue
            fi

            if [[ -z "$directory" ]]; then
                if [[ -f "$filename" ]];  then
                    echo "Ошибка: файл с именем $filename уже существует."
                    continue
                fi
		touch "$filename"
            else
		if [[ -f "${directory}/${filename}" ]];  then
                    echo "Ошибка: файл с именем $filename уже существует."
                    continue
                fi
                touch "${directory}/${filename}"
            fi

            echo "Файл успешно создан."
            ;;
        0)
            echo "Выход из программы."
            exit
            ;;
        *)
            echo "Ошибка: недопустимая опция. Пожалуйста, выберите пункт меню от 0 до 3."
            ;;
    esac

    echo
done
