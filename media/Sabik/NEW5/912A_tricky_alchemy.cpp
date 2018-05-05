#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	long long int yellow,blue,YCRY=0,BCRY=0;
	cin >> yellow >> blue;
	long long int Y,G,B,needed=0;
	cin >> Y >> G >>B;
	YCRY=2*Y;
	BCRY=3*B;
	YCRY+=G;
	BCRY+=G;
	
	if(YCRY>yellow){
		needed+=YCRY-yellow;
	}
	if(BCRY>blue){
		needed+=BCRY-blue;
	}
	cout << needed <<"\n";

}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}