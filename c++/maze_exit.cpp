#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m;
string board[200];
bool visited[200][200];
int dir[4][2] = {
	{0,1},
	{1,0},
	{-1,0},
	{0,-1}
};

bool inRange(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < m;
}

void solve() {
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> board[i];
	queue<pair<pair<int, int>, int>>q;
	q.push({ {0,0},1 });
	visited[0][0] = true;
	while (!q.empty()) {
		int x = q.front().first.first;
		int y = q.front().first.second;
		int dis = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int dx = x + dir[i][0];
			int dy = y + dir[i][1];
			if (dx == n - 1 && dy == m - 1) {
				cout << dis+1 << "\n";
				return;
			}
			if (inRange(dx, dy) && board[dx][dy] == '1' && !visited[dx][dy]) {
				visited[dx][dy] = true;
				q.push({ { dx,dy },dis + 1 });
			}
		}
	}

}

int main() {
	solve();
}