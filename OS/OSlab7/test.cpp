#include <iostream>
#include <fstream>
#include <string>

struct Worker {
    std::string name;
    float salary;
};

int main() {
    std::ifstream file("Work.dat", std::ios::binary); // Открытие файла в бинарном режиме
    if (file.is_open()) {
        Worker workers[6];
        // Проверка, что файл не пустой
        file.seekg(0, std::ios::end);
        std::streampos fileSize = file.tellg();
        if (fileSize < static_cast<std::streampos>(sizeof(workers))) {
            std::cerr << "Файл Work.dat слишком мал для чтения данных." << std::endl;
            return 1;
        }
        file.seekg(0, std::ios::beg);

        file.read(reinterpret_cast<char*>(workers), sizeof(workers));

        Worker highestPaid = workers[0];
        for (int i = 1; i < 6; ++i) {
            if (workers[i].salary > highestPaid.salary) {
                highestPaid = workers[i];
            }
        }
        std::cout << "Работник с наибольшей зарплатой: " << highestPaid.name << " (зарплата: " << highestPaid.salary << ")" << std::endl;
        file.close();
    } else {
        std::cerr << "Ошибка при открытии файла Work.dat." << std::endl;
    }
    return 0;
}