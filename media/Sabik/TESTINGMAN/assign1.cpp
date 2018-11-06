#include<bits/stdc++.h>

using namespace std;

int sum(int a,int b){
	return a+b;
}

void run(){
	int a,b;
	cin >>a >> b;
	int answer=sum(a,b);
	cout << answer <<"\n";
}

int main(){
	// ios_base::sync_with_stdio(false);
    // cin.tie(NULL);

	run();
	return 0;
}