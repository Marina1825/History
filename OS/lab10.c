#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>

#define BUFFER_SIZE 1024

int main() {
    int fd[2];
    pid_t pid;
    char buf[BUFFER_SIZE];
    int file_descriptor;
    int open_brackets = 0, close_brackets = 0;

    if (pipe(fd) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    pid = fork();

    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0) {
        // Дочерний процесс
        close(fd[1]); // Закрываем неиспользуемую конец канала
        read(fd[0], buf, BUFFER_SIZE);
        close(fd[0]); // Закрываем конец канала

        for (int i = 0; buf[i] != '\0'; i++) {
            if (buf[i] == '(') {
                open_brackets++;
            } else if (buf[i] == ')') {
                close_brackets++;
            }
        }

        if (open_brackets == close_brackets) {
            printf("Баланс скобок соблюдается.\n");
        } else {
            printf("Баланс скобок не соблюдается. Открывающих скобок: %d, закрывающих: %d\n", open_brackets, close_brackets);
        }
        

        exit(EXIT_SUCCESS);
    } else {
        // Родительский процесс
        close(fd[0]); // Закрываем неиспользуемую конец канала
        file_descriptor = open("/home/marina/STUDENT/ADMIN/FILE4.TEXT" , O_RDONLY);
        if (file_descriptor == -1) {
            perror("open");
            exit(EXIT_FAILURE);
        }
        read(file_descriptor, buf, BUFFER_SIZE);
        write(fd[1], buf, BUFFER_SIZE);
        close(fd[1]); // Закрываем конец канала
        close(file_descriptor); // Закрываем файловый дескриптор
        wait(NULL); // Ожидаем завершения дочернего процесса
        exit(EXIT_SUCCESS);
    }

    return 0;
}