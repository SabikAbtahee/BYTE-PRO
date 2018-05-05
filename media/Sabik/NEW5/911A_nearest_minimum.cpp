#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	long long int size,min=10000000000,length=10000000000;
	cin >> size;
	int a[size];
	for(int i=0;i<size;i++){
		cin >> a[i];
		if(a[i]<min){
			min=a[i];
		}
	}
	int count=1;
	bool found=false;
	for(int j=0;j<size;j++){
		if(a[j]==min && found==false){
			count=1;
			found=true;
		}
		else if(a[j]!=min && found==true){
			count++;
		}
		else if(a[j]==min && found==true){
			//count++;
			if(count<length){
				length=count;
			}
			found=false;
			j--;
		}
	}
	cout << length << "\n";
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}