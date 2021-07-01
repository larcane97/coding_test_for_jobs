#include <queue>
#include <vector>
#include <iostream>
using namespace std;

const int INF = 987654321;
vector<pair<int, int>>adj[30001];
void solve() {
	int n, m, start;
	cin >> n >> m >> start;
	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		adj[a].push_back({ b,c });
	}
	vector<int>distance(n+1, INF);
	priority_queue<pair<int, int>>pq;
	pq.push({ 0,start });
	distance[start] = 0;
	while (!pq.empty()) {
		int here = pq.top().second;
		int dist = -pq.top().first;
		pq.pop();
		if (distance[here] < dist)continue;
		for (int i= 0; i< adj[here].size(); i++) {
			int there = adj[here][i].first;
			int cost = adj[here][i].second;
			if (cost + dist < distance[there]) {
				distance[there] = cost + dist;
				pq.push({ -distance[there],there });
			}
		}
	}
	int num = 0;
	int time = 0;
	for (int i = 1; i <= n; i++) {
		if (distance[i] < INF && i != start) {
			num++;
			time = max(time, distance[i]);
		}
	}
	cout << num << " " << time << "\n";

}

int main() {
	solve();
}