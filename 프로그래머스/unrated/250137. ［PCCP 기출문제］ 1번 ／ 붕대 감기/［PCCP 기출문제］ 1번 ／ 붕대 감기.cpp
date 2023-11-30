#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    int answer = 0;

    int executeTime = bandage.at(0);
    int maxHealth = health;
    int heal = bandage.at(1);
    int addHeal = bandage.at(2);

    int time = 0;
    int finalTime = attacks.at(attacks.size() - 1).at(0);
    int attackCount = 0;

    for (int i = 0; i <= finalTime; i++) {
        time++;
        if (attacks.at(attackCount).at(0) == i) {
            health -= attacks.at(attackCount).at(1);
            time = 0;
            attackCount++;
        }
        else {
            if (time == executeTime) {
                health += heal + addHeal;
                time = 0;
            }
            else {
                health += heal;
            }

            
            if (health  >= maxHealth) {
                health = maxHealth;
            }
        }
        cout << i << ": " << health << "\n";
        if (health <= 0)
            return -1;
    }

    return health;
}
