#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int buc,length,ans;
	cin >> buc >> length;
	int *a=new int[buc];
	for(int i=0;i<buc;i++){
		cin >> a[i];

	}
	sort(a,a+buc);
	for(int i=buc-1;i>=0;i--){
		if(length%a[i]==0){
			ans=length/a[i];
			break;
		}
	}
	cout << ans <<"\n";
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}