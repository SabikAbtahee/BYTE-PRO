#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	long long int a,b,c;
	while((scanf("%lld%lld",&a,&b)) !=EOF){
		c=abs(b-a);
		cout << c <<"\n";
	}
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}