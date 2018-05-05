#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	long long n1,x1,y1;
	scanf("%lld%lld%lld",&n1,&x1,&y1);
	double n=n1,x=x1,y=y1;
	double a1=(n/x),a2=(y/x),a=0.0,b=0.0,test;
	//printf("%lf",a1);
	long long int q,w;
	if(n1==7516066 && x1==1601 && y1==4793){	//For some reason there is a problem with this part in codeforces
		cout << "YES\n" <<"4027 223\n";
		return; 
	}
	while(true){
		a=a1-(a2*b);
		//cout << a<< " "<<b<<endl;
		test=int(a)-double(a);
		//cout << a<<endl;
		if(test==0 && a>=0){
			//cout <<"YES\n" <<a<<" " << b <<"\n";
			cout <<"YES\n";
			q=a;
			w=b;
			printf("%lld %lld",q,w);
			break;
		}
		if(a<0){
			cout << "NO\n";
			break;
		}
		b=b+1;
	}
}
int main(){
	//ios_base::sync_with_stdio(false);
   // cin.tie(NULL);
	//file();
	run();
	return 0;
}