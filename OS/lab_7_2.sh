#!/bin/bash
bash lab_7_1.sh &
id=$!

# Ожидание завершения процесса
# продолжительность ожидания в секундах

# Ожидание завершения первого задания
start=$(date +%s)
while wait $id; do
    wait $id
    time="$(($(date +%s) - $start))"
    printf "Продолжительность ожидания составила: $(date -u -d "@$time" +%H:%M:%S) \n"
    exit
done
