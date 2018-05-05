#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void run(){
	int testCases,length;
	string falseLine;
	cin >> testCases;
	getline(cin,falseLine);
	string str1[testCases];
	getline(cin,str1[0]);
	length=str1[0].size();
	//cout << length;
	int answer=0;
	bool breakFlag=true;
	for(int i=1;i<testCases;i++){
		breakFlag=true;
		getline(cin,str1[i]);

		while(breakFlag){
			if(str1[0].compare(0,length,str1[i],0,length)==0){
				answer=length;
				breakFlag=false;
			}
			else{
				length--;
			}
		}
	}
	cout << answer << "\n";
	


}

int main(){
	file();
	run();
	return 0;
}