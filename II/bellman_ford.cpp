#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// Структура для представления ребра
struct Edge {
    int src, dest, weight;
};

// Структура для представления графа
struct Graph {
    int V, E;
    vector<Edge> edges;
};

// Функция для выполнения алгоритма Беллмана-Форда
void BellmanFord(Graph graph, int src) {
    int V = graph.V;
    int E = graph.E;
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;

    // Шаг 2: Выполняем алгоритм
    for (int i = 1; i <= V - 1; i++) {
        for (int j = 0; j < E; j++) {
            int u = graph.edges[j].src;
            int v = graph.edges[j].dest;
            int weight = graph.edges[j].weight;
            if (dist[u] != INT_MAX && dist[u] + weight < dist[v])
                dist[v] = dist[u] + weight;
        }
    }

    // Шаг 3: Проверяем наличие отрицательного цикла
    for (int i = 0; i < E; i++) {
        int u = graph.edges[i].src;
        int v = graph.edges[i].dest;
        int weight = graph.edges[i].weight;
        if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
            cout << "Граф содержит отрицательный цикл\n";
            return;
        }
    }

    // Выводим кратчайшие расстояния
    cout << "Кратчайшие расстояния от источника до всех вершин:\n";
    for (int i = 0; i < V; ++i)
        cout << i << "\t\t" << dist[i] << "\n";
}

int main() {
    // Создаем граф
    Graph graph;
    graph.V = 5; // Количество вершин
    graph.E = 7; // Количество ребер
    graph.edges.push_back({0, 1, -1});
    graph.edges.push_back({0, 2, 4});
    graph.edges.push_back({1, 2, 3});
    graph.edges.push_back({1, 3, 2});
    graph.edges.push_back({1, 4, 2});
    graph.edges.push_back({3, 2, 5});
    graph.edges.push_back({4, 3, -3});

    BellmanFord(graph, 0);

    return 0;
}