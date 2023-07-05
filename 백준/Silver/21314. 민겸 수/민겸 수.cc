#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie();

	string str;
	cin >> str;

	vector<string> vec;
	string tmp = "";
	for (int i = 0; i < str.size(); i++) {
		tmp += str.at(i);
		if (str.at(i) == 'K' || i == str.size() - 1) {
			vec.push_back(tmp);
			tmp = "";
		}
	}

	/*for (int i = 0; i < vec.size(); i++)
		cout << vec.at(i) << endl;*/

	string max = "";
	for (int i = 0; i < vec.size(); i++) {
		if (vec.at(i).at(vec.at(i).size() - 1) == 'K') {
			max += '5';
			for (int j = 0; j < vec.at(i).size() - 1; j++) {
				max += '0';
			}
		}
		else {
			if (i == vec.size() - 1) {
				for (int j = 0; j < vec.at(i).size(); j++) {
					max += '1';
				}
			}
			else {
				max += '1';
				for (int j = 0; j < vec.at(i).size() - 1; j++) {
					max += '0';
				}
			}
		}
	}

	string min = "";
	for (int i = 0; i < vec.size(); i++) {
		if (vec.at(i).at(vec.at(i).size() - 1) == 'K') {
			if (vec.at(i).size() != 1) {
				min += '1';
				for (int j = 0; j < vec.at(i).size() - 2; j++) {
					min += '0';
				}
			}
			min += '5';
		}
		else {
			min += '1';
			for (int j = 0; j < vec.at(i).size() - 1; j++) {
				min += '0';
			}
		}
	}

	cout << max << '\n';
	cout << min << '\n';
}