/*В соответствии с вариантом задания разработать две программы: программу создания и 
программу обработки бинарного файла. Также необходимо обработать ошибки, которые могут 
возникнуть при открытии, закрытии и выводе файла на экран.
При завершении программы (даже в случае возникновения ошибок) на экран должно быть 
выдано сообщение об авторе программы, учетное имя, группа.*/
/*1.Создать файл Spravka.dat, содержащий 10 записей следующей структуры: название 
начального пункта маршрута; название конечного пункта маршрута; номер маршрута; 
2.Написать программу, выполняющую следующую обработку файла Spravka.dat:
 поиск в файле данных о маршрутах, которые начинаются или заканчиваются в 
пункте, название которого вводится с клавиатуры;
 если таких маршрутов нет, выдать соответствующее сообщение на дисплей.
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

struct Route {
    std::string start; //название начального пункта маршрута
    std::string end; //название конечного пункта маршрута
    int number; //номер маршрута
};

int main()
{
    std::ofstream file("Spravka.dat");
    Route routes[10];
    routes[0] = {"Москва", "Санкт-Петербург", 1};
    routes[1] = {"Санкт-Петербург", "Москва", 2};
    routes[2] = {"Киев", "Шир", 3};
    routes[3] = {"Минск", "Киев", 4};
    routes[4] = {"Лондон", "Париж", 5};
    routes[5] = {"Париж", "Лондон", 6};
    routes[6] = {"Токио", "Осака", 7};
    routes[7] = {"Осака", "Токио", 8};
    routes[8] = {"Нью-Йорк", "Лос-Анджелес", 9};
    routes[9] = {"Лос-Анджелес", "Нью-Йорк", 10};
    if (file.is_open())
    {
        for (const Route& route: routes)
        {
            file << route.start << ", "<< route.end << ", " << route.number << std::endl;
        }
        for (const Route& route: routes)
        file.close();
        std::cout << "Автор программы: Буянова Марина." << std::endl << "Группа: ИА-132." << std::endl;
        std::cout << "YES" << '\n';
    }
    return 0;
}