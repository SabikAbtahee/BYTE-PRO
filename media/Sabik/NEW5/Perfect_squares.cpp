#include<bits/stdc++.h>                      //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int arraySize;
	cin >> arraySize;
	int arr[arraySize];
	double root;
	for(int i=0;i<arraySize;i++){
		cin >> arr[i];
	}
	sort(arr,arr+arraySize);
	for(int j=arraySize-1;j>=0;j--){
		root=sqrt(arr[j]);
		if(root-int(root)!=0){
			cout << arr[j] <<"\n";
			break;
		}
	}
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}