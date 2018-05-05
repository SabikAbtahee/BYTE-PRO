#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
/*void run2(int testCase){
	int ee;
	int x,x1;
	double y,y1;
	cin >>ee;
	x=sqrt(ee);
	y=sqrt(ee);
	x1=cbrt(ee);
	y1=cbrt(ee);

	cout << x << "  ";
	cout << y << "\n\n";

	cout << x1 << "  ";
	cout << y1 << "\n\n";
	double q = 5.123;
	cout << q-int(q);


}
*/
void run(){
	long long int input;
	double sq,cb,zero1,zero2;
	do{
		cin >> input;
		if(input==0){
			break;
		}
		sq=sqrt(input);
		cb=cbrt(input);
		zero1=sq-int(sq);
		zero2=cb-int(cb);
		if(zero1==0 && zero2==0){
			cout << "Special\n";
		}
		else{
			cout << "Ordinary\n";
		}
		//cout << zero1 << "   "<<zero2 <<"\n";
	}while(true);

}

int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	//run();
	mai();
	return 0;
}
