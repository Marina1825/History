#include "Solution.h"

Solution::Solution(const Graph& g) {
    graph = g;
}

// алгоритм Дейкстры
Path* Solution::Dijkstra(int v, Path* data) {
    data = (Path*)calloc(graph.Get_n(), sizeof(Path));      //пути от вершины v до других вершин графа
    int distaces[graph.Get_n()];                            //минимальное расстояние от вершины v до других
    int out[graph.Get_n()];                                 //посещенные вершины
    for (int i = 0; i < graph.Get_n(); ++i) {
        if (i == v) {
            distaces[i] = 0;
            data[i] = Path(v);
        } else {
            distaces[i] = numeric_limits<int>::max();
        }
        out[i] = 0;
    }

    int min = numeric_limits<int>::max(), index = -1;
    do {
        min = numeric_limits<int>::max();
        for (int i = 0; i < graph.Get_n(); ++i) {
            if ((out[i] == 0) && (distaces[i] < min)) {
                min = distaces[i];
                index = i;
            }
        }
        if (min != numeric_limits<int>::max()) {
            for (int i = 0; i < graph.Get_n(); ++i) {
                if (graph.Get_data()[index][i] > 0) {
                    int temp = min + graph.Get_data()[index][i];
                    if (temp < distaces[i]) {
                        distaces[i] = temp;
                        data[i] = data[index];
                        data[i].push_back(i, graph.Get_data()[index][i]);
                    }
                }
            }
            out[index] = 1;
        }
    } while (min < numeric_limits<int>::max());

    return data;
}

// вычисление оптимального пути
Path Solution::calc(vector<int> v, int start) {
    map<int, Path*> distaces;
    Path* temp = (Path*)calloc(graph.Get_n(), sizeof(Path));
    temp = Dijkstra(start, temp);
    distaces[start] = temp;
    for (size_t i = 0; i < v.size(); ++i) {
        temp = Dijkstra(v[i], temp);
        distaces[v[i]] = temp;
    }

    Path p = Path(start);
    sort(v.begin(), v.end());
    for (size_t i = 0; i < v.size(); ++i) {
        int last = p.Get_path()[p.Get_path().size() - 1];
        p.push_back(distaces[last][v[i]]);
    }
    int last = p.Get_path()[p.Get_path().size() - 1];
    p.push_back(distaces[last][start]);
    next_permutation(v.begin(), v.end());

    do {
        Path temp = Path(start);
        for (size_t i = 0; i < v.size(); ++i) {
            int last = temp.Get_path()[temp.Get_path().size() - 1];
            temp.push_back(distaces[last][v[i]]);
            if (temp.Get_length() > p.Get_length())
                break;
        }
        int last = temp.Get_path()[temp.Get_path().size() - 1];
        temp.push_back(distaces[last][start]);

        if (temp.Get_length() < p.Get_length()) {
            p = temp;
        }
    } while (next_permutation(v.begin(), v.end()));

    return p;
}