#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int a[5][5],x,y,ans;
	for(int i=0;i<5;i++){
		for(int j=0;j<5;j++){
			cin >>a[i][j];
			if(a[i][j]==1){
				x=i;
				y=j;
			}
		}
	}
	ans = abs(2-x) + abs(2-y);
	cout << ans <<"\n";
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}