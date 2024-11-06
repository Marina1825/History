#!/bin/bash

echo $TERM

echo "Идентификатор пользователя: "$UID
echo "Текушая дириктория: "$HOME
echo "Список дирикторий для обработки: "$PATH
echo "PS1: "$PS1
echo "PS2: "$PS2
echo "Рабочая текущая дериктория: "$PWD
cd ~marina
echo "мы зашли в домашнюю директориию"
echo "Зайти в папку и посмотреть содержимое STUDENT/ADMIN/FILE4.TEXT"
cat STUDENT/ADMIN/FILE4.TEXT
echo "*завершено*"
printf "Введите команду: "
read command
if [ -z "$command" ]; then
    echo "Ошибка: команда не была введена."
else
    $command
fi
