#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	long long size,left,right;
	cin >> size;
	long long a[size],squares[100000],bro,b[size],sum;
	squares[0]=0;
	squares[1]=1;
	for(int j=2;j<=100000;j++){
		squares[j]=j*j;
		//cout << squares[j] <<"\n";
	}
	double check;
	for(int i=0;i<size;i++){
		cin >> a[i];
		check = sqrt(a[i]);
		bro=int(check);
		//cout << bro<<endl;
		check=abs(int(check)-double(check));
		//cout << check <<"\n";
		if(check==0){
			b[i]=0;
		}
		else{
			if(check>=0.5){
				b[i]=abs(squares[bro+1]-a[i]);
			}
			else{
				b[i]=abs(squares[bro]-a[i]);	
			}
		}
		//cout << check <<"\n";
	}
	sort(b,b+size);
	for(int i=0;i<size;i++){
	//	cout << b[i] <<"\n";
	}
	sum=0;
	for(int i=0;i<size/2;i++){
		sum+=b[i];
	}
	if(sum==0){
		sort(a,a+size);
		for(int i=size/2;i<size;i++){
			if(b[i]==0){
				if(a[i]==0){
					sum+=2;
				}
				else{
					sum+=1;
				}
			}
		}	
	}
	cout << sum <<"\n";


}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}