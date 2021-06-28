#include <iostream>
using namespace std;

bool check(int num) {
	while (num > 1) {
		if ((num % 10) ==3) return true;
		else num /= 10;
	}
	return false;
}

void solve() {
	int n;
	cin >> n;
	int ret = 0;
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j < 60; j++) {
			for (int k = 0; k < 60; k++) {
				if (check(k) || check(j) || check(i))
					ret++;
			}
		}
	}
	cout << ret << "\n";
}

int main() {
	solve();
}