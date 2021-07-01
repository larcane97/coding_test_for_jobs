#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct disjoint {
	vector<int>parent, rank;
	disjoint(int n) :rank(n+1, 1),parent(n+1) {
		for (int i = 1; i <= n; i++)
			parent[i] = i;
	}
	
	int find(int u) {
		if (parent[u] != u)
			parent[u] = find(parent[u]);
		return parent[u];
	}
	bool merge(int u, int v) {
		u = find(u), v = find(v);
		if (u == v)return false;
		if (rank[u] > rank[v]) swap(u, v);
		parent[v] = u;
		if (rank[u] == rank[v])
			rank[u]++;
		return true;
	}
};


void kruskal() {
	int v, e;
	cin >> v >> e;
	disjoint ds(v);
	vector<pair<int, pair<int, int>>>edges;
	int ret = 0;
	for (int i = 0; i < e; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		edges.push_back({ c,{a,b} });
	}
	sort(edges.begin(), edges.end());
	for (int i = 0; i < edges.size(); i++) {
		int a = edges[i].second.first;
		int b = edges[i].second.second;
		int c = edges[i].first;
		if (ds.merge(a, b))
			ret += c;
	}
	cout << ret << "\n";
}


int main() {
	kruskal();
}