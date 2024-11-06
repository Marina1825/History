#!/bin/bash

query="" #поисковый запрос
lang="en" #язык поиска
sort="relevance" #тип сортировки результатов
maxres="10" #максимальное количество результатов

#формирование текста для запроса
while [[ $# -gt 0 ]]
do
    key="$1"

    case $key in
        --query=*)
        query="${key#*=}"
        query="${query// /+}" 
        shift
        ;;
        --lang=*)
        lang="${key#*=}"
        shift
        ;;
        --sort=*)
        sort="${key#*=}"
        shift
        ;;
        --maxres=*)
        maxres="${key#*=}"
        shift
        ;;
        *)
        echo "Unknown option: $key"
        exit 1
        ;;
    esac
done

if [ -z "$query" ]
then
    echo "Query is empty"
    exit 1
fi

#запрос к сайтту для полученияя информации по книгам
url="https://www.googleapis.com/books/v1/volumes?q=$query&langRestrict=$lang&orderBy=$sort&maxResults=$maxres"
#echo "$(curl -s "$url")"

name=$(curl -s "$url" | grep 'title' | awk '{$1=""; print substr($0, 1, length($0)-1)}')
echo -ne "\n Название: "$name";\n" #название книги

avtor=$(curl -s "$url" | head -n 13 | tail -n 1)
echo -ne "\n Автор (-ы): "$avtor";\n" #автор книги

annotation=$(curl -s "$url" | grep 'description' | awk '{$1=""; print substr($0, 1, length($0)-1)}')
echo -ne "\n Аннотация: "$annotation".;\n" #аннотация к книге

publishing=$(curl -s "$url" | grep 'publisher' | awk '{$1=""; print $0}' | grep -o '[a-zA-Z]*')
echo -ne "\n Издательство: "$publishing";\n" #издательство

date=$(curl -s "$url" | grep 'published' | awk '{$1=""; print substr($0, 1, length($0)-1)}' | grep -o '[0-9]*')
echo -ne "\n Дата публикации: "$date";\n" #дата публикации

pages=$(curl -s "$url" | grep 'pageCount' | awk '{$1=""; print substr($0, 1, length($0)-1)}' )
echo -ne "\n Количество страниц: "$pages";\n" #количество страниц

prise=$(curl -s "$url" | grep -m 1 'amount' | awk '{$1=""; print substr($0, 1, length($0)-1)}')
echo -ne "\n Цена: "$prise";\n" #цена книги

form=$(curl -s "$url" | grep 'printType' | awk '{$1=""; print substr($0, 1, length($0)-1)}' | grep -o '[a-zA-Z]*')
echo -ne "\n Формат (pdf или электронная книга epub): "$form";\n" #формат книги

link=$(curl -s "$url" | grep 'buyLink' | awk '{$1=""; print $0}')
echo -ne "\n Ссылка для просмотра фрагмента: "$link".\n" #ссылка для просмотра фрагмента книги