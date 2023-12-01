#include <iostream>
#include <queue>
#include <functional>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	priority_queue<int, vector<int>, greater<int>> pq;

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		pq.push(temp);
	}

	if (N == 1) {
		cout << 0 << "\n";
		return 0;
	}

	int answer = 0;
	while (true){
		int n1 = pq.top();
		pq.pop();
		int n2 = pq.top();
		pq.pop();

		pq.push(n1 + n2);
		answer += (n1 + n2);
		if (pq.size() == 1)
			break;
	}

	cout << answer << "\n";
}