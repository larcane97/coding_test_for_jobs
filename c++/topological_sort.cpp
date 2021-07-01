#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int>adj[501];
void topological_sort() {
	int v, e;
	cin >> v >> e;
	vector<int>indegree(v + 1, 0);
	for (int i = 0; i < e; i++) {
		int a, b;
		cin >> a >> b;
		adj[a].push_back(b);
		indegree[b]++;
	}
	queue<int>q;
	vector<int>route;
	for (int i = 1; i <= v; i++)
		if (indegree[i] == 0)
			q.push(i);

	while (!q.empty()) {
		int here = q.front();
		q.pop();
		route.push_back(here);
		for (int i = 0; i < adj[here].size(); i++) {
			int there = adj[here][i];
			indegree[there]--;
			if (indegree[there] == 0)
				q.push(there);
		}
	}
	for (int i = 0; i < route.size(); i++)
		cout << route[i] << " ";
}

int main() {
	topological_sort();
}