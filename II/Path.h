#ifndef PATH_H
#define PATH_H

#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Path {
private:
    vector<int> path;                   // путь
    int length;                         // длина пути

public:
    Path(int start);
    Path& operator= (const Path& p);
    vector<int> Get_path() const;       // путь
    int Get_length() const;             // длина пути
    void push_back(int v, int l);       // добавление вершины в конец
    void push_back(Path p);             // добавление пути в конец

};

ostream& operator<<(ostream& os, const Path& p);

#endif