#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(int x, int y) {
	return x > y;
}
void solve() {
	int n, m, k;
	cin >> n >> m >> k;
	vector<int>arr(n);
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	sort(arr.begin(),arr.end(), cmp);

	int ret = 0;
	for (int i = 1; i <= m; i++) {
		if ((i % (k + 1) == 0))
			ret += arr[1];
		else ret += arr[0];
	}
	cout << ret << "\n";
}

int main() {
	solve();
}