#include<bits/stdc++.h>

using namespace std;



void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void ans(){
	double AB,AC,BC,ratio;
	double R,AD;
	cin >> AB >> AC >> BC >> ratio;
	R=(ratio)/(ratio+1);
	AD=AB*sqrt(R);
	cout << setprecision(10)<<AD<<"\n";
}	

void run(){
	int testCase;
	cin >> testCase;
	for(int i=1;i<=testCase;i++){
		cout << "Case " << i <<": ";
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

