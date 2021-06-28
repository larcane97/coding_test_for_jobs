#include <iostream>
using namespace std;

void solve() {
	int n, k;
	int ret = 0;
	cin >> n >> k;
	while (n != 1) {
		if (n % k == 0) n /= k;
		else n--;
		ret++;
	}
	cout << ret << "\n";
}

int main() {
	solve();
}