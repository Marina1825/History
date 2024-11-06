#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

int main()
{
    std::string line;
    std::string needle;
    std::ifstream file("Spravka.dat");
    if(!file)
    {
        std::cout << "Ошибка: не удалось получить доступ к файлу.";
        std::cout << "Автор программы: Буянова Марина." << std::endl << "Группа: ИА-132." << std::endl;
        return 0;
    }
        std::cout << "Какой пункт вас интересует:" << std::endl;
        std::cin >> needle;
    
        while(std::getline(file, line))
        {
            if(line.find(needle) != std::string::npos)
            {
                std::cout << "Найденые рейсы: " << std::endl << line << std::endl;
            }
            else 
            {
                std::cout << "Такого пункта нет." << std::endl;
                break;
            }
        }
        file.close();
    std::cout << "Автор программы: Буянова Марина." << std::endl << "Группа: ИА-132." << std::endl;
    return 0;
}
//открытие файла