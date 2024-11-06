#include "myheader.h"

void print_env_vars(int option) {
    int i;
    for (i = 0; i < 10; i++) {
        if (option == '1') {
            printf("%s\n", environ[i]);
        } else if (option == '2') {
            char *env_var = strtok(environ[i], "=");
            char *value = strtok(NULL, "=");
            printf("%s: %s\n", env_var, value);
        }
    }
}

void process_file(char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Ошибка: не удалось открыть файл %s\n", filename);
        return;
    }

    char c;
    while ((c = fgetc(file)) != EOF) {
        putchar(c);
    }

    if (ferror(file)) {
        fprintf(stderr, "Ошибка: не удалось прочитать файл %s\n", filename);
    }

    if (fclose(file) == EOF) {
        fprintf(stderr, "Ошибка: не удалось закрыть файл %s\n", filename);
    }
}

int main(int argc, char *argv[]) {
    int option = 0;
    char *filename = NULL;
    int c;

    while ((c = getopt(argc, argv, "12f:")) != -1) {
        switch (c) {
            case '1':
            case '2':
                option = c;
                break;
            case 'f':
                filename = optarg;
                break;
            default:
                fprintf(stderr, "Usage: %s [-1|-2] [-f filename]\n", argv[0]);
                return 1;
        }
    }

    print_env_vars(option);

    if (filename != NULL) {
        process_file(filename);
    }

    printf("\nАвтор программы: Буянова Марина.\nГруппа: ИА-132.\n");

    return 0;
}