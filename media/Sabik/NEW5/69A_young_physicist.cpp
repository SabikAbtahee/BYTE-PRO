#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int forces;
	cin >> forces;
	int a,b,c,suma=0,sumb=0,sumc=0;
	for(int i=0;i<forces;i++){
		cin >> a >> b >> c;
		suma+=a;
		sumb+=b;
		sumc+=c;

	}
	if(suma==sumb && sumb==sumc && sumb==0){
		cout << "YES\n";
	}
	else{
		cout << "NO\n";
	}
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}