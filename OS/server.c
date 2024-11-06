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
    int fd, data_fd;

    /* Создаем FIFO */
    if (mkfifo(FIFO_NAME, 0666) == -1) {
        perror("mkfifo");
        exit(1);
    }

    printf("Сервер запущен, ожидание клиента...\n");

    /* Открываем FIFO для чтения */
    if ((fd = open(FIFO_NAME, O_RDONLY)) < 0) {
        perror("open");
        exit(1);
    }

    /* Читаем данные из FIFO */
    if (read(fd, buf, MAX_BUF) < 0) {
        perror("read");
        exit(1);
    }

    /* Обрабатываем данные */
    char *filename = strtok(buf, "~");
    filename = strtok(NULL, "~");

    /* Открываем файл для чтения */
    if ((data_fd = open(filename, O_RDONLY)) < 0) {
        perror("open");
        exit(1);
    }

    /* Читаем данные из файла */
    if (read(data_fd, buf, MAX_BUF) < 0) {
        perror("read");
        exit(1);
    }

    /* Закрываем файл */
    close(data_fd);

    /* Отправляем данные обратно клиенту */
    if (write(fd, buf, strlen(buf)) < 0) {
        perror("write");
        exit(1);
    }

    /* Закрываем FIFO */
    close(fd);

    /* Удаляем FIFO */
    unlink(FIFO_NAME);

    return 0;
}