#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int n,a,b,count=1,left,count1=0,count2=0,min;
	bool dhukenai;
	cin >> n >> a >> b;
	if(a>b){
		min=b;
	}
	else{
		min=a;
	}

	left=n;
	while(true){
		dhukenai=true;
		if(left>=a && count1<4){
			left=left-a;
			count1++;
			dhukenai=false;
		}
		if(left>=b && count2<2){
			left=left-b;
			count2++;
			dhukenai=false;
		}

		if(count2==2 && count1==4){
			break;
		}
		if(dhukenai){
			count++;
			left=n;
		}
		
	}
	cout << count<<"\n";
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}
