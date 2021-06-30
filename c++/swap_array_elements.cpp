#include <iostream>
#include <queue>
using namespace std;

void solve() {
	int n, k;
	cin >> n >> k;
	priority_queue<int>a;
	priority_queue<int>b;
	int ret = 0;
	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		ret += tmp;
		a.push(-tmp);
	}
	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		b.push(tmp);
	}
	for (int i = 0; i < k; i++) {
		int t1 = -a.top();
		int t2 = b.top();
		b.pop();
		a.pop();
		ret = ret - t1 + t2;
		a.push(-t2);
		b.push(t1);
	}
	cout << ret << "\n";

}

int main() {
	solve();
}