#include <iostream>

#include <string>
#include <vector>

using namespace std;

char graph[50][50];
int H, W;

struct Coordinate
{
    int row;
    int col;
    Coordinate(int _row, int _col) : row(_row), col(_col) {};
};


Coordinate direct(Coordinate start, string op) {
    char dir = op.at(0);
    int count = stoi(op.substr(2, 1));
    Coordinate temp(start.row, start.col);

    if (dir == 'N') {
        for (int i = 0; i < count; i++) {
            start.row -= 1;
            if (start.row < 0 || graph[start.row][start.col] == 'X')
                return temp;
        }
    }
    else if (dir == 'S') {
        for (int i = 0; i < count; i++) {
            start.row += 1;
            if (start.row >= H || graph[start.row][start.col] == 'X')
                return temp;
        }
    }
    else if (dir == 'W') {
        for (int i = 0; i < count; i++) {
            start.col -= 1;
            if (start.col < 0 || graph[start.row][start.col] == 'X')
                return temp;
        }
    }
    else {
        for (int i = 0; i < count; i++) {
            start.col += 1;
            if (start.col >= W || graph[start.row][start.col] == 'X')
                return temp;
        }
    }

    if (start.row < 0 || start.row >= H || start.col < 0 || start.col >= W) {
        return temp;
    }

    return start;
}

vector<int> solution(vector<string> park, vector<string> routes) {
    vector<int> answer;
    Coordinate start(0, 0);

    H = park.size();
    W = park.at(0).size();
    cout << H << ", " << W << endl;
 
    for (int i = 0; i < park.size(); i++) {
        string row = park.at(i);
        for (int j = 0; j < row.size(); j++) {
            graph[i][j] = row.at(j);
            if (row.at(j) == 'S') {
                start.row = i;
                start.col = j;
            }
        }
    }
    
    
    for (int i = 0; i < routes.size(); i++) {
        string op = routes.at(i);
        start = direct(start, op);
    }

    answer.push_back(start.row);
    answer.push_back(start.col);

    return answer;
}