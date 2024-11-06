#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int sockfd;
    struct sockaddr_in servaddr;

    // Создание сокета
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        std::cerr << "Ошибка при создании сокета" << std::endl;
        return -1;
    }

    memset(&servaddr, 0, sizeof(servaddr));

    // Заполнение информации о сервере
    servaddr.sin_family = AF_INET; // IPv4
    servaddr.sin_port = htons(68); // порт сервера DHCP
    servaddr.sin_addr.s_addr = inet_addr("192.168.1.1"); // IP-адрес сервере DHCP

    // Проверка IP-адреса
    if (servaddr.sin_addr.s_addr == INADDR_NONE) {
        std::cerr << "Неверный IP-адрес сервера DHCP" << std::endl;
        close(sockfd);
        return -1;
    }

    // Буфер для хранения данных
    char buffer[1024] = "DHCPREQUEST";

    // Отправка запроса серверу
    ssize_t bytes_sent = sendto(sockfd, buffer, strlen(buffer), MSG_CONFIRM, (const struct sockaddr *) &servaddr, sizeof(servaddr));
    if (bytes_sent < 0) {
        std::cerr << "Ошибка при отправке запроса" << std::endl;
        close(sockfd);
        return -1;
    }

    // Закрытие сокета
    close(sockfd);

    return 0;
}