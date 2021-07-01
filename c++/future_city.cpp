#include <iostream>
#include <vector>
using namespace std;

const int INF = 987654321;
int adj[101][101];
int n, m;
void solve() {
	cin >> n >> m;
	for(int i=1;i<=n;i++)
		for (int j = 1; j <= n; j++) {
			if (i == j)continue;
			adj[i][j] = INF;
		}
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		adj[a][b] = 1;
		adj[b][a] = 1;
	}
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);
	int x, k;
	cin >> x >> k;
	int ret = adj[1][k] + adj[k][x];
	if (ret >= INF)
		cout << -1 << "\n";
	else
		cout << ret << "\n";
}

int main() {
	solve();
}