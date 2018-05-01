#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int first,second,small=0;
	cin >> first >> second;
	int a[first],b[second],c[first+second];
	for(int i=0;i<first;i++){
		cin >> a[i];
		c[i]=a[i];
	}
	for(int j=0;j<second;j++){
		cin >> b[j];
		c[first+j]=b[j];
	}
	sort(a,a+first);
	sort(b,b+second);
	sort(c,c+(first+second));
	for(int i=0;i<first+second;i++){
		if(c[i]==c[i+1]){
			cout << c[i]<<"\n";
			return;
		}
	}
	/*
	for(int j=0;j<second;j++){
		cout << c[first+j];
	}
	*/
	if(a[0]!=b[0]){
		if(a[0]<b[0]){
			cout << a[0]<<b[0]<<"\n";
		}
		else{
			cout << b[0]<<a[0]<<"\n";
		}
	}
	else{
		cout << a[0] <<"\n";
	}
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}