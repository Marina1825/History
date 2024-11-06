#include <asio.h>
#include <iostream>
#include <vector>
#include <cstring>
#include <cstdint>

using asio::ip::udp;

class DHCPServer {
private:
    asio::io_context io_context;
    udp::socket socket_;
    udp::endpoint remote_endpoint_;
    std::vector<char> recv_buffer_;

public:
    DHCPServer(short port)
        : socket_(io_context, udp::endpoint(udp::v4(), port)) {
        recv_buffer_.resize(1024);  // Enough for basic DHCP messages
    }

    void start() {
        send_discover();  // Initiate DHCP client functionality
        do_receive();     // Start server to listen for incoming DHCP messages
        io_context.run();
    }

private:
    void do_receive() {
        socket_.async_receive_from(
            asio::buffer(recv_buffer_), remote_endpoint_,
            [this](std::error_code ec, std::size_t bytes_recvd) {
                if (!ec && bytes_recvd > 0) {
                    handle_request(bytes_recvd);
                    do_receive();
                }
            });
    }

    void handle_request(std::size_t length) {
        std::cout << "Received " << length << " bytes\n";
        if (is_discover_message(recv_buffer_, length)) {
            send_offer();
        } else if (is_offer_message(recv_buffer_, length)) {
            std::cout << "Received DHCPOFFER\n";
            send_request();  // После получения предложения отправляем запрос
        } else if (is_ack_message(recv_buffer_, length)) {
            std::cout << "Received DHCPACK\n";
            // Конфигурация успешно завершена
        }
    }

    bool is_discover_message(const std::vector<char>& buffer, std::size_t length) {
        return length >= 240 && buffer[0] == 0x01 && buffer[242] == 0x35 && buffer[243] == 0x01 && buffer[244] == 0x01;
    }

    bool is_offer_message(const std::vector<char>& buffer, std::size_t length) {
        return length >= 240 && buffer[0] == 0x02 && buffer[242] == 0x35 && buffer[243] == 0x01 && buffer[244] == 0x02;
    }

    bool is_ack_message(const std::vector<char>& buffer, std::size_t length) {
        return length >= 240 && buffer[0] == 0x02 && buffer[242] == 0x35 && buffer[243] == 0x01 && buffer[244] == 0x05;
    }

    void send_discover() {
        std::vector<char> discover(300, 0);
        discover[0] = 0x01;  // BOOTREQUEST
        discover[242] = 0x35;  // Option: DHCP Message Type
        discover[243] = 0x01;  // Length
        discover[244] = 0x01;  // Type: DHCPDISCOVER

        // Broadcast endpoint
        udp::endpoint broadcast_endpoint(asio::ip::address_v4::broadcast(), 67);
        socket_.set_option(udp::socket::reuse_address(true));
        socket_.set_option(asio::socket_base::broadcast(true));

        socket_.async_send_to(asio::buffer(discover), broadcast_endpoint,
            [this](std::error_code /*ec*/, std::size_t /*bytes_sent*/) {
                std::cout << "DHCPDISCOVER sent\n";
            });
    }

    void send_offer() {
        std::vector<char> offer(300, 0);
        offer[0] = 0x02; // BOOTREPLY
        offer[242] = 0x35; // Option: DHCP Message Type
        offer[243] = 0x01; // Length
        offer[244] = 0x02; // Type: DHCPOFFER

        // Example IP address
        offer[16] = 192; offer[17] = 168; offer[18] = 1; offer[19] = 100;

        // Subnet Mask
        offer[245] = 1;   // Option number for subnet mask
        offer[246] = 4;   // Length
        offer[247] = 255; offer[248] = 255; offer[249] = 255; offer[250] = 0;

        // Router IP address
        offer[251] = 3;   // Option number for router
        offer[252] = 4;   // Length
        offer[253] = 192; offer[254] = 168; offer[255] = 1; offer[256] = 1;

        // End option
        offer[257] = 255;

        socket_.async_send_to(asio::buffer(offer), remote_endpoint_,
            [this](std::error_code /*ec*/, std::size_t /*bytes_sent*/) {
                std::cout << "DHCPOFFER sent\n";
            });
    }

    void send_request() {
        std::vector<char> request(300, 0);
