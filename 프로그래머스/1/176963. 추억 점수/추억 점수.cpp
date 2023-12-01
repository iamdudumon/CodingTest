#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;

    map<string, int> map;
    for (int i = 0; i < name.size(); i++)
        map.insert({ name.at(i), yearning.at(i) });

    for (int i = 0; i < photo.size(); i++) {
        int sum = 0;
        for (int j = 0; j < photo.at(i).size(); j++) {
            if (map.find(photo.at(i).at(j)) != map.end()) {
                sum += map.find(photo.at(i).at(j))->second;
            }
 
        }
        answer.push_back(sum);
    }

    return answer;
}