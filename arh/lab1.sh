ls /sys/class/net#!/bin/bash 
data=$(date)
name=$(whoami)
dname=$(hostname)
model=$(cat /proc/cpuinfo | grep 'model name' | uniq)
arch=$(lscpu | grep 'Arch' | awk '{print $2}')
cpumax=$(lscpu | grep 'CPU max' | awk '{print $4}')
cpu=$(lscpu | grep 'cpu MHz' | uniq)
uniq=$(grep ^cpu\\scores /proc/cpuinfo | uniq |  awk '{print $4}')
core=$(lscpu | grep 'Thread(s) per core:' | awk '{print $4}')
zagruzca=$(mpstat | grep 'all'| awk '{print $12}')
L1=$(lscpu | grep 'L1d cache' | uniq)
L2=$(lscpu | grep 'L2 cache' | uniq)
L3=$(lscpu | grep 'L3 cache' | uniq)
mem=$( free | grep 'Mem' | awk '{print $2}')
memtotal=$( free | grep 'Mem' | awk '{print $3')
disk=$(echo "$disk_info" | awk 'NR==2 {print $2}')
diskopen=$(echo "$disk_info" | awk 'NR==2 {print $4}')
colvo=$(df -h | grep -c '^/dev/')
corn=$(df -h / | grep -v "Filesystem" | awk '{print $2}')
swapall=$(cat /proc/meminfo | grep 'SwapTotal' | awk '{print $2 " " $3}')
swap=$(cat /proc/meminfo | grep 'SwapFree' | awk '{print $2 " " $3}')
colip=$(ip -o l | wc -l)
echo "Дата: "$data";"
echo "Имя учетной записи: "$name";"
echo "Доменное имя ПК: "$dname";" 
echo "Процессор:"
echo "	Модель – "$model
echo "	Архитектура – "$arch
echo "	Тактовая частота максимальная – "$cpumax
echo "	Тактовая частота текущая (используемая) – "$cpu
echo "	Количество ядер – "$uniq
echo "	Количество потоков на одно ядро – "$core
echo "	Загрузка процессора – "$zagruzca
echo "Оперативная память:"
echo "	Cache L1 – "$L1
echo "	Cache L2 – "$L2
echo "	Cache L3 – "$L3
echo "	Всего – "$mem
echo "	Доступно – "$memtotal
echo "Жесткий диск:"
echo "	Всего – "$disk
echo "	Доступно – "$diskopen
echo "	Количество разделов – "$colvo
echo "По каждому разделу общий объём и доступное свободное место. Смонтировано в корневую директорию / – "
df -h | grep -v "tmpfs" | grep -v "udev"
echo "Смонтировано в корневую директорию"$corn
echo "Объём неразмеченного пространства - "
echo "	SWAP всего – "$swapall
echo "	SWAP доступно – "$swap
echo -ne "\nСетевые интерфейсы:"
echo -ne "\n	Количество сетевых интерфейсов – "$colip
MAC=$(ip -o l | grep 'eth0' | awk '{print $17}')
IP=$(ip -br a | grep 'eth0' |awk '{print $3}')
sv=$( ifconfig -a | grep 'ether' |awk '{print $5}')
sp=$(speedtest-cli --secure | grep 'Download' | awk '{print $2}')
echo -ne "\n№ Имя сетевого интерфейса\tМАС адрес\t\t\tIP адрес\t\tСтандарт связи\tСкорость соединения\n"
echo -ne "\teth0\t\t\t"$MAC " \t" $IP " \t\t"$sv"\t"$sp"\n"


name=$(curl -s "$url" | grep 'title' | awk '{print $2 " " $3 " " $4 " " $5 " " $6}')
echo "Название: "$name";"
name=$(curl -s "$url" | grep 'authors' | awk '{print $2 " " $3}')
echo "Автор (-ы): "$name";"
name=$(curl -s "$url" | grep 'description' | awk '{print $2 " " $3}')
echo "Аннотация: "$name";"

echo "Издательство: "$name";"
echo "Дата публикации: "$name";"
echo "Количество страниц: "$name";"
echo "Цена: "$name";"
echo "Формат (pdf или электронная книга epub): "$name";"
echo "Аннотация: "$name";"
echo "Ссылка для просмотра фрагмента: "$name";"
