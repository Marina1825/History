#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <fstream>

#define BUFFER_SIZE 1024

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <server_ip> <server_port>" << std::endl;
        return 1;
    }

    int client_socket;
    struct sockaddr_in server_addr;
    socklen_t addr_size;
    char buffer[BUFFER_SIZE];
    char ack_buffer[4];

    // Создаем сокет
    client_socket = socket(AF_INET, SOCK_DGRAM, 0);
    if (client_socket < 0) {
        std::cerr << "Error in socket creation" << std::endl;
        return 1;
    }

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(atoi(argv[2]));
    server_addr.sin_addr.s_addr = inet_addr(argv[1]);

    // Получаем IP адрес клиента
    struct sockaddr_in client_addr;
    socklen_t client_addr_len = sizeof(client_addr);
    getsockname(client_socket, (struct sockaddr *)&client_addr, &client_addr_len);
    char client_ip[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &(client_addr.sin_addr), client_ip, INET_ADDRSTRLEN);

    // Отправляем IP адрес клиента
    sendto(client_socket, client_ip, strlen(client_ip), 0, (struct sockaddr *)&server_addr, sizeof(server_addr));

    std::cout << "Enter 'text' for message or 'file' for file transfer: ";
    std::string choice;
    std::getline(std::cin, choice);

    if (choice == "text") {
        std::cout << "Enter message to send: ";
        std::cin.getline(buffer, BUFFER_SIZE);
        // Отправляем сообщение по 8 символов
        for (size_t i = 0; i < strlen(buffer); i += 8) {
            sendto(client_socket, buffer + i, std::min(8, (int)strlen(buffer) - i), 0, (struct sockaddr *)&server_addr, sizeof(server_addr));
        }
        
    } else if (choice == "file") {
        std::cout << "Enter filename: ";
        std::string filename;
        std::getline(std::cin, filename);

        std::ifstream file(filename, std::ios::binary);
        if (!file.is_open()) {
            std::cerr << "Cannot open file: " << filename << std::endl;
            close(client_socket);
            return 1;
        }

        while (!file.eof()) {
            file.read(buffer, BUFFER_SIZE);
            size_t bytes_read = file.gcount();
            if (bytes_read > 0) {
                // Отправляем файл по 8 символов
                for (size_t i = 0; i < bytes_read; i += 8) {
                    sendto(client_socket, buffer + i, std::min(8, (int)bytes_read - i), 0, (struct sockaddr *)&server_addr, sizeof(server_addr));
                }
            }
        }
        sendto(client_socket, buffer + i, std::min(8, (int)bytes_read - i), 0, (struct sockaddr *)&server_addr, sizeof(server_addr));
    } else {
        std::cerr << "Invalid option. Use 'text' or 'file'." << std::endl;
        close(client_socket);
        return 1;
    }

    // Получаем подтверждение
    addr_size = sizeof(server_addr);
    int recv_len = recvfrom(client_socket, ack_buffer, sizeof(ack_buffer), 0, (struct sockaddr *)&server_addr, &addr_size);
    if (recv_len > 0) {
        ack_buffer[recv_len] = '\0';  // Завершаем строку нулем
        std::cout << "Received ACK from server: " << ack_buffer << std::endl;
    }

    close(client_socket);
    return 0;
}