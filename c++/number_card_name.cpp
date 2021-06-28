#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve() {
	int n, m;
	cin >> n >> m;
	vector<vector<int>>cards(n, vector<int>(m));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> cards[i][j];
	for (int i = 0; i < n; i++)
		sort(cards[i].begin(), cards[i].end());
	int ret = -1;
	for (int i = 0; i < n; i++)
		if (ret < cards[i][0])
			ret = cards[i][0];
	cout << ret << "\n";
}

int main() {
	solve();
}