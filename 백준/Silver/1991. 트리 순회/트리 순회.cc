#include <iostream>
#include <map>

using namespace std;

typedef struct node {
	char left;
	char right;
}node;

map<char, node> tree;

void inorder(char t) {
	if (t == '.')return;
	node temp = tree.find(t)->second;
	inorder(temp.left);
	cout << t;
	inorder(temp.right);
}

void preorder(char t) {
	if (t == '.')return;
	cout << t;
	node temp = tree.find(t)->second;
	preorder(temp.left);
	preorder(temp.right);
}

void postorder(char t) {
	if (t == '.')return;
	node temp = tree.find(t)->second;
	postorder(temp.left);
	postorder(temp.right);
	cout << t;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;
	

	char p, l, r;
	for (int i = 0; i < n; i++) {
		cin >> p >> l >> r;
		node child;
		child.left = l;
		child.right = r;
		tree.insert({ p, child });
	}

	preorder('A');
	cout << '\n';
	inorder('A');
	cout << '\n';
	postorder('A');
	cout << '\n';
}