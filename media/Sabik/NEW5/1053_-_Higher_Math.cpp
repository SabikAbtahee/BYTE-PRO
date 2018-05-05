#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void ans(){
	int a,b,c;
	cin >> a >> b>> c;
	int s,s1,temp,small,small2,big;
	if(a>=b && a>=c){
		big=a;
		small=b;
		small2=c;
	}
	else if(b>=a && b>=c){
		big=b;
		small=a;
		small2=c;
	}
	else{
		big=c;
		small=a;
		small2=b;
	}
	s=small2*small2+small*small;
	s1=big*big;
	if(s==s1){
		cout << "yes\n";
	}
	else{
		cout << "no\n";
	}
	return;
}

void run(){
	int testCase;
	cin >> testCase;
	for(int i=1;i<=testCase;i++){
		
		//printf("Case %d: ",i);
		cout << "Case "<<i<<": ";
		ans();
		
	}
	
}

int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}


