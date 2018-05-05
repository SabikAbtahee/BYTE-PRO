#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

int input;
bool found=false;

vector <int> answer;
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

void recur(int a,int count){
	string temp,temp1;
	int num1,num2;
	if(input==a){
		//cout << count << "\n";
		answer.push_back(count);
		//found=true;
		return;
	}
	if(input<a){
		//cout << count <<"\n";
		answer.push_back(count-1);
		//found=true;
		return;
	}
	else if(found==false){
		temp = IntToStr(a);
		temp1=temp;
		temp=temp+'0';
		num1=strToInt(temp);
		temp1=temp1+'1';
		num2=strToInt(temp1);
		recur(num1,count+count);
		recur(num2,count+count+1);
	}
}

void run(){
	
	cin >> input;
	recur(1,1);
	int l=answer.size();
	//cout << l;
	sort(answer.begin(),answer.end());
	cout << answer[0] << "\n";
	/*for(int i=0;i<answer.size();i++){
		cout << answer[i] <<"\n";
	}*/

}

int main(){
	file();
	run();
	return 0;
}