#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <ctype.h>

#define READ_END 0
#define WRITE_END 1
#define MAX_BUF 1024

int main() {
    int fd[2];
    pid_t pid;
    char buffer[MAX_BUF];
    int nbytes;

    // Создание программного канала
    if (pipe(fd) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    // Генерация дочернего процесса
    pid = fork();
    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    // Основной процесс
    if (pid > 0) {

        // Открытие файла для чтения
        int file = open("input.txt", O_RDONLY);
        if (file == -1) {
            perror("open");
            exit(EXIT_FAILURE);
        }

        // Чтение файла и запись в канал
        while ((nbytes = read(file, buffer, MAX_BUF)) > 0) {
            write(fd[WRITE_END], buffer, nbytes);
        }

        // Закрытие файла и канала
        close(file);
        close(fd[WRITE_END]);
    }
    // Дочерний процесс
    else {
        close(fd[WRITE_END]);

        // Открытие файла для записи
        int file = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
        if (file == -1) {
            perror("open");
            exit(EXIT_FAILURE);
        }

        // Чтение из канала и запись в файл
        while ((nbytes = read(fd[READ_END], buffer, MAX_BUF)) > 0) {
            for (int i = 0; i < nbytes; i++) {
                if (buffer[i] == ' ') {
                    buffer[i] = '.';
                    buffer[i + 1] = toupper(buffer[i+1]);
                }
            }
            write(file, buffer, nbytes);
        }

        // Закрытие файла и канала
        close(file);
        close(fd[READ_END]);
    }

    return 0;
}