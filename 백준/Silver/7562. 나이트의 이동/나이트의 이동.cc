#include <iostream>
#include <queue>
#include <utility>

using namespace std;


//struct Posistion {
//	int row;
//	int col;
//	Posistion(int _row, int _col) : row(_row), col(_col) { };
//};

pair<int, int> move[8] = { {-2, -1}, {-1, -2}, {1, -2}, {2,-1}, {2,1}, {1,2}, {-1,2}, {-2,1} };

bool isVaild(pair<int, int> position, int I) {
	if (position.first < 0 || position.first >= I || position.second < 0 || position.second >= I)
		return false;
	return true;
}



int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), ::cout.tie(NULL);
	
	int test;
	cin >> test;
	
	for (int i = 0; i < test; i++) {
		int I;
		int **graph;

		cin >> I;

		graph = new int*[I];
		for (int j = 0; j < I; j++) {
			graph[j] = new int[I];
			for (int k = 0; k < I; k++)
				graph[j][k] = 0;
		}
		
		pair<int, int> start, end;
		cin >> start.first>> start.second;
		cin >> end.first >> end.second;

		if (start == end) {
			::cout << 0 << "\n";
			continue;
		}

		queue<pair<int, int>> queue;
		queue.push(start);

		bool state = false;
		while (!queue.empty()) {
			pair<int, int> position = queue.front();
			queue.pop();

			for (int i = 0; i < 8; i++) {
				pair<int, int> temp;
				temp.first = position.first + ::move[i].first;
				temp.second = position.second + ::move[i].second;
				if (!isVaild(temp, I) || graph[temp.first][temp.second] > 0)
					continue;

				queue.push(temp);
				if (graph[temp.first][temp.second] == 0 || graph[temp.first][temp.second] >= graph[position.first][position.second] + 1)
					graph[temp.first][temp.second] = graph[position.first][position.second] + 1;
			
			}

			if (state) break;
		}	
		
		::cout << graph[end.first][end.second] << "\n";
	}
	

}