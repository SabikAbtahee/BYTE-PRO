#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int testCase,a,b,left=0,right=0;
	cin >> testCase;
	for(int i=0;i<testCase;i++){
		cin >> a >> b;
		if(a<0){
			left++;
		}
		else if(a>0){
			right++;
		}
	}
	if(left==0 || left==1 || right ==0 || right==1){
		cout << "Yes\n";
	}
	else{
		cout << "No\n";
	}


}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}