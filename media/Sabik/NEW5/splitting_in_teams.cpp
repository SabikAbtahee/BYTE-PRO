#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int x,one=0,two=0,sum=0;
	cin >> x;
	int a[x];
	for(int i=0;i<x;i++){
		cin >> a[i];
		if(a[i]==1){
			one++;
		}
		else{
			two++;
		}

	}
	while(one!=0 && two!=0){
		one--;
		two--;
		sum++;
	}
	if(one>=3){
		sum+=int(one/3);
	}
	cout << sum <<"\n";

}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}