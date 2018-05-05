#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void run(){
	int testCase,x;
	cin >> testCase;
	for(int i=1;i<=testCase;i++){
		cin >> x;
		if(x%3==0 ||x%7==0){
			cout << "YES\n";
		}
		else if(x>11 ||x==10){
			cout << "YES\n";
		}
		else{
			cout << "NO\n";
		}
		
	}
}

int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}
