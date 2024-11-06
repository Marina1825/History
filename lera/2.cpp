#include <fstream>
#include <iostream>

struct Worker {
    char name[50];
    double salary;
};

int main() {
    Worker workers[6];

    std::ifstream file("Work.dat");

    if (!file) {
        std::cerr << "Ошибка: не удалось открыть файл" << std::endl;
        return 1;
    }

    try {
        file.read(reinterpret_cast<char*>(workers), sizeof(workers));
    } catch (const std::exception& e) {
        std::cerr << "Ошибка с чтением файла: " << e.what() << std::endl;
        return 1;
    }

    file.close();

    double max_salary = workers[0].salary;
    int max_index = 0;

    for (int i = 1; i < 6; ++i) {
        if (workers[i].salary > max_salary) {
            max_salary = workers[i].salary;
            max_index = i;
        }
    }

    std::cout << "Работник с самой высокой зарплатой: " << workers[max_index].name << std::endl;

    std::cout << "Автор: Худеева Валерия\nГруппа: ИА-132" << std::endl;

    return 0;
}