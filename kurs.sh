#!/bin/bash

echo "Введите URL: "
read url

while true; do
  echo "Выберите действие:"
  echo "1) Показать список всех словарей на данном сервисом"
  echo "2) Отображение информации о библиотеках "
  echo "3) Вывести список команд, поддерживаемых данным сервисом"
  echo "4) Вывести список стратегий поиска, поддерживаемых данным сервисом"
  echo "5) Работа со словами: поиск определения слова, синонима, антонима"
  echo "0) Выход из программы"

  read choice

  #curl https://dict.org/bin/Dict

  case $choice in
    1)
      echo "Выполняется: Показать список всех словарей на данном сервисом"
      database=$(dict -D | head -n 166 | tail -n 165 | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8"\n"}')
      echo -ne "Словари: $database\n"
      ;;
    2)
      echo "Выполняется: Отображение информации о библиотеках"
      commands=$(dict -I | tail -n +3 | awk '{print $1" "$2" "$3" "$4" "$5" "$6" "$7"\n"}')
      echo -ne "$commands\n"
      ;;  
    3)
      echo "Выполняется: Вывести список команд, поддерживаемых данным сервисом"
      commands=$(dict --help | tail -n +4 | awk '{print $1" "$2" "$3" "$4" "$5" "$6" "$7"\n"}')
      echo "список команд $commands\n"
      ;;
    4)
      echo "Выполняется: Вывести список стратегий поиска, поддерживаемых данным сервисом"
      Strategy=$(curl -s "$url" | head -n 40 | tail -n 12 | awk '{print substr($0,index($0,">")+1)}')
      echo -ne "Название:\n $Strategy\n"
      ;;
    5)
      echo "Что вас интересует, поиск определения слова, синонима, антонима"
      echo "  1. Опредедение"
      echo "  2. Синоним"
      echo "  3. Антоним"

      read choice
      
      echo "Введите слово:"
      read word
      
      if [ "$choice" -eq 1 ]; then
        definition=$(dict "$word")
        echo "Определение(я) для '$word':"
        echo "$definition"
      fi
      if [ "$choice" -eq 2 ]; then
        url="https://api.dictionaryapi.dev/api/v2/entries/en/$word"
        synonym=$(curl -s "$url")
        echo "Синоним(ы) для '$word':"
        echo "$synonym" | grep -oP '(?<="synonyms":\[)[^\]]*' | tr -d '"' | tr ',' '\n'
      fi
      if [ "$choice" -eq 3 ]; then
        url="https://api.dictionaryapi.dev/api/v2/entries/en/$word"
        antonym=$(curl -s "$url")
        echo "Антоним(ы) для '$word':"
        echo "$antonym" | grep -oP '(?<="antonyms":\[)[^\]]*' | tr -d '"' | tr ',' '\n'
      fi
      ;;
    0)
      break
    ;;
  esac
done