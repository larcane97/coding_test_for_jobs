#include <iostream>
#include <vector>
using namespace std;

void solve() {
	string numbers;
	cin >> numbers;
	int sum = 0;
	for (int i = 0; i < numbers.size() / 2; i++)
		sum += (numbers[i] - '0');
	for (int i = numbers.size() / 2; i < numbers.size(); i++)
		sum -= (numbers[i] - '0');
	if (sum == 0)
		cout << "LUCKY" << "\n";
	else
		cout << "READY" << "\n";
	
}

int main() {
	solve();
}