#include<bits/stdc++.h>

using namespace std;

string separateSentence(string x);

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

long long int fac(long long x){
	
	if(x==0){
		return 1;
	}
	else if(x==1){
		return 1;
	}
	return x*fac(x-1);
}

void run(){
	long long int x;
	cin >> x;
	//x=fac(x);
	for(int i=x-1;i>0;i--){
		x=x*(i);
	}
	cout << x;
}

int main(){
	file();
	run();
	return 0;
}


int strToInt(string x){
	int number;
	istringstream(x) >> number;
	return number;
}
string IntToStr(int x){
	string str;
	//str=to_string(x);
	ostringstream ss;
	ss << x;
	return ss.str();
}
string separateSentence(string x){
	istringstream iss(x);
	string word;
	while(iss >> word){
		cout << word <<"\n";
	}
	return x;
}