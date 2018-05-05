#include<bits/stdc++.h>                      //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
long long int poww(long long int first,long long int second){         //power function
	long long int x=1;
	if(second==0){
		return 1;
	}
	else{
		for(int i=0;i<second;i++){
			x=x*first;
		}
	}
	return x;

}
double intlog(double base, double x) {
    return (double)(log(x) / log(base));
}
void run(){
	int power,mod;
	cin >> power >> mod;
	int temp=mod;
	double ans=intlog(2,mod);
	if(ans<power){
		cout << temp<<"\n";
		return;
	}
	while(ans>power){
		
			
			ans=intlog(2,mod);
			mod=mod/2;
			//cout << mod<<"\n\n";
		
	}	
	cout << temp%mod<<"\n";
	



}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}