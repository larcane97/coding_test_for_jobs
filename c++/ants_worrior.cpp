#include <iostream>
#include <vector>
using namespace std;

int dp[101];
int n;

int memoization(int cur,const vector<int>&arr) {
	if (cur >= n) return 0;
	int& ret = dp[cur];
	if (ret != -1) return ret;
	ret = 0;
	// 현재 창고를 터는 경우 & 털지 않는 경우
	ret = max(arr[cur] + memoization(cur + 2,arr),memoization(cur+1,arr));
	return ret;
}

void solve() {
	cin >> n;
	vector<int>arr(n);
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	memset(dp , -1, sizeof(dp));
	cout << memoization(0, arr) << "\n";
}

int main() {
	solve();
}