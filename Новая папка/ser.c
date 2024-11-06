#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define BUFFER_SIZE 1024

int main() {
    int server_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_size;
    char buffer[BUFFER_SIZE];

    // Создаем UDP сокет
    server_socket = socket(AF_INET, SOCK_DGRAM, 0);
    if (server_socket < 0) {
        perror("Error in socket creation");
        return 1;
    }

    // Настройка структуры адреса сервера
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(12345); // Порт для прослушивания
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);

    // Привязываем сокет
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        return 1;
    }

    printf("Server is listening on port 12345\n");

    // Прием данных
    while (1) {
        addr_size = sizeof(client_addr);
        int recv_len = recvfrom(server_socket, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&client_addr, &addr_size);
        if (recv_len > 0) {
            buffer[recv_len] = '\0'; // Null-terminate the string
            printf("Received: %s\n", buffer);

            // Отправляем подтверждение
            sendto(server_socket, "ACK", strlen("ACK"), 0, (struct sockaddr *)&client_addr, addr_size);
        }
    }

    close(server_socket);
    return 0;
}
