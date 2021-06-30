#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool cmp(pair<string, int>p1, pair<string, int>p2) {
	return p1.second < p2.second;
}
void solve() {
	int n;
	cin >> n;
	vector<pair<string, int>>arr(n);
	for (int i = 0; i < n; i++)
		cin >> arr[i].first >> arr[i].second;
	sort(arr.begin(), arr.end(), cmp);
	for (int i = 0; i < arr.size(); i++)
		cout << arr[i].first << " ";

}
int main() {
	solve();
}