#include <iostream>
#include <cmath>

using namespace std;

//1. 원반이 한 개면 그냥 옮기면 끝이다(종료 조건).
//2. 원반이 n개일 때
//1) 1번 기둥에 있는 n개 원반 중 n - 1개를 2번 기둥으로 옮긴다(3번 기둥을 보조 기둥으로 사용).
//2) 1번 기둥에 남아 있는 가장 큰 원반을 3번 기둥으로 옮긴다.
//3) 2번 기둥에 있는 n - 1개 원반을 다시 3번 기둥으로 옮긴다(1번 기둥을 보조 기둥으로 사용).


//int count = 0; 어차피 n이 정해지면 count도 정해짐! 굳이 ++ 할 필요가 X

void hanoiTower(int n, int from, int to, int assist, int orginalN) {
	if (n == 1) {
		printf("%d %d\n", from, to);				//cout과 printf의 차이가 생각보다 크다!
		return;
	}
	hanoiTower(n - 1, from, assist, to, orginalN);
	printf("%d %d\n", from, to);
	//hanoiTower(1, 1, 3, 2); == count++;
	hanoiTower(n - 1, assist, to, from, orginalN);
}

void printLargeNum(int n, int array[]) {		//long long 을 범어나는 범위의 숫자를 표현하기 위해 ㅅㅂ c++
	for (int j = 1; j <= n ; j++) {
		for (int i = 0; i < j; i++) {
			array[i] *= 2;
		}
		for (int i = 0; i < j; i++) {
			if (array[i] >= 10) {
				array[i + 1] += 1;
				array[i] -= 10;
			}
		}
	}

	array[0] -= 1;
	bool tmp = false;
	for (int i = n - 1; i >= 0; i--) {
		if (array[i] != 0 || tmp) {
			tmp = true;
			printf("%d", array[i]);
		}
	}
	printf("\n");
}

int main() {

	int n;
	int array[100] = { 0 };
	array[0] = 1;
	cin >> n;

	
	if (n <= 20) {
		cout << (long long)(pow(2, n) - 1) << endl;
		hanoiTower(n, 1, 3, 2, n);
	}
	else {
		printLargeNum(n, array);
	}
	

}