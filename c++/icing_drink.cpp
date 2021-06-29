#include <iostream>
#include <vector>
using namespace std;

string board[1000];
bool visited[1000][1000];
int n, m;
int dir[4][2] = {
	{0,1},
	{1,0},
	{-1,0},
	{0,-1}
};

bool inRange(int x, int y) {
	return x >= 0 && x < n&& y >= 0 && y < m;
}
void DFS(int x,int y) {
	visited[x][y] = true;
	for (int i = 0; i < 4; i++) {
		int dx = x + dir[i][0];
		int dy = y + dir[i][1];
		if (inRange(dx, dy) && !visited[dx][dy] && board[dx][dy]=='0')
			DFS(dx, dy);
	}
}



void solve_by_DFS() {
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> board[i];
	int ret = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (!visited[i][j] && board[i][j]=='0') {
				ret++;
				DFS(i, j);
			}
	cout << ret << "\n";
}

#include <queue>
void solve_by_BFS() {
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> board[i];
	int ret = 0;
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			if (board[i][j] == '0' && !visited[i][j]) {
				ret++;
				queue<pair<int,int>>q;
				q.push({ i,j });
				while (!q.empty()) {
					int x = q.front().first;
					int y = q.front().second;
					q.pop();
					for (int i = 0; i < 4; i++) {
						int dx = x + dir[i][0];
						int dy = y + dir[i][1];
						if (inRange(dx, dy) && board[dx][dy] == '0' && !visited[dx][dy]) {
							visited[dx][dy] = true;
							q.push({ dx,dy });
						}
					}
				}
			}
	cout << ret << "\n";
}

int main() {
	solve_by_BFS();
}