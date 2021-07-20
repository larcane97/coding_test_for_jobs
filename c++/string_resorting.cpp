#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve() {
	string s;
	cin >> s;
	vector<char>alphabet;
	int number = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] - '0' >= 0 && s[i] - '0' <= 9)
			number += s[i] - '0';
		else
			alphabet.push_back(s[i]);
	}
	sort(alphabet.begin(), alphabet.end());
	string ret;
	for (int i = 0; i < alphabet.size(); i++)
		ret += alphabet[i];
	if (number != 0) {
		string number_string;
		while (number > 0) {
			number_string += (number % 10)+'0';
			number /= 10;
		}
		for (int i = number_string.size() - 1; i >= 0; i--)
			ret += number_string[i];
	}
	cout << ret << "\n";
}

int main() {
	solve();
}