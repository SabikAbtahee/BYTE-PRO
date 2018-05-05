#include<bits/stdc++.h>
using namespace std;

int charToInt(char x);

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void run(){
	int n,jumps,count=0,currentPosition=0,j;
	string road,falseLine;
	cin >> n >> jumps;
	getline(cin,falseLine);
	getline(cin,road);
	j=jumps;
	int path;
	while(currentPosition!=n-1){
			path=currentPosition+j;
			if(path<=n-1){
				if(charToInt(road[path])==1){
					currentPosition=path;
					j=jumps;
					count++;
				}
				else{
					j--;
					if(j==0){
						count=-1;
						break;
					}
				}
			}
			else{
				j--;
				if(j==0){
					count=-1;
					break;
				}
			}
	}
	cout << count;;

}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}

int charToInt(char x){
	int p=int(x)-48;
	return p;
}
