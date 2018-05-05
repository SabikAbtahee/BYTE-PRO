#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void run2(int testCase){
	int farmers,land,animal,premium,sum=0;
	cin >> farmers;
	for(int i=0;i<farmers;i++){
		cin >> land >> animal >> premium;
		if(animal>0){
			sum+=(land*premium);
		}
	}
	cout << sum <<"\n";
}

void run(){
	int testCase;
	cin >> testCase;
	for(int i=1;i<=testCase;i++){
		run2(i);
	}
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}