#include <iostream>
#include <vector>
using namespace std;

struct disjoint {
	vector<int>parent, rank;
	disjoint(int n) :parent(n+1), rank(n+1, 1) {
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
		if (rank[u] > rank[v])swap(u, v);
		parent[v] = u;
		if (rank[u] == rank[v])
			rank[u]++;
		return true;
	}
};

void solve() {
	int v, e;
	cin >> v >> e;
	disjoint ds(v);
	for (int i = 0; i < e; i++) {
		int a, u, v;
		cin >> a >> u >> v;
		if (a == 0)
			ds.merge(u, v);
		else {
			if (ds.find(u) == ds.find(v))
				cout << "YES" << "\n";
			else
				cout << "NO" << "\n";
		}
	}
}

int main() {
	solve();
}