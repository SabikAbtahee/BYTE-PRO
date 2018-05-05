#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int size,query,l,r;
	cin >> size >> query;
	string falseLine;
	//getline(cin,falseLine);
	char str[size],charr,replace;
	for(int i=0;i<size;i++){
		cin >> str[i];
		//cout << str[i];

	}
	for(int i=0;i<query;i++){
		cin >> l >> r >> charr >> replace;
		//cout << l << r << charr << replace<<endl;
		for(int k=l-1;k<r;k++){
			if(str[k]==charr){
				
				str[k]=replace;
			}
		}
	}
	for(int i=0;i<size;i++){
		cout << str[i];
	}

}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}