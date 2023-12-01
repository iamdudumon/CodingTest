#include <iostream>
#include <queue>
#include <functional>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	priority_queue<long long, vector<long long>, greater <long long> > pq;


	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		long long temp;
		cin >> temp;
		pq.push(temp);
	}

	for (int i = 0; i < N*N - N; i++) {
		int temp;
		cin >> temp;

		if (pq.top() < temp) {
			pq.push(temp);
			pq.pop();
		}
	}

	cout << pq.top() << "\n";
}