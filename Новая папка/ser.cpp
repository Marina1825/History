#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <cstring>
#include <unistd.h>
#include <fstream>
#include <unordered_map>
#include <sstream>

#define BUFFER_SIZE 1024

int main() {
    int server_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_size;
    char buffer[BUFFER_SIZE] = {0};
    std::unordered_map<int, int> packet_loss;
    int packet_count = 0;
    char IP_buffer[BUFFER_SIZE] = {0};
    char form_buffer[BUFFER_SIZE] = {0};

    //Симуляция потери пакетов
    //packet_loss[2] = 1; // Потерять пакет с номером 2 один раз
    //packet_loss[5] = 2; // Потерять пакет с номером 5 два раза

    // Создаем сокет
    server_socket = socket(AF_INET, SOCK_DGRAM, 0);
    if (server_socket < 0) {
        std::cerr << "Error in socket creation" << std::endl;
        return 1;
    }

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = 0; // Задаем 0 для автоматического выбора порта
    server_addr.sin_addr.s_addr = INADDR_ANY;

    // Привязываем сокет
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        std::cerr << "Bind failed" << std::endl;
        return 1;
    }

    // Получаем присвоенный порт
    addr_size = sizeof(server_addr);
    getsockname(server_socket, (struct sockaddr *)&server_addr, &addr_size);
    std::cout << "Server is running on port " << ntohs(server_addr.sin_port) << std::endl;

    while (true) {
        addr_size = sizeof(client_addr);
        int IP_len = recvfrom(server_socket, IP_buffer, BUFFER_SIZE, 0, (struct sockaddr *)&client_addr, &addr_size);
        int form_len = recvfrom(server_socket, form_buffer, BUFFER_SIZE, 0, (struct sockaddr *)&client_addr, &addr_size);
        int recv_len = recvfrom(server_socket, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&client_addr, &addr_size);
        if (recv_len > 0) {
            buffer[recv_len] = '\0';
            packet_count++;

            if (packet_loss.find(packet_count) != packet_loss.end() && packet_loss[packet_count] > 0) {
                std::cout << "Packet " << packet_count << " lost" << std::endl;
                packet_loss[packet_count]--;
                continue; // Пропускаем обработку и отправку ACK для симуляции потери
            }

            std::cout << "IP: " << IP_buffer << " (Packet " << packet_count << ")" << std::endl;
            std::cout << "form: " << form_buffer << " (Packet " << packet_count << ")" << std::endl;
            std::string form = form_buffer;
            
            if (form == "text") {
                std::cout << "Received: \n" << buffer << " (Packet " << packet_count << ")\n\n" << std::endl;
            } else if(form == "file") {
                std::string file_name = buffer;
                std::cout << "FILE NAME " << file_name << '\n';
                std::ifstream file(file_name);
                std::ostringstream buffer_file;
                buffer_file << file.rdbuf();
                if (!file.is_open()) {
                    std::cerr << "Cannot open file: " << file_name << std::endl;
                    //return 1;
                }
                std::cout << "Text file:" << '\n';
                std::cout << buffer_file.str() << '\n';
                file.close();
            }
        // Отправляем подтверждение
        sendto(server_socket, "ACK", strlen("ACK"), 0, (struct sockaddr *)&client_addr, addr_size);   
        }
    }

    close(server_socket);
    return 0;
}
