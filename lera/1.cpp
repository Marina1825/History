#include <fstream>
#include <iostream>

struct Worker {
    char name[50];
    double salary;
};

int main() {
    Worker workers[6] = {
        {"Денис Бобенко", 2500.0},
        {"Кларк Кент", 3500.0},
        {"Никита Путеев", 2700.0},
        {"Артем Савенко", 2800.0},
        {"Кирилл Клачков", 2900.0},
        {"Диана Корчева", 3200.0}
    };

    std::ofstream file("Work.dat");

    if (!file) {
        std::cerr << "Ошибка: не удалось откртыть файл" << std::endl;
        return 1;
    }

    try {
        file.write(reinterpret_cast<char*>(workers), sizeof(workers));
    } 
    catch (const std::exception& e) {
        std::cerr << "Ошибка с записью файла: " << e.what() << std::endl;
        return 1;
    }

    file.close();

    std::cout << "Автор: Худеева Валерия\nГруппа: ИА-132" << std::endl;

    return 0;
}