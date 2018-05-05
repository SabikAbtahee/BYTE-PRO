#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void run(){
	int number,last;
	cin >> number;
	bool found=false;
	do{
		last=number%10;
		if(last==4 || last==7){
			number=number/10;
			if(number==0){
				cout << "YES" << "\n";
				found=true;
				break;
			}
		}
		else{
			break;
		}
	}while(true);

	if((number%4==0 || number%7==0 || number%44==0|| number%47==0|| number%74==0|| number%77==0)&& (found==false)){
		cout << "YES" <<"\n";
	}
	else if(found==false){
		cout << "NO" << "\n";
	}

}
int y,o,number;
bool found=false;
void recur(int x,int z){
	y=x+(4*z);
	cout <<"Y" <<y<<"\n";
	o=x+(7*z);
	cout <<"O"<< o <<"\n";
	if(number%y==0 || number%o==0){
		cout << "YES\n";
		found=true;
		return;
	}
	else if(z<=100){
		z=z*10;
		recur(y,z);
		recur(o,z);
	}
	
}

void run2(){
	//int number;
	cin >> number;
	if(number==4 || number==7 || number%4==0 || number%7==0){
		cout << "YES\n";
		return;
	}
	else{
		recur(4,10);
		recur(7,10);
	}
	if(found==false){
		cout << "NO\n";
	}
}
int main(){
	file();
	//run();
	run2();
	return 0;
}