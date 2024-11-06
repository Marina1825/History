#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include "common.h"

#define MAX_ROUTE_LEN 100
#define MAX_ROUTES 10

typedef struct {
    char start[MAX_ROUTE_LEN];
    char end[MAX_ROUTE_LEN];
    int number;
} Route;

int main() {
    char buf[MAX_LEN];
    int fd, bytes_read;

    /* Создание именованного канала */
    mkfifo(FIFO_NAME, 0666);

    /* Открытие именованного канала */
    fd = open(FIFO_NAME, O_RDWR);

    /* Чтение из именованного канала */
    while(1) {
        bytes_read = read(fd, buf, MAX_LEN);
        buf[bytes_read] = '\0';

        /* Проверка на соответствие формату "FileName- имяфайла" */
        if(strncmp(buf, "FileName-", 9) == 0) {
            printf("Received file name: %s\n", buf + 9);

            /* Открытие файла */
            FILE *file = fopen(buf + 9, "r");
            if(file == NULL) {
                printf("Failed to open file\n");
                return 1;
            }

            /* Чтение файла */
            Route routes[MAX_ROUTES];
            int i;
            for(i = 0; i < MAX_ROUTES; i++) {
                fscanf(file, "%s %s %d", routes[i].start, routes[i].end, &routes[i].number);
            }

            /* Запись в новый файл */
            FILE *new_file = fopen("new_file.txt", "w");
            if(new_file == NULL) {
                printf("Failed to open new file\n");
                return 1;
            }

            for(i = 0; i < MAX_ROUTES; i++) {
                fprintf(new_file, "%s %s %d\n", routes[i].start, routes[i].end, routes[i].number);
            }
            printf("3");
            fclose(new_file);
            fclose(file);
            printf("5");
            write(fd, "new_file.txt", 13);
            printf("6");
            break;
        }
    }
    printf("4");
    sleep(1);
    /* Закрытие именованного канала */
    close(fd);

    return 0;
}