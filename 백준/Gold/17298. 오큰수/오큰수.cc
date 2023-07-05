#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

int main(){

	int n;
	scanf("%d", &n);

	vector<int> list;
	stack<int> stack;
	int* answer = new int[n];

	for (int i = 0; i < n; i++) {
		int tmp;
		scanf("%d", &tmp);
		list.push_back(tmp);
	}

	for (int i = n - 2; i >= 0; i--) {
		if (list.at(i) < list.at(i + 1)) {
			stack.push(list.at(i + 1));
			answer[i] = list.at(i + 1);
		}
		else {
			while (!stack.empty()) {
				if (stack.top() > list.at(i)) {
					answer[i] = stack.top();
					break;
				}
				stack.pop();
			}
			if (stack.empty())
				answer[i] = -1;
		}

	}
	answer[n - 1] = -1;

	for (int i = 0; i < n; i++)
		printf("%d ", answer[i]);
}