#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
string IntToStr(int x){
	string str;
	//str=to_string(x);
	ostringstream ss;
	ss << x;
	return ss.str();
}
int charToInt(char x){
	int p=int(x)-48;
	return p;
}

long long convert2(string answer){
	int y=answer.length();
	long long int decimalNumber=0;
	for(int i=0;i<y;i++){
		decimalNumber+=pow(2,i);
	}
	return decimalNumber;
}
long long convert (long long int a){
	int remainderr;
	string ans="";
	long long answer;

	while(a!=0){
		remainderr=a%2;
		if(remainderr==0){
			remainderr=1;
		}
		a/=2;
		ans+=IntToStr(remainderr);

	}
	answer=convert2(ans);
	return answer;
	
	
}



void run(){
	long long int a,b,answer;
	cin >> a >>b;

	if(a>=b){
		answer=convert(a);
	}
	else{
		answer=convert(b);
	}
	if(a==1 || b==1){
		if(a!=1){
			cout << a << "\n";
		}
		else{
			cout << b << "\n";
		}
	}
	else{
		cout << answer <<"\n";
	}
}


int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}