#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void checkSurround(char *arr,int H,int W){
	
	for(int j=0;j<H;j++){
		for(int i=0;i<W;i++){
				cout << arr[(j*W)+i];
		}
		cout << "\n";
	}
	/*
	for(int x=0;x<W*H;x++){
		cout << arr[x];
		if((x+1)%W==0){
			cout << "\n";
		}
	}
	*/
}

void run2(int testCase){
	int W,H;
	cin >> W >> H;
	char arr[H][W];

	for(int j=0;j<H;j++){
		for(int i=0;i<W;i++){
				cin >> arr[j][i];
		}
	}
	checkSurround((char *)arr,H,W);
	

}

void run(){
	int testCase;
	cin >> testCase;
	for(int i=1;i<=testCase;i++){
		run2(i);
	}
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}
