#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <cstring>
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
    char buffer[BUFFER_SIZE] = {0};
    char ack_buffer[4];
    char IP_buffer[BUFFER_SIZE] = {0};

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

    strncpy(IP_buffer, argv[1], sizeof(IP_buffer) - 1);
    IP_buffer[sizeof(IP_buffer) - 1] = '\0';

    sendto(client_socket, IP_buffer, strlen(IP_buffer), 0, (struct sockaddr *)&server_addr, sizeof(server_addr));

    std::cout << "Enter 'text' for message or 'file' for file transfer: ";
    std::string choice;
    std::getline(std::cin, choice);

    const char* choice_cstr = choice.c_str();
    //std::cout << choice_cstr << std::endl;
    sendto(client_socket, choice_cstr, strlen(choice_cstr), 0, (struct sockaddr *)&server_addr, sizeof(server_addr));

    if (choice == "text") {
        std::cout << "Enter message to send: ";
        std::cin.getline(buffer, BUFFER_SIZE);
        sendto(client_socket, buffer, strlen(buffer), 0, (struct sockaddr *)&server_addr, sizeof(server_addr));

    } else if (choice == "file") {
        std::cout << "Enter filename: ";
        std::cin.getline(buffer, BUFFER_SIZE);
        sendto(client_socket, buffer, strlen(buffer), 0, (struct sockaddr *)&server_addr, sizeof(server_addr));
    
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
