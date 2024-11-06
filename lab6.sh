#!bin/bash

echo "1) Используя перенаправление канала вывода вывести содержимое файла, созданного в лабораторной работе №1 в файл с именем Lab6"
cat STUDENT/ADMIN/FILE4.TEXT > lab6/LAB6
echo "1) Успешно"
echo "2) Убедитесь, что первое задание вами выполнено верно. Для этого выведите содержимое файла Lab6 на экран и сравните с исходным текстом."
cat STUDENT/ADMIN/FILE4.TEXT
cat lab6/LAB6
echo "2) Успешно"
echo "3) Вывести на экран содержимое файла /etc/passwd. Проанализировать полученную на экране информацию."
echo "имя_пользователя:зашифрованный_пароль:ID_пользователя:ID_группы:поле_описания:домашний_каталог:командная_оболочка"
cat /etc/passwd
echo "3) Успешно"
echo "4) Используя канал «конвейер» и перенаправление вывода выполнить следующие действия списком команд:"
echo " - Сделать текущим один из каталогов, созданный в лабораторной №1;"
echo " - Вывести оглавление этого каталога, если переход завершится успешно."
echo " - выдать содержимое файла /etc/passwd, отсортированное по имени пользователей в файл passwd.orig. ( для проведения сортировки файла"
echo "используйте команду sort);"
echo " - еще раз вывести оглавление текущего каталога"
cd  STUDENT/ADMIN/
ls
cat /etc/passwd | sort > passwd.orig
ls
echo "4) Успешно"
echo "5) Вывести на экран содержимое файла passwd.orig . Проанализируйте смысл файла passwd.orig."
echo "имя_пользователя:зашифрованный_пароль:ID_пользователя:ID_группы:поле_описания:домашний_каталог:командная_оболочка"
cat passwd.orig #дописать 'Проанализируйте смысл файла passwd.orig."
echo "5) Успешно"
echo "6) Используя перенаправление ввода с разделителем и перенаправление вывода добавить в файл passwd.orig информацию о новом пользователе согласно"
echo "формату записи файла /etc/passwd (все поля обязательно должны быть заполнены)."
echo "marina:x:1000:1000:marina:/home/marina:/bin/bash" >> passwd.orig
echo "6) Успешно"
echo "7) Выведите содержимое файла passwd.orig еще раз на экран. Убедитесь, что добавление записи прошло успешно."
cat passwd.orig
echo "7) Успешно"
