#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int pappu,mammu,pola,masha;
	cin >> pappu>>mammu>>pola>>masha;
	int a1,a2,a3,temp,big,small;
	if(pola>masha){
		big=pola;
		small=masha;
	}
	else{
		big=masha;
		small=pola;
	}
	temp=small*2;

	if(temp>=big){
		a3=big;
	}
	else{
		cout << "-1\n";
		return;
	}
	if(mammu>a3){
		a2=mammu*2;
		if(masha*2>=a2){
			cout << "-1\n";
			return;
		}
	}
	else if(mammu<=a3){
		a2=mammu*2;
		if(masha*2>=a2){
			cout << "-1\n";
			return;
		}
	}
	if(pappu>a2){
		a1=pappu*2;
		if(masha*2>=a1){
			cout << "-1\n";
			return;
		}
	}
	else if(pappu<=a2){
		a1=pappu*2;
		if(masha*2>=a1){
			cout << "-1\n";
			return;
		}
	}


	cout << a1 <<"\n"<<a2  <<"\n" << a3 <<"\n";


}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}
