#include<bits/stdc++.h>                      //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

int check (int x,int h,int m,int value){
	
	int halfm=(m%10);
	int halfh=(h%10);

	if(halfh==7 || halfm==7){
		return value;
	}
	else{
		int newM=m-x;
		int newH=h;
		if(newM<0){
			newM+=60;
			newH=h-1;
			if(newH<0){
				newH+=24;
			}
		}

		check(x,newH,newM,value+x);
	}


	
}

void run(){
	int x,h,m;
	cin >> x >> h >> m;
	int answer=check(x,h,m,0);
	cout << int(answer/x) <<"\n";
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}