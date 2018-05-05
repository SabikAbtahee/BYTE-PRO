#include<bits/stdc++.h>
#include<stdio.h>
#include<math.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
long long int mod,temp;

long long int check(long long int sor,long long int divi){

	mod=sor%divi;
	//cout << mod<< "\n";
	//divi=sor/divi;
	if(mod==0){
		return divi;
	}
	else{
		temp=check(divi,mod);
	}
}

void run(){
	long long int n,x;
	int k;
	long long int answer,q,w;
	cin >> n >> k;
	x=pow(10.0,k);
	//cout << x;

	if(n>x){
		temp=check(n,x);
	}
	else{
		temp=check(x,n);
	}

	//cout <<"\n\n\n" << temp<<"\n\n\n\n";
	q=(n/temp);
	w=(x/temp);
	answer=temp*q*w;
	cout << answer << "\n";
	//printf("%164d\n",answer);
}

int main(){
	file();
	run();
	return 0;
}
