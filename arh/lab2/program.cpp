#include <iostream>
#include <fstream>
#include <signal.h>

void handler(int sign){
    exit (0);
}

int main(int argc, char** argv) {
    signal (2, handler);
    if (argc < 2) {
        std::cout << "Usage: program_name <file_path>" << std::endl;
        return 1;
    }

    std::string file_path = argv[1];

    std::ifstream file(file_path);

    if (!file.is_open()) {
        std::cout << "Failed to open file: " << file_path << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }
    int i = 0;
    while (i != 1) {
        
    }

    return 0;
}