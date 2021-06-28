#include <iostream>
#include <vector>
#include <string>
using namespace std;

int n;
int dir[4][2] = {
	{0,1},
	{1,0},
	{-1,0},
	{0,-1}
};
bool inRange(int x, int y) {
	return x > 0 && x <= n && y > 0 && y <= n;
}

void solve() {
	cin >> n;
	vector<char>direction;

	cin.get();
	string s;
	getline(cin, s);
	for (int i = 0; i < s.size(); i++)
		if (s[i] != ' ')
			direction.push_back(s[i]);

	int x = 1, y = 1;
	for (int i = 0; i < direction.size(); i++) {
		int dx = x, dy = y;
		char d = direction[i];
		if (d == 'R') {
			dx += dir[0][0];
			dy += dir[0][1];
			if (inRange(dx, dy)) {
				x = dx;
				y = dy;
			}
		}
		else if(d=='L') {
			dx += dir[3][0];
			dy += dir[3][1];
			if (inRange(dx, dy)) {
				x = dx;
				y = dy;
			}
		}
		else if (d == 'U') {
			dx += dir[2][0];
			dy += dir[2][1];
			if (inRange(dx, dy)) {
				x = dx;
				y = dy;
			}
		}
		else if (d == 'D') {
			dx += dir[1][0];
			dy += dir[1][1];
			if (inRange(dx, dy)) {
				x = dx;
				y = dy;
			}
		}
	}
	cout << x << " " << y << "\n";
}

int main() {
	solve();
}