#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	string s,falseLine;
	getline(cin,s);
	//getline(cin,falseLine);
	int a;
	cin >> a;

	int len=s.length();
	char x[len];
	set<char> all;
	for(int i=0;i<len;i++){
		x[i]=s[i];
		all.insert(x[i]);
	}
	sort(x,x+len);
	/*for(set<char>::iterator it=all.begin();it!=all.end();it++){
		cout << *it;
	}*/
	int sizee=all.size();
	//cout << sizee;

	if(a>len){
		cout <<"impossible\n";
	}
	else if(sizee>=a){
		cout << "0\n";
	}
	else{
		sizee=a-sizee;
		cout << sizee <<"\n";
	}
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}