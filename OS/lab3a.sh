#!/bin/bash
read -p "Введите фамилию: " firstname
if [ -z "$firstname" ]; then
    firstname="Иванов"
fi
read -p "Введите имя: " name
if [ -z "$name" ]; then
    name="Иван"
fi
read -p "Введите отчество: " surname
if [ -z "$surname" ]; then
    surname="Иванович"
fi
echo "ФИО: "$firstname $name $surname

mkdir -p $firstname
touch ~/"$firstname"/"$name".txt
touch ~/"$firstname"/"$surname".txt

echo "$firstname" > firstname.txt

chmod -R o-r $firstname
chmod -R o+w $firstname



