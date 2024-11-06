#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include "common.h"

int main(void)
{
    char buf[MAX_BUF];
    int fd;

    /* Открываем FIFO для записи */
    if ((fd = open(FIFO_NAME, O_WRONLY)) < 0) {
        perror("open");
        exit(1);
    }

    /* Запрашиваем имя файла у пользователя */
    printf("Введите имя файла: ");
    fgets(buf, MAX_BUF, stdin);

    /* Удаляем символ новой строки */
    buf[strlen(buf) - 1] = '\0';

    /* Формируем строку для отправки серверу */
    char send_buf[MAX_BUF];
    sprintf(send_buf, "FILENAME~%s", buf);

    /* Отправляем строку серверу */
    if (write(fd, send_buf, strlen(send_buf)) < 0) {
        perror("write");
        exit(1);
    }

    /* Читаем данные от сервера */
    if (read(fd, buf, MAX_BUF) < 0) {
        perror("read");
        exit(1);
    }

    /* Выводим полученные данные */
    printf("Полученные данные: %s\n", buf);

    /* Закрываем FIFO */
    close(fd);

    return 0;
}