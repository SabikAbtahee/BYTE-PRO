#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){

	int a,b,ans;
	while((scanf("%d%d",&a,&b))!=EOF){
		ans=a*b*2;
		cout << ans <<"\n";
	}
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}