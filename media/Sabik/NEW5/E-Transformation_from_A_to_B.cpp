#include<bits/stdc++.h>
#include<string>
using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
int number, checkNumber;
int allcount[10000];
int indexFound=-1;
bool found=false;
vector<int> answer;
//int count =1;
/*void recur(long long int x,int count){
	long long int mul,addidtion;
	allcount[count-1]=x;
	mul=2*x;
	cout << mul << "\n";
	addidtion=10*x+1;
	cout << addidtion << "\n";
	if(x==checkNumber){
		indexFound=count;
		found=true;
		return;
	}
	if(x>checkNumber){
		return;
	}
	if(found==false){
		recur(addidtion,count+count+1);
		recur(mul,count+count);
		
		
	}
	//recur(addidtion,count+count+1);
}

void go(int yolo){

	answer.push_back(allcount[yolo-1]);
	//cout << yolo-1 <<"\n";
	if(yolo-1==0){
		return;
	}
	if(yolo%2==0){
		yolo=yolo/2;
		go(yolo);
	}
	else{
		yolo--;
		yolo=yolo/2;
		go(yolo);
	}
}

void run(){
	cin >> number >> checkNumber;
	if(number>100000 || checkNumber>=1000000000){
		cout << "NO\n";
	}
	else{
		recur(number,1);
		//sort(allcount,allcount+1000);
		/*for(int i=1000-1;i>(1000-100);i--){
			cout << allcount[i] <<"\n";
		}
		if(indexFound==-1){
			cout << "NO\n";
		}
		else{
			cout << "YES\n";
			go(indexFound);
			cout << answer.size() << "\n";
			for(vector<long long int>::iterator it = answer.end()-1 ; it != answer.begin()-1; --it){
				cout << *it <<" ";
			}
			cout << "\n";
		}
	}
}
*/
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


int divide(int z){
	return z/2;
}
int removeOne(int z){
	string ss;
	ss=IntToStr(z);
	ss.erase(ss.end()-1);

	z=strToInt(ss);
	return z;
}

void recur2(int z){
	if(z==number){
		found=true;
		return;
	}
	else if(z<number || z<=0){
		found=false;
		return;
	}
	if(z%2==0){
		z=divide(z);
		answer.push_back(z);
	}
	else if(z%10==1){
		z=removeOne(z);
		answer.push_back(z);
		
	}
	else{
		found=false;
		return;
	}
	//cout << z;
	recur2(z);
}

void run2(){
	cin >> number >> checkNumber;
	recur2(checkNumber);
	if(found==true){
		cout <<"YES\n";
		cout << answer.size()+1<<"\n";
		
		for(vector<int>::iterator it=answer.end()-1;it!=answer.begin()-1;--it){
			cout << *it <<" ";
		}
		cout << checkNumber << "\n";
	}
	else{
		cout << "NO\n";
	}
}

int main(){
	file();
	//run();

	run2();
	return 0;
}