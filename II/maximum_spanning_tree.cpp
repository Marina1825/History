#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

struct Edge {
    int to, weight;
    Edge(int to, int weight) : to(to), weight(weight) {}
};

struct Node {
    int vertex, key;
    Node(int vertex, int key) : vertex(vertex), key(key) {}
};

bool operator<(const Node& a, const Node& b) {
    return a.key > b.key;
}

void prim(vector<vector<Edge>>& graph, int start) {
    int n = graph.size();
    vector<int> key(n, INF);
    vector<int> parent(n, -1);
    vector<bool> inMST(n, false);
    priority_queue<Node> pq;

    key[start] = 0;
    pq.push(Node(start, 0));

    while (!pq.empty()) {
        int u = pq.top().vertex;
        pq.pop();

        inMST[u] = true;

        for (Edge& edge : graph[u]) {
            int v = edge.to;
            int weight = edge.weight;

            if (!inMST[v] && key[v] > weight) {
                key[v] = weight;
                pq.push(Node(v, key[v]));
                parent[v] = u;
            }
        }
    }

    // Вывод результата
    for (int i = 1; i < n; ++i) {
        cout << parent[i] << " - " << i << endl;
    }
}

int main() {
    int n = 9; // Количество вершин
    vector<vector<Edge>> graph(n);

    // Добавление ребер
    graph[0].push_back(Edge(1, 4));
    graph[0].push_back(Edge(7, 8));
    graph[1].push_back(Edge(0, 4));
    graph[1].push_back(Edge(2, 8));
    graph[1].push_back(Edge(7, 11));
    graph[2].push_back(Edge(1, 8));
    graph[2].push_back(Edge(3, 7));
    graph[2].push_back(Edge(8, 2));
    graph[2].push_back(Edge(5, 4));
    graph[3].push_back(Edge(2, 7));
    graph[3].push_back(Edge(4, 9));
    graph[3].push_back(Edge(5, 14));
    graph[4].push_back(Edge(3, 9));
    graph[4].push_back(Edge(5, 10));
    graph[5].push_back(Edge(2, 4));
    graph[5].push_back(Edge(3, 14));
    graph[5].push_back(Edge(4, 10));
    graph[5].push_back(Edge(6, 2));
    graph[6].push_back(Edge(5, 2));
    graph[6].push_back(Edge(7, 1));
    graph[6].push_back(Edge(8, 6));
    graph[7].push_back(Edge(0, 8));
    graph[7].push_back(Edge(1, 11));
    graph[7].push_back(Edge(6, 1));
    graph[7].push_back(Edge(8, 7));
    graph[8].push_back(Edge(2, 2));
    graph[8].push_back(Edge(6, 6));
    graph[8].push_back(Edge(7, 7));

    prim(graph, 0);

    return 0;
}