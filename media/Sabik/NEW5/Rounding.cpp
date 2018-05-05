#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	long long int x,y;
	cin >> x;
	y=x%10;
	if(y>5){
		x=x+(10-y);
	}
	else{
		x=x-y;
	}
	cout << x << "\n";
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}