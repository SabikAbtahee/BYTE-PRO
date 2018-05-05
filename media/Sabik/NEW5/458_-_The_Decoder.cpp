#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	
	string ss,ans="";
	int length;
	
	while(getline(cin,ss)){
		ans="";
		length  = ss.length();
		//cout << length;
		for(int i=0;i<length;i++){
			ans+=ss[i]-7;
			//printf("%c",ss[i]-7);
		}
		cout <<ans<< "\n";
	}
// HELLOW WORLD
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}
// Hellow again