#include <fstream>
#include <sstream>
#include <iostream>

int main()
{
    std::string file_name{"testfile.txt"};
    std::ostringstream buffer_file;
    std::ifstream file(file_name);
    buffer_file << file.rdbuf();
    std::cout << buffer_file.str() << "\n";
}